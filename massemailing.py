import boto3

def send_mass_emails(event, context):
    ses_client = boto3.client(
        'ses',
        region_name='ap-south-1',
        aws_access_key_id='YOUR_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'
    )
    subject = 'Your Subject'
    body_html = '''
        <html>
            <head>
                <meta charset="UTF-8">
                <title>Email Template</title>
            </head>
            <body>
                <h1>Welcome to our Newsletter!</h1>
                <p>Dear {{name}},</p>
                <p>We are excited to share the latest news and updates with you.</p>
                <p>Here are some highlights:</p>
                <p>Stay tuned for more exciting updates!</p>
                <p>Best regards,</p>
                <p>Your Team</p>
            </body>
        </html>
    '''
    body_text = 'Plain text body content'
    sender = 'jinxforever8341@gmail.com'
    recipients = ['recipient1@example.com', 'recipient2@example.com']

    for recipient in recipients:
        try:
            response = ses_client.send_email(
                Source=sender,
                Destination={'ToAddresses': [recipient]},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {
                        'Html': {'Data': body_html},
                        'Text': {'Data': body_text}
                    }
                }
            )
            print(f"Email sent to {recipient}. Message ID: {response['MessageId']}")
        except Exception as e:
            print(f"Error sending email to {recipient}: {str(e)}")
