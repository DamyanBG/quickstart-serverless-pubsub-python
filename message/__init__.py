import json

import azure.functions as func


def main(data, actions: func.Out[str]) -> None:
    actions.set(json.dumps({
        'data': '[SYSTEM] ack.',
        'dataType': 'text'
    }))