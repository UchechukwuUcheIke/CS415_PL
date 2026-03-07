window.GraphEvents = {}

GraphEvents.showNodeSearch = function( canvas, graph, screenX, screenY, canvasX, canvasY) {
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

GraphEvents.handleDoubleClick = function(e, canvas, graph)
{
    const rect = canvas.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    GraphEvents.showNodeSearch(canvas, graph, e.clientX, e.clientY, x, y);
}

GraphEvents.attachCanvasEvents = function(canvas, graph)
{
    canvas.canvas.addEventListener("dblclick", (e) => {
        GraphEvents.handleDoubleClick(e, canvas, graph)
    });
}


