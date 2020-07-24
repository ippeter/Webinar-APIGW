# -*- coding:utf-8 -*-
import json
import base64

def handler(event, context):
    # Decode request body and convert to dict
    body = json.loads(base64.b64decode(event["body"]).decode("utf-8"))

    # Extract parts of the expression
    x = body["x"]
    y = body["y"]
    action = body["action"]

    # Prepare the output
    result = {}
    result["headers"] = {"Content-Type": "application/json"}

    # Evaluate the statement
    if (action in ["+", "-", "*", "/"]):
        result["statusCode"] = 200
        data = {"Result": eval(str(x) + action + str(y))}
    else:
        result["statusCode"] = 400
        data = {"Result": "failure"}
    
    result["body"] = json.dumps(data)

    return result
