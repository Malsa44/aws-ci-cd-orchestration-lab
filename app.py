
def main():
    print("Hello from AWS CI/CD Lab!")
    print("Application build successful. Hi Ra Nanna")


def lambda_handler(event, context):
    main()

    return {
        "statusCode": 200,
        "body": "AWS CI/CD Lambda deployment successful!"
    }


if __name__ == "__main__":
    main()
