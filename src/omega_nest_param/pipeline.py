"""
This is a boilerplate pipeline
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from pprint import pprint

def demo_node(parameters, nested_parameters):
    print(type(parameters))
    print(parameters["demo_nested"]["param"])
    pprint(parameters)
    print(type(nested_parameters))
    pprint(nested_parameters)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=demo_node,
                inputs=["parameters", "params:demo_nested"],
                outputs=None,
                name="demo"
            )
        ]
    )
