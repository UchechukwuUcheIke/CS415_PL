def to_litegraph_json(graph):
    """
    Convert internal Graph representation
    into LiteGraph JSON format.
    """

    litegraph_nodes = []
    litegraph_links = []
    link_id = 0

    # Map node id -> index (LiteGraph expects numeric IDs)
    node_id_map = {}

    for index, node in enumerate(graph.nodes):
        node_id_map[node.id] = index

        litegraph_nodes.append({
            "id": index,
            "type": node.type_name,
            "pos": [node.x, node.y],
            "size": [200, 100],  # basic default
            "inputs": [
                {"name": pin_name, "type": 0}
                for pin_name in node.inputs
            ],
            "outputs": [
                {"name": pin_name, "type": 0, "links": []}
                for pin_name in node.outputs
            ],
            "properties": {}
        })

    # Build links
    for (from_id, from_slot, to_id, to_slot) in graph.links:
        from_index = node_id_map[from_id]
        to_index = node_id_map[to_id]

        litegraph_links.append([
            link_id,          # link id
            from_index,       # origin node
            from_slot,        # origin slot index
            to_index,         # target node
            to_slot,          # target slot index
            0                 # type
        ])

        # Also register link inside output slot (LiteGraph expects this)
        litegraph_nodes[from_index]["outputs"][from_slot]["links"] = [link_id]

        link_id += 1

    return {
        "last_node_id": len(litegraph_nodes),
        "last_link_id": link_id,
        "nodes": litegraph_nodes,
        "links": litegraph_links
    }

def from_litegraph_json():
    pass