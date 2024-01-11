import boto3
from botocore.exceptions import BotoCoreError, ClientError

def send_email(error_message):
    SENDER = "Inevnto App: vasu@sellerlift.com"
    RECIPIENT = "vasu@sellerlift.com"
    AWS_REGION = "us-west-2"  # or your AWS region where SES is configured
    SUBJECT = "Amazon SES Test"
    BODY_TEXT = error_message

    CHARSET = "UTF-8"

    client = boto3.client('ses',region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
