import json


def create_thumbnail(event, context):
    body = {"message": "I'm creating the thumbnail", "input": event}

    response = {"statusCode": 200, "body": json.dumps(body)}

    print(response)

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
