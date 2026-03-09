from blueprints.server_utils import generate_question, grade_submission
from question_utils.create_graph import create_initial_graph, create_solution_graph
from question_utils.blueprint_nodes import NODES_TO_REGISTER
import json

solution_graph = create_solution_graph()
initial_graph = create_initial_graph()

def generate(data):
    generate_question(data, initial_graph, NODES_TO_REGISTER)

def grade(data):
    grade_submission(data, solution_graph)