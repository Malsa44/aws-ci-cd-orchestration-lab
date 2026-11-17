
import json

def lambda_handler(event, context):
    print("AWS CI/CD Lambda deployment successful!")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from AWS CI/CD Pipeline!",
            "status": "success"
        })
    }
