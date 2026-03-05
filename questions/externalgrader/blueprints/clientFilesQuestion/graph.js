// Visuals
LiteGraph.NODE_TITLE_HEIGHT = 28;
LiteGraph.NODE_SLOT_HEIGHT = 22;
LiteGraph.NODE_DEFAULT_BGCOLOR = "#2c2f33";
LiteGraph.NODE_DEFAULT_BOXCOLOR = "#0057b8";
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

canvas.background_color = "#1e1e1e";