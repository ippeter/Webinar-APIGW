# -*- coding:utf-8 -*-
import json

def handler(event, context):
    
    # Prepare the output
    result = {}
    
    result["headers"] = {"Content-Type": "application/json"}
    result["statusCode"] = 200

    data = {"Status": "Awesome, it works!"}
    result["body"] = json.dumps(data)

    return result
