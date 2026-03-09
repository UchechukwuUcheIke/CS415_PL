from blueprints.litegraph_utils import from_litegraph_json, to_litegraph_json, generate_litegraph_registration_js
from blueprints.graph import graphs_equal
from blueprints.node_type import NODE_TYPES
from pathlib import Path
import json

def _read_file(filename):
    with open(filename) as f:
        return f.read()

def generate_question(data, initial_graph, nodes_to_register=None):
    data["params"]["prompt"] = _read_file("prompt.md")
    #TODO: Fix bug here. not working
    instructions_path = Path(data["options"]["server_files_course_path"])/'blueprints'/'instructions.md'
    data["params"]["instructions"] = _read_file(str(instructions_path))
    data["params"]["storage_key"] =  f"{data['variant_seed']}"
    #Jinja struggles with parsing JSON directly, so we stringify it
    litegraph_json = to_litegraph_json(initial_graph)
    data["params"]["initial_graph"] = json.dumps(litegraph_json)
    # Injects registered node types into question.html

    if nodes_to_register is None:
        nodes_to_register = NODE_TYPES.values()
    data["params"]["node_registration_js"] = generate_litegraph_registration_js(nodes_to_register)

def grade_submission(data, solution_graph):
    student_graph_json = data["submitted_answers"]["student_graph"]
    student_graph = from_litegraph_json(json.loads(student_graph_json))
    
    final_score = 1 if graphs_equal(student_graph, solution_graph) else 0
    data["score"] = final_score