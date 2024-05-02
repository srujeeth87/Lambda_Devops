**Lambda Function Deployment with Infrastructure as Code (IaC) and CI/CD Pipeline**

This project demonstrates how to deploy a simple AWS Lambda function using Infrastructure as Code (IaC) and set up a CI/CD pipeline for automated deployments using GitHub Actions.

**Project Structure**
lambda_function.py: Contains the Python code for the Lambda function.
lambda_template.yml: CloudFormation template defining the infrastructure for the Lambda function.
.github/workflows/deploy.yml: GitHub Actions workflow for CI/CD pipeline.

**Prerequisites**
AWS account with appropriate permissions.
GitHub repository to host the project.
AWS CLI installed and configured locally.

**Setup Instructions**
1.Clone this repository:
git clone <repository_url>

2. Navigate to the project directory:
cd <project_directory>

3. Package the Lambda function code:
Ensure you have replaced YOUR_S3_BUCKET_NAME in lambda_stack.yml with your actual S3 bucket name.
Run the following command to package the Lambda function code:

aws cloudformation package --template-file lambda_stack.yml --s3-bucket YOUR_S3_BUCKET_NAME --output-template-file packaged.yaml

4.Deploy the Lambda function:
Run the following command to deploy the Lambda function using the packaged CloudFormation template:

aws cloudformation deploy --template-file packaged.yaml --stack-name LambdaStack --capabilities CAPABILITY_IAM
5.Access the deployed Lambda function in the AWS Management Console. 

**CI/CD Pipeline**
GitHub Actions workflow is triggered on any push to the main branch of the repository.
The workflow lints Python code and deploys the Lambda function automatically.
