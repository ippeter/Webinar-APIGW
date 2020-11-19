## Webinar-APIGW
### Serverless functions for the API Gateway demo

## Description

### backend.py
This is a basic API GW backend, which simply responds with a "Awesome, it works!" message, regardless of the function input.
It's ok for a quick demo.

### calculator.py
This is a more sophisticated example, when you want to pass additional parameters and get a corresponding response.  
**Please note, that API GW base64-encodes the request body!**  
This is why calculator.py decodes the body in the first line.  

Expected body schema:  

{  
"x": integer  
"y": integer  
"action": string, one of "+", "-", "*", "/"  
}  

Response body schema:  

{  
"Result": float  
}  


## Installation

1. Go to the FunctionGraph service
2. Create a new Python3.6 function
3. Simply copy/paste the code into the function
