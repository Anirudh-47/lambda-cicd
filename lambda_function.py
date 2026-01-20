def lambda_handler(event, context):
    print("Lambda deployed via GitHub Actions successfully")

    return {
        "statusCode": 200,
        "body": "Hello from Lambda CI/CD"
    }
