function main()
{
    GraphSetup.setUpLiteGraph();
    GraphSetup.clearRegisteredNodes();
    const BlueprintNodeObj = BlueprintNode.initializeBlueprintNode();
    initializeDynamicNodes(BlueprintNodeObj);

    const graph = new LGraph();
    const canvas = GraphSetup.setUpCanvas(graph)
    GraphEvents.attachCanvasEvents(canvas, graph)

    // I'll think of a better name later
    function captureGraph()
    {
        GraphSerialise.captureGraphState(graph);
    }   

    graph.onNodeAdded = captureGraph
    graph.onNodeRemoved = captureGraph
    graph.onConnectionChange = captureGraph

    document.addEventListener("DOMContentLoaded", function() {
        GraphSerialise.initializeGraph(graph, initialGraph);
    });

    document.getElementById("reset-graph").addEventListener("click", function() {
        resetGraph(graph);
    });
}

main();