window.GraphSerialise = {}

GraphSerialise.loadSavedGraph = function(graph) {
    // For whatever reason, session storage doesn't seem to persist between refreshes
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        graph.configure(JSON.parse(saved));
        graph.start();
        console.log("Successfully loaded");
        return true;
    }
    console.log("Load failed");
    return false;
}

GraphSerialise.createNodes = function(graph, graphData, nodeMap) {
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
}

GraphSerialise.createLinks = function(graph, graphData, nodeMap) {
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
}

GraphSerialise.initializeGraph = function(graph, graphData) {
    const success = GraphSerialise.loadSavedGraph(graph);
    if (success)
    {
        return;
    }

    GraphSerialise.buildGraphFromJSON(graph, graphData);
}

GraphSerialise.buildGraphFromJSON = function(graph, graphData) {
    const nodeMap = {}; // backend id → actual node instance
    GraphSerialise.createNodes(graph, graphData, nodeMap);
    GraphSerialise.createLinks(graph, graphData, nodeMap);
    graph.start();
}

GraphSerialise.captureGraphState = function(graph) {
    const graphData = graph.serialize();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(graphData));
    console.log(JSON.parse(localStorage.getItem(STORAGE_KEY)));

    const graphJSON = JSON.stringify(graphData);
    const input = document.querySelector('input[name="student_graph"]');
    if (input) {
        input.value = graphJSON;
        console.log("Graph captured! Length:", graphJSON.length);
    }
}

function resetGraph(graph)
{
    graph.clear();
    GraphSerialise.buildGraphFromJSON(graph, initialGraph);
    GraphSerialise.captureGraphState(graph);
}

