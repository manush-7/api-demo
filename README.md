# Inserting and Extracting Data from RDS using API Gateway and Lambda Function

This module will show you how to create API gateway, how to create a proxy lambda and connect it to RDS MySQL Database and insert records to it vice a versa. Also, it will help to setup an authentication layer with cognito which will be deployed part of the cloud formation. We will also see how can we deploy an automated solution using Serverless framework. 

### 1. Deploy the workshop CloudFormation template
This step will create the necessary resources for workshop. 

<!-- <img width="650" alt="image" src="https://user-images.githubusercontent.com/58434120/169806983-9292c3ca-ad59-40fd-a101-e7db3e6ed706.png"> -->
<img width="550" alt="image" src="https://user-images.githubusercontent.com/58434120/170464691-4aab1105-713b-47a0-91a6-01bd62c3db43.png">

**Step-by-step instructions**

1. Navigate to the Cloudformation folder in the repository and download the template file. 

1. From the AWS console, go to CloudFormation. Click on **Create stack** button.

1. Under **Upload Template**, upload the downloaded template from Local. Click **Next**.

1. Provide a stack name like `immersion-day-workshop`.

1. The default input currently has required fields. 

1. Click **Next** twice.

1. Under **Capabilities**, check both boxes to acknowledge the required resources. Then click on the **Create Stack** button.

1. Once stack is fully deployed, click on the `immersion-day-workshop-[random-string]` stack. Under **Outputs**, note the **Cloudfront** value. You will need this later. 

### 3. Create and test the Lambda that will insert data to RDS

**Step-by-step instructions**

1. From the AWS console, go to Lambda.

1. Click on **Create function** button.

1. Provide a function name like `InsertDatatoRDS`.

1. Choose `Python 3.8` for your runtime.

1. For the execution role, choose `Use an existing role`. In the existing role dropdown, choose the role that the CloudFormation created for you named `Demo-lambda-role-[random-string]`. 

1. Replace the code in lambda_function.py by clicking on upload: 
    1. Zip the contents of folder api-demo/ServerlessFramework-API/
    2. Upload the folder to the lambda function 
    3. Scroll down in Lambda Console and click on edit Runtime Settings. 
    
     ![image](https://user-images.githubusercontent.com/44434434/170463374-e19b10de-9025-4953-830e-4500be70c030.png)
     
    4. Update handler to **api/lambda_function.lambda_handler** 

1. Make sure to replace the **channel** value with your own MediaLive channel ID. Save the Lambda.
1. Let's test this Lambda by clicking on the **Test** button.
1. Give the test a name like `SimpleTest` and hit the **Save** button.
1. Select the test you just created and saved and click the **Test** button.
1. If there were no errors, then the data we wanted to insert should have made to database. 

### 4. Create and test the Lambda that will extract data from RDS to S3

**Step-by-step instructions**

1. From the AWS console, go to Lambda.

1. Click on **Create function** button.

1. Provide a function name like `RDStoS3`.

1. Choose `Python 3.8` for your runtime.

1. For the execution role, choose `Use an existing role`. In the existing role dropdown, choose the role that the CloudFormation created for you named `Demo-lambda-role-[random-string]`. 

1. Replace the code in lambda_function.py by clicking on upload: 
    1. Zip the contents of folder api-demo/ServerlessFramework-API/
    2. Upload the folder to the lambda function 
    3. Scroll down in Lambda Console and click on edit Runtime Settings.
    
     ![image](https://user-images.githubusercontent.com/44434434/170461317-65d4828f-b89d-418b-8a89-a4ac30c5b7f0.png)
     
    4. Update handler to **api/handler.extract** 

1. Make sure to replace the **channel** value with your own MediaLive channel ID. Save the Lambda.
1. Let's test this Lambda by clicking on the **Test** button.
1. Give the test a name like `SimpleTest` and hit the **Save** button.
1. Select the test you just created and saved and click the **Test** button.
1. If there were no errors, then the data we wanted from RDS should have made to S3.


## Completion

Congratulations! You've successfully created a API with Lambda function that inserts data and retrives data from the database. In addition, you have automated your deployment using Server Framework.


## Cloud Resource Clean Up

### CloudFormation
Select and delete the CloudFormation templates deployed as part of the prerequisites. This will clean up all the resources created by the template. 

### AWS API Gateway
Select the configuration you created manually and hit the **Delete** button to remove the configuration.

### AWS API Gateway
Select the Lambda Functions that you created manually and hit the **Delete** button to remove the functions. 

### Serverless Framework 
Run Command ```sls destroy```
