def lambda_handler(event, context):
    print("Lambda CI/CD pipeline triggered via GitHub Actions")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda CI/CD"
    }
