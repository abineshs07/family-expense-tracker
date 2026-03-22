import json


def handler(event, context):
    """
    Sample Lambda handler function.
    
    Args:
        event: The event dict that contains the request data
        context: The context object with methods and properties
    
    Returns:
        dict: Response with statusCode and body
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from sample-lambda!",
            "input": event
        })
    }