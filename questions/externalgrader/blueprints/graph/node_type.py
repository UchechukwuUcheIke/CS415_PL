from graph.pin_type import PIN_TYPES

class NodeType:
    def __init__(self, type_name, title, inputs, outputs, color = "#007777"):
        self.type_name = type_name
        self.title = title
        self.inputs = inputs  # list of (name, type) tuples
        self.outputs = outputs
        self.color = color

NODE_TYPES = {
    "blueprint/beginplay": NodeType(
        "blueprint/beginplay",
        "BeginPlay",
        [],
        [("Out", PIN_TYPES["flow"])],
        "#770000"
    ),
    "blueprint/print": NodeType(
        "blueprint/print",
        "Print String",
        [("In", PIN_TYPES["flow"]),("Text", PIN_TYPES["text"])],
        [],
        "#007777"
    ),
    # Add more node types here
}

def generate_litegraph_registration_js():
    """Generate JavaScript code to register all node types"""
    js_lines = []
    
    for node_type in NODE_TYPES.values():
        func_name = node_type.type_name.replace("/", "_").title().replace("_", "")
        
        js_lines.append(f"function {func_name}() {{")
        js_lines.append("    BlueprintNode.call(this);")
        js_lines.append(f"    this.title = '{node_type.title}';")
        
        for idx, (input_name, pin_type) in enumerate(node_type.inputs):
            input_type = pin_type.pin_type
            input_color = pin_type.color
            js_type = "LiteGraph.EVENT" if input_type == "event" else "0"
            js_lines.append(f"    this.addInput('{input_name}', {js_type});")
            js_lines.append(f"    this.inputs[{idx}].color = '{input_color}';")
            js_lines.append(f"    this.inputs[{idx}].link_color = '{output_color}';")

        for idx, (output_name, pin_type) in enumerate(node_type.outputs):
            output_type = pin_type.pin_type
            output_color = pin_type.color
            js_type = "LiteGraph.EVENT" if output_type == "event" else "0"
            js_lines.append(f"    this.addOutput('{output_name}', {js_type});")
            js_lines.append(f"    this.outputs[{idx}].color = '{output_color}';")
            js_lines.append(f"    this.outputs[{idx}].link_color = '{output_color}';")
        
        js_lines.append("}")
        js_lines.append(f"{func_name}.title = '{node_type.title}';")
        js_lines.append(f"{func_name}.prototype = Object.create(BlueprintNode.prototype);")
        js_lines.append(f"{func_name}.prototype.constructor = {func_name};")
        js_lines.append(f"{func_name}.prototype.color = '{node_type.color}';")
        js_lines.append(f"LiteGraph.registerNodeType('{node_type.type_name}', {func_name});")
        js_lines.append("")
    
    return "\n".join(js_lines)