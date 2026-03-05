from graph.graph import Graph
from graph.node import Node

def to_litegraph_json(graph):
    litegraph_nodes = []
    litegraph_links = []
    link_id = 0
    
    # Map node id -> numeric index
    node_id_map = {}
    for index, (node_id, node) in enumerate(graph.nodes.items()):
        node_id_map[node_id] = index
        
        litegraph_nodes.append({
            "id": index,
            "type": node.type_name,
            "pos": [node.x, node.y],
            "size": [200, 100],
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
            link_id,
            from_index,
            from_slot,
            to_index,
            to_slot,
            0
        ])
        
        # Register link in output slot
        litegraph_nodes[from_index]["outputs"][from_slot]["links"].append(link_id)
        link_id += 1
    
    return {
        "last_node_id": len(litegraph_nodes),
        "last_link_id": link_id,
        "nodes": litegraph_nodes,
        "links": litegraph_links,
        "config": {}
    }

def from_litegraph_json(litegraph):
    g = Graph()
    
    # Create nodes
    for node_data in litegraph["nodes"]:
        node_id = node_data["id"]
        node_type = node_data["type"]
        
        # Handle both array and object formats for pos
        pos = node_data.get("pos", [0, 0])
        if isinstance(pos, dict):
            x = pos.get("0", 0) if "0" in pos else 0
            y = pos.get("1", 0) if "1" in pos else 0
        else:
            x, y = pos[0], pos[1]
        
        node = Node(node_id, node_type, x, y)
        node.inputs = [inp["name"] for inp in node_data.get("inputs", [])]
        node.outputs = [out["name"] for out in node_data.get("outputs", [])]
        
        g.nodes[node_id] = node
    
    # Build set of actually connected links from node outputs
    # (LiteGraph stores extra garbage links that aren't connected)
    active_link_ids = set()
    for node_data in litegraph["nodes"]:
        for output in node_data.get("outputs", []):
            if output.get("links"):
                active_link_ids.update(output["links"])
    
    # Only process links that are actually connected
    seen_links = set()
    for link in litegraph.get("links", []):
        link_id, origin_id, origin_slot, target_id, target_slot, *_ = link
        
        # Skip if this link isn't actually connected
        if link_id not in active_link_ids:
            continue
        
        link_tuple = (origin_id, origin_slot, target_id, target_slot)
        
        if link_tuple not in seen_links:
            g.links.append(link_tuple)
            seen_links.add(link_tuple)
    
    return g