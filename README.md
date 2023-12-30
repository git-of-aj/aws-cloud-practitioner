# aws-cloud-practitioner


## API Gateway 
- API Gateway acts as a "front door" for applications to access data, business logic, or functionality from your backend services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, any web application, or real-time communication applications.
- https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html#api-gateway-overview-features
For an app to call publicly available AWS services, you can use Lambda to interact with required services and expose Lambda functions through API methods in API Gateway.

## monitoring
- metrics demo : https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.html
- CloudWatch Logs Insights, you can interactively search and analyze your log data in Amazon CloudWatch Logs. Docs: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html
- alarm demo: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html

## Real Life
1. Aws organisation can invite accounts from same reseller only.. (to avoid currency issue)
2. EIP can be attached to ec2 ONLY IF that VPC has NAT gateway
3. You'll see PUBLIC IP of VPN Gateway after creating a connection => download configuration (generic for cloud), Microsoft means windows server
4. mount newly attched ebs to ec2 : https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html to view permissions:
```sh
ls -ld filepath_of_new-vol
sudo chown -R your_user : filepath
```
