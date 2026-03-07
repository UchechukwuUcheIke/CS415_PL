// Visuals
LiteGraph.NODE_TITLE_HEIGHT = 28;
LiteGraph.NODE_SLOT_HEIGHT = 22;
LiteGraph.NODE_DEFAULT_BGCOLOR = "#2c2f33";
LiteGraph.NODE_DEFAULT_BOXCOLOR = "transparent";
LiteGraph.BACKGROUND_COLOR = "#1e1e1e";
LiteGraph.ROUND_RADIUS = 8;

// Graph container
const container = document.getElementById("graph-container");

const canvasEl = document.createElement("canvas");
canvasEl.width = container.clientWidth || 800;
canvasEl.height = 600;
container.appendChild(canvasEl);

const graph = new LGraph();
const canvas = new LGraphCanvas(canvasEl, graph);

const customLinkTypeColors = {
  event: "#ffffff",   // Exec wires (white)
  "string": "#ff77ff",  // String wires (magenta)
  "number": "#6fb1ff",  // Float wires (blue)
  "bool": "#ff5555",    // Boolean wires (red)
  "vector": "#55dd55",  // Vector wires (green)
  "object": "#ffaa00",  // Object wires (orange)
  "-1": "#999999"       // Wildcard / Any
};


canvas.default_connection_color_byType  = customLinkTypeColors
canvas.default_connection_color_byTypeOff  = customLinkTypeColors

function colorizeLinks() {

    for (const linkId in graph.links) {
        const link = graph.links[linkId];
        if (!link) continue;
        link.color = customLinkTypeColors[link.type] ?? "#ff0000";
    }
}

const originalDrawConnections = LGraphCanvas.prototype.drawConnections;
LGraphCanvas.prototype.drawConnections = function(ctx) {
    colorizeLinks();
    return originalDrawConnections.call(this, ctx);
};


Object.assign(LGraphCanvas.link_type_colors, customLinkTypeColors);
const MIN_ZOOM = 0.5;
const MAX_ZOOM = 1.5;
canvas.min_zoom = MIN_ZOOM;
canvas.max_zoom = MAX_ZOOM;

canvas.background_color = "#1e1e1e";
canvas.allow_searchbox = false;
// Disable zooming entirely
canvas.allow_zoom = false;

// Disable panning entirely
canvas.allow_dragcanvas = false;

colorizeLinks();


canvas.canvas.addEventListener("dblclick", (e) => {
  const rect = canvas.canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  showNodeSearch(e.clientX, e.clientY, x, y);
});

function showNodeSearch(screenX, screenY, canvasX, canvasY) {
  // Remove any existing search UI
  document.getElementById("node-search")?.remove();

  const container = document.createElement("div");
  container.id = "node-search";
  container.style.cssText = `
    position: fixed;
    left: ${screenX}px;
    top: ${screenY}px;
    background: #1a1a1a;
    border: 1px solid #444;
    border-radius: 4px;
    padding: 4px;
    z-index: 9999;
    width: 200px;
  `;

  const input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Search nodes...";
  input.style.cssText = `
    width: 100%;
    background: #2a2a2a;
    color: white;
    border: 1px solid #555;
    padding: 4px;
    box-sizing: border-box;
  `;
  container.appendChild(input);

  const list = document.createElement("div");
  list.style.cssText = `
    max-height: 200px;
    overflow-y: auto;
    margin-top: 4px;
  `;
  container.appendChild(list);

  document.body.appendChild(container);
  input.focus();

  const allTypes = Object.keys(LiteGraph.registered_node_types);

  function renderList(filter) {
    list.innerHTML = "";
    const filtered = allTypes.filter(t => 
      t.toLowerCase().includes(filter.toLowerCase())
    );
    filtered.forEach(type => {
      const item = document.createElement("div");
      item.textContent = LiteGraph.registered_node_types[type].title || type;
      item.style.cssText = `
        padding: 4px 6px;
        cursor: pointer;
        color: #ddd;
        border-radius: 3px;
      `;
      item.addEventListener("mouseenter", () => item.style.background = "#333");
      item.addEventListener("mouseleave", () => item.style.background = "transparent");
      item.addEventListener("mousedown", () => {
        const node = LiteGraph.createNode(type);
        // Convert screen position to graph position
        node.pos = canvas.convertOffsetToCanvas([canvasX, canvasY]);
        graph.add(node);
        container.remove();
      });
      list.appendChild(item);
    });
  }

  renderList("");
  input.addEventListener("input", () => renderList(input.value));

  // Close on outside click
  setTimeout(() => {
    document.addEventListener("mousedown", (e) => {
      if (!container.contains(e.target)) container.remove();
    }, { once: true });
  }, 100);
}