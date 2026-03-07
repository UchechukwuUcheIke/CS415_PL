from blueprints.graph import Graph
from blueprints.node import Node
from blueprints.node_type import NODE_TYPES

def to_litegraph_json(graph):
    litegraph_nodes = []
    litegraph_links = []
    link_id = 0
    
    node_id_map = {}
    for index, (node_id, node) in enumerate(graph.nodes.items()):
        node_id_map[node_id] = index
        
        litegraph_nodes.append({
            "id": index,
            "type": node.type_name,
            "pos": [node.x, node.y],
            "size": [200, 100],
            "inputs": [
                {
                    "name": pin.name, 
                    "type": pin.pin_type.litegraph_data_type, 
                    "color": pin.pin_type.color,
                    "link_color": pin.pin_type.color,
                }
                for pin in node.inputs
            ],
            "outputs": [
                {
                    "name": pin.name, 
                    "type": pin.pin_type.litegraph_data_type, 
                    "color": pin.pin_type.color,
                    "link_color": pin.pin_type.color,
                    "links": []
                }
                for pin in node.outputs
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
    # TODO: Add validation for litegraph json
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

def generate_litegraph_registration_js(nodes_to_register = NODE_TYPES):
    """Generate JavaScript code to register all node types"""
    js_lines = []

    js_lines.append(f"function initializeDynamicNodes(BlueprintNode) {{")
    for node_type in nodes_to_register.values():
        func_name = node_type.type_name.replace("/", "_").title().replace("_", "")
        
        js_lines.append(f"function {func_name}() {{")
        js_lines.append("    BlueprintNode.call(this);")
        js_lines.append(f"    this.title = '{node_type.title}';")
        
        for idx, pin in enumerate(node_type.inputs):
            input_name = pin.name
            pin_type = pin.pin_type
            pin_shape = pin_type.shape
            input_type = pin_type.litegraph_data_type
            input_color = pin_type.color
            js_type = f"\"{input_type}\""
            js_lines.append(f"    this.addInput('{input_name}', {js_type})")
            js_lines.append(f"    this.inputs[{idx}].color = '{input_color}';")
            js_lines.append(f"    this.inputs[{idx}].link_color = '{input_color}';")
            js_lines.append(f"    this.inputs[{idx}].color_on = '{input_color}';")
            js_lines.append(f"    this.inputs[{idx}].color_off = '{input_color}';")
            js_lines.append(f"    this.inputs[{idx}].shape = {pin_shape};")

            if (pin.widget_type is None):
                continue

            js_lines.append(f"this.addWidget('{pin.widget_type}','{input_name}','');")
            js_lines.append(f"this.inputs[{idx}].widget = {{ name: '{input_name}' }};")

        for idx, pin in enumerate(node_type.outputs):
            output_name = pin.name
            pin_type = pin.pin_type
            pin_shape = pin_type.shape
            output_type = pin_type.litegraph_data_type
            output_color = pin_type.color
            js_type = f"\"{output_type}\""
            js_lines.append(f"    this.addOutput('{output_name}', {js_type});")
            js_lines.append(f"    this.outputs[{idx}].color = '{output_color}';")
            js_lines.append(f"    this.outputs[{idx}].link_color = '{output_color}';")
            js_lines.append(f"    this.outputs[{idx}].color_on = '{output_color}';")
            js_lines.append(f"    this.outputs[{idx}].color_off = '{output_color}';")
            js_lines.append(f"    this.outputs[{idx}].shape = {pin_shape};")
        
        js_lines.append("}")
        js_lines.append(f"{func_name}.title = '{node_type.title}';")
        js_lines.append(f"{func_name}.prototype = Object.create(BlueprintNode.prototype);")
        js_lines.append(f"{func_name}.prototype.constructor = {func_name};")
        js_lines.append(f"{func_name}.prototype.color = '{node_type.color}';")
        js_lines.append(f"LiteGraph.registerNodeType('{node_type.type_name}', {func_name});")
        js_lines.append("")
    
    js_lines.append("}")

    return "\n".join(js_lines)