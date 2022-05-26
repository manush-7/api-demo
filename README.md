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

### 2. Create and test the Lambda that will insert data to RDS

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

### 3. Create and test the Lambda that will extract data from RDS to S3

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

### 4. Create a "Demo" API
Now create an API for your Lambda functions by using the API Gateway console.

**Build a "Demo" API**

1. Sign in to the API Gateway console at https://console.aws.amazon.com/apigateway.

1. If this is your first time using API Gateway, you see a page that introduces you to the features of the service. Under REST API, choose Build. When the Create Example API popup appears, choose OK.
If this is not your first time using API Gateway, choose Create API. Under REST API, choose Build.

1. Create an empty API as follows:
   1. Under Create new API, choose New API.
   2. Under Settings:
      1. For API name, enter LambdaSimpleProxy.
      2. If desired, enter a description in the Description field; otherwise, leave it empty.
      3. Leave Endpoint Type set to Regional.
   3. Choose Create API.
   4. Create the **s3tords** resource as follows:
        1. Choose the root resource (/) in the Resources tree.
        2. Choose Create Resource from the Actions dropdown menu.
        3. Leave Configure as proxy resource unchecked.
        4. For Resource Name, enter **s3tords**.
        5. Leave Resource Path set to /s3tords.
        6. Leave Enable API Gateway CORS checked. 
        7. Choose Create Resource.
   5. In a proxy integration, the entire request is sent to the backend Lambda function as-is, via a catch-all ANY method that represents any HTTP method.  The actual HTTP method is specified by the client at run time. The ANY method allows you to use a single API method setup for all of the supported HTTP methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.
        1. To set up the GET method, do the following:
        2. In the Resources list, choose /s3tords.
        3. In the Actions menu, choose Create method.
        4. Choose GET from the dropdown menu, and choose the checkmark icon
        5. Leave the Integration type set to Lambda Function.
        6. Choose Use Lambda Proxy integration.
        7. From the Lambda Region dropdown menu, choose the region where you created the Lambda function.
        8. In the Lambda Function field, type any character and choose from the dropdown menu.
        9. Leave Use Default Timeout checked.
        10. Choose Save.
        11. Choose OK when prompted with Add Permission to Lambda Function.

### 5. Deploy and test the API
Deploy the API in the API Gateway console

1. Choose Deploy API from the Actions dropdown menu.

1. For Deployment stage, choose [new stage].

1. For Stage name, enter test.

1. If desired, enter a Stage description.

1. If desired, enter a Deployment description.

1. Choose Deploy.

1. Note the API's Invoke URL.

### 6. Use browser and Postman to test an API with Lambda proxy integration

1. To test GET requests using only query string parameters, you can type the URL for the API's s3tords resource into a browser address bar. For example: https://r275xc9bmd.execute-api.us-east-1.amazonaws.com/test/s3tords?bucket_name=paccar-test-mysql-to-s3&file_name=testfile.csv

1. For other methods, you must use more advanced REST API testing utilities, such as POSTMAN or cURL.

## Completion

Congratulations! You've successfully created a API with Lambda function that inserts data and retrives data from the database. In addition, you have automated your deployment using Server Framework.


## Cloud Resource Clean Up

### CloudFormation
Select and delete the CloudFormation templates deployed as part of the prerequisites. This will clean up all the resources created by the template. 

### S3 Bucket
Select the S3 bucket created by CloufFormation and delete it. 

### AWS API Gateway
Select the configuration you created manually and hit the **Delete** button to remove the configuration.

### Lambda Functions
Select the Lambda Functions that you created manually and hit the **Delete** button to remove the functions. 

### Serverless Framework 
Run Command ```sls destroy```
