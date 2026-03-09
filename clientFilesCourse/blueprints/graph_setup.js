window.GraphSetup = {}

GraphSetup.clearRegisteredNodes = function()
{
    LiteGraph.registered_node_types = {};
    LiteGraph.node_types_by_file_extension = {};
    LiteGraph.Nodes = {};
}

GraphSetup.setUpLiteGraph = function()
{
  LiteGraph.NODE_TITLE_HEIGHT = 28;
  LiteGraph.NODE_SLOT_HEIGHT = 22;
  LiteGraph.NODE_DEFAULT_BGCOLOR = "#2c2f33";
  LiteGraph.NODE_DEFAULT_BOXCOLOR = "transparent";
  LiteGraph.BACKGROUND_COLOR = "#1e1e1e";
  LiteGraph.ROUND_RADIUS = 8;
  LiteGraph.NODE_TITLE_COLOR = "#FFFFFF"; // title text
}

GraphSetup.createCanvas = function(graph)
{
  const container = document.getElementById("graph-container");
  const canvasEl = document.createElement("canvas");
  canvasEl.setAttribute('id', 'graph-canvas');
  canvasEl.width = container.clientWidth || 800;
  canvasEl.height = 600;
  container.appendChild(canvasEl);

  const canvas = new LGraphCanvas(canvasEl, graph);

  return { canvas, canvasEl }
}

GraphSetup.setCanvasColors = function(graph, canvas)
{
  const originalAdd = LGraph.prototype.add;
  LGraph.prototype.add = function(node) {
    originalAdd.apply(this, arguments);
    if (node.computeSize) {
      node.setSize(node.computeSize());
    }
  };

  canvas.background_color = "#1e1e1e";

  // NOTE: Only colors the link when newly connected currently
  const customLinkTypeColors = {
    event: "#ffffff",   // Exec wires (white)
    "string": "#ff77ff",  // String wires (magenta)
    "number": "#6fb1ff",  // Float wires (blue)
    "bool": "#ff5555",    // Boolean wires (red)
    "vector": "#55dd55",  // Vector wires (green)
    "object": "#ffaa00",  // Object wires (orange)
    "-1": "#999999"       // Wildcard / Any
  };

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

  canvas.default_connection_color_byType  = customLinkTypeColors
  canvas.default_connection_color_byTypeOff  = customLinkTypeColors

  colorizeLinks();
}

GraphSetup.clampNodeMovement = function(canvasEl)
{
  const originalDraw = LGraphCanvas.prototype.draw;
  LGraphCanvas.prototype.draw = function() {
    if (this.graph) {
      this.graph._nodes.forEach(node => {
        node.pos[0] = Math.max(0, Math.min(canvasEl.width, node.pos[0]));
        node.pos[1] = Math.max(0, Math.min(canvasEl.height, node.pos[1]));
      });
    }
    return originalDraw.apply(this, arguments);
  };
}

GraphSetup.setCanvasInteraction = function(canvas, canvasEl)
{
  canvas.allow_searchbox = false;
  canvas.allow_dragnodes = true;
  canvas.allow_zoom = false;
  canvas.allow_dragcanvas = false;
  GraphSetup.clampNodeMovement(canvasEl);
}

GraphSetup.setUpCanvas = function(graph)
{
  const { canvas, canvasEl } = GraphSetup.createCanvas(graph);
  GraphSetup.setCanvasColors(graph, canvas);
  GraphSetup.setCanvasInteraction(canvas, canvasEl);
  return canvas;
}

