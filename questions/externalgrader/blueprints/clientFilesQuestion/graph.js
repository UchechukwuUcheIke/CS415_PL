// --------------------------------------------------
  // GLOBAL VISUAL SETTINGS
  // --------------------------------------------------

  LiteGraph.NODE_TITLE_HEIGHT = 28;
  LiteGraph.NODE_SLOT_HEIGHT = 22;
  LiteGraph.NODE_DEFAULT_BGCOLOR = "#2c2f33";
  LiteGraph.NODE_DEFAULT_BOXCOLOR = "#0057b8";
  LiteGraph.BACKGROUND_COLOR = "#1e1e1e";
  LiteGraph.ROUND_RADIUS = 8;

  // --------------------------------------------------
  // SAFE CANVAS CREAsTION
  // --------------------------------------------------

  const container = document.getElementById("graph-container");

  const canvasEl = document.createElement("canvas");
  canvasEl.width = container.clientWidth || 800;
  canvasEl.height = 600;
  container.appendChild(canvasEl);

  const graph = new LGraph();
  const canvas = new LGraphCanvas(canvasEl, graph);

  canvas.background_color = "#1e1e1e";

  // --------------------------------------------------
  // BLUEPRINT BASE NODE (PROPERLY EXTENDS LGraphNode)
  // --------------------------------------------------

  function BlueprintNode() {
      LGraphNode.call(this);
      this.size = [220, 120];
  }

  BlueprintNode.prototype = Object.create(LGraphNode.prototype);
  BlueprintNode.prototype.constructor = BlueprintNode;

  // Header + body drawing
  BlueprintNode.prototype.onDrawBackground = function(ctx) {

      const w = this.size[0];
      const h = this.size[1];

      // Body
      ctx.fillStyle = "#2c2f33";
      ctx.beginPath();
      ctx.roundRect(0, 0, w, h, 8);
      ctx.fill();

      // Header
      ctx.fillStyle = "#0057b8";
      ctx.beginPath();
      ctx.roundRect(0, 0, w, 28, [8,8,0,0]);
      ctx.fill();

      // Divider
      ctx.strokeStyle = "#1e1e1e";
      ctx.beginPath();
      ctx.moveTo(0, 60);
      ctx.lineTo(w, 60);
      ctx.stroke();
  };

  // Blueprint-style pin layout
  BlueprintNode.prototype.getSlotPosition = function(slot, isInput) {

      const x = isInput ? 0 : this.size[0];
      const slots = isInput ? this.inputs : this.outputs;
      const slotInfo = slots[slot];

      let execIndex = 0;
      let dataIndex = 0;

      for (let i = 0; i < slot; i++) {
          if (slots[i].type === LiteGraph.EVENT)
              execIndex++;
          else
              dataIndex++;
      }

      let y;

      if (slotInfo.type === LiteGraph.EVENT) {
          y = 38 + execIndex * 20;   // exec near top
      } else {
          y = 70 + dataIndex * 22;   // data lower
      }

      return [x, y];
  };

  BlueprintNode.prototype.onResize = function() {
      const total = (this.inputs?.length || 0) +
                    (this.outputs?.length || 0);
      this.size[1] = 100 + total * 22;
  };

  // --------------------------------------------------
  // BEGIN PLAY NODE
  // --------------------------------------------------

  function BeginPlayNode() {
      BlueprintNode.call(this);
      this.title = "BeginPlay";
      this.addOutput("Exec", LiteGraph.EVENT);
  }
  BeginPlayNode.title = "BeginPlay";
  BeginPlayNode.prototype = Object.create(BlueprintNode.prototype);
  BeginPlayNode.prototype.constructor = BeginPlayNode;

  LiteGraph.registerNodeType("blueprint/beginplay", BeginPlayNode);

  // --------------------------------------------------
  // PRINT STRING NODE
  // --------------------------------------------------

  function PrintNode() {
      BlueprintNode.call(this);
      this.title = "Print String";
      this.addInput("Exec", LiteGraph.EVENT);
      this.addInput("In String", "string");
      this.addOutput("Then", LiteGraph.EVENT);
  }
  PrintNode.title = "Print String";
  PrintNode.prototype = Object.create(BlueprintNode.prototype);
  PrintNode.prototype.constructor = PrintNode;

  LiteGraph.registerNodeType("blueprint/print", PrintNode);

  // --------------------------------------------------
  // BRANCH NODE
  // --------------------------------------------------

  function BranchNode() {
      BlueprintNode.call(this);
      this.title = "Branch";
      this.addInput("Exec", LiteGraph.EVENT);
      this.addInput("Condition", "number");
      this.addOutput("True", LiteGraph.EVENT);
      this.addOutput("False", LiteGraph.EVENT);
  }
  BranchNode.title = "Branch";
  BranchNode.prototype = Object.create(BlueprintNode.prototype);
  BranchNode.prototype.constructor = BranchNode;

  LiteGraph.registerNodeType("blueprint/branch", BranchNode);

  // --------------------------------------------------
  // ADD NODES TO GRAPH
  // --------------------------------------------------

  /**
  const n1 = LiteGraph.createNode("blueprint/beginplay");
  n1.pos = [150, 250];
  graph.add(n1);

  const n2 = LiteGraph.createNode("blueprint/print");
  n2.pos = [450, 220];
  graph.add(n2);

  const n3 = LiteGraph.createNode("blueprint/branch");
  n3.pos = [450, 350];
  graph.add(n3);

  graph.start();
  **/
/** */
  function buildGraphFromJSON(graphData) {

    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        console.log("Loading saved graph from localStorage");
        graph.configure(JSON.parse(saved));
        return;
    }

    const nodeMap = {}; // backend id → actual node instance

    // -----------------------------
    // 1️⃣ Create Nodes
    // -----------------------------
    graphData.nodes.forEach(nodeData => {

        const node = LiteGraph.createNode(nodeData.type);

        if (!node) {
            console.error("Unknown node type:", nodeData.type);
            return;
        }

        node.pos = nodeData.pos || [100, 100];

        // Clear default slots (important if constructor added them)
        node.inputs = [];
        node.outputs = [];

        // Recreate inputs
        if (nodeData.inputs) {
            nodeData.inputs.forEach(input => {
                node.addInput(
                    input.name,
                    input.type === 0 ? LiteGraph.EVENT : input.type
                );
            });
        }

        // Recreate outputs
        if (nodeData.outputs) {
            nodeData.outputs.forEach(output => {
                node.addOutput(
                    output.name,
                    output.type === 0 ? LiteGraph.EVENT : output.type
                );
            });
        }

        graph.add(node);
        nodeMap[nodeData.id] = node;
    });

    // -----------------------------
    // 2️⃣ Create Links
    // -----------------------------
    graphData.links.forEach(link => {

        const [
            linkId,
            originNodeId,
            originSlot,
            targetNodeId,
            targetSlot
        ] = link;

        const originNode = nodeMap[originNodeId];
        const targetNode = nodeMap[targetNodeId];

        if (!originNode || !targetNode) {
            console.warn("Invalid link:", link);
            return;
        }

        originNode.connect(originSlot, targetNode, targetSlot);
    });

    graph.start();
}

document.addEventListener("DOMContentLoaded", function() {
    buildGraphFromJSON(initialGraph);
});


  // --------------------------------------------------
  // SAVE GRAPH STATE
  // --------------------------------------------------
function captureGraphState() {
    const graphData = graph.serialize();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(graphData));

    const graphJSON = JSON.stringify(graphData);
    const input = document.querySelector('input[name="student_graph"]');
    if (input) {
        input.value = graphJSON;
        console.log("Graph captured! Length:", graphJSON.length);
    }
}

// Capture on any graph change
graph.onNodeAdded = captureGraphState
graph.onNodeRemoved = captureGraphState
graph.onConnectionChange = captureGraphState