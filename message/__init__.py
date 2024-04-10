import json
import logging

import azure.functions as func


def main(data, actions: func.Out[str]) -> None:
    logging.info(data)
    logging.info(actions)
    actions.set(json.dumps({
        'actionName': 'sendToAll',
        'data': '[SYSTEM] ack.',
        'dataType': 'text'
    }))