def lambda_handler(event, context):
    print("Lambda CI/CD pipeline executed successfully")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda CI/CD"
    }
