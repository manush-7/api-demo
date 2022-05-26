# Inserting and Extracting Data from RDS using API Gateway and Lambda Function

This module will show you how to create API gateway, how to create a proxy lambda and connect it to RDS MySQL Database and insert records to it vice a versa. Also, it will help to setup an authentication layer with cognito which will be deployed part of the cloud formation. We will also see how can we deploy an automated solution using Serverless framework. 

### 1. Deploy the workshop CloudFormation template
This step will create the necessary resources for workshop. 

<img width="650" alt="image" src="https://user-images.githubusercontent.com/58434120/169806983-9292c3ca-ad59-40fd-a101-e7db3e6ed706.png">

**Step-by-step instructions**

1. Navigate to the Cloudformation folder in the repository and download the template file. 

1. From the AWS console, go to CloudFormation. Click on **Create stack** button.

1. Under **Upload Template**, upload the downloaded template from Local. Click **Next**.

1. Provide a stack name like `immersion-day-workshop`.

1. The default input currently has required fields. 

1. Click **Next** twice.

1. Under **Capabilities**, check both boxes to acknowledge the required resources. Then click on the **Create Stack** button.

1. Once stack is fully deployed, click on the `immersion-day-workshop-[random-string]` stack. Under **Outputs**, note the **Cloudfront** value. You will need this later. 
