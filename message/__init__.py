import json

import azure.functions as func


def main(request, actions: func.Out[str]) -> None:
    req_json = json.loads(request)
    actions.set(
        json.dumps(
            {
                "actionName": "sendToAll",
                "data": f'[{req_json["connectionContext"]["userId"]}] {req_json["data"]}',
                "dataType": req_json["dataType"],
            }
        )
    )
