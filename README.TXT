# Mass Emailing with AWS SES using AWS Lambda and Python

This is a Python script that demonstrates how to send mass emails using AWS SES (Simple Email Service) within an AWS Lambda function.

## Prerequisites

Before setting up the AWS Lambda function and running this code, ensure that you have the following:

- An AWS account with appropriate permissions to create and configure Lambda functions, IAM roles, and SES.

## Setup

1. Clone or download the code from the GitHub repository.

2. Open the `massemailing.py` file in a text editor.

3. Modify the following variables based on your requirements:

    - `subject`: Set the subject of the email.
    - `body_html`: Set the HTML body of the email. You can include placeholders like `{{name}}` for personalized content.
    - `body_text`: Set the plain text body of the email.
    - `sender`: Set the sender's email address. It must be verified in AWS SES.
    - `recipients`: Set the list of recipient email addresses.

4. Save the changes to the `massemailing.py` file.

5. Open the command line or terminal and navigate to the project directory.

6. Run the following command to create a deployment package:

7. Create an AWS Lambda function:

 - Use the AWS Management Console or AWS CLI to create a new Lambda function.
 - Choose "Author from scratch" and provide a name, runtime (Python 3.x), and execution role.
 - In the "Function code" section, select the "Upload a .zip file" option.
 - Upload the `massemailing.zip` file created in the previous step.
 - Set the handler name as `massemail.massemails`.
 - Configure the required environment variables, such as `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`.
 - Set the timeout and other advanced settings as per your needs.
 - Create the Lambda function.

8. Configure the IAM role for the Lambda function:

 - Go to the IAM service in the AWS Management Console.
 - Locate the IAM role created for the Lambda function.
 - Attach the `AmazonSESFullAccess` policy to the role to grant SES permissions.

## Usage

- Once the Lambda function is created and configured, you can trigger it manually or schedule it to run at specific intervals using AWS CloudWatch Events or other triggering mechanisms.

- When the Lambda function runs, it will send the mass email to the recipients specified in the `recipients` variable.

- Check the AWS CloudWatch Logs for the Lambda function to monitor the execution and view any error messages or debugging information.

- You can modify the code or Lambda function settings as needed to meet your specific requirements.


