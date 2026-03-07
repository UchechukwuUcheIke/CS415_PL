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
}

GraphSetup.createCanvas = function(graph)
{
  const container = document.getElementById("graph-container");
  const canvasEl = document.createElement("canvas");
  canvasEl.width = container.clientWidth || 800;
  canvasEl.height = 600;
  container.appendChild(canvasEl);

  const canvas = new LGraphCanvas(canvasEl, graph);

  return canvas
}

GraphSetup.setCanvasColors = function(canvas)
{
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
}

GraphSetup.setCanvasZoom = function(canvas)
{
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
}

GraphSetup.setUpCanvas = function(graph)
{
  const canvas = GraphSetup.createCanvas(graph);
  GraphSetup.setCanvasColors(canvas);
  GraphSetup.setCanvasZoom(canvas);
  return canvas;
}

// Graph container


/** 
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


colorizeLinks();
*/

