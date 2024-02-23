Get into Develeoper's Boot : [AWS Dev Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/developer-tools.html)

# How AWS Works 
REst API baiscs
Type of API Calls to aws
Ways to work with aws
AWS SDK
AWS CLI
aws cli hands on  - generate skeleton
- aws sam cli
- aws cognito
- cloidformation basics
boto 3 basics
aws cloud 9 
aws codewispher

# Compute services
- Elastic beanstalk
- ECS
- lambda
- [aws step function](https://aws.amazon.com/step-functions/)
- event bridge
- app runner

# storage 
- rds proxy
- DAX
- elasticache
- ACM
- slide 244,312,436,462,477,502,587
# AWS IAM In dev's Point of view:

IAM revision
role
Users
Policy
Policy boundary
Grant lambda permission to ec2 

# s3 for dev's Deep dive: 
s3 static website hosting demo
s3 prefix 
s3 select
s3 access point
s3 multipart upload
s3 event notifications

# Python with AWS Serviecs :
RDS (MySQL)
DynamoDb

# DevOps Intro
- DevOps lifecycle
- AWS DevOps Services Intro
- github actions
- jira
- xray


Automation: Scripting Knowldeg
1. Less Humans Needed
2. Less Error Prone
3. Repeatable 

bash scripting : AWS CLI 

IAM – Password Policy
IAM – Password Policy
• IAM Access Advisor (user-level)
• Access advisor shows the service permissions granted to a user and when those
services were last accessed.
• You can use this information to revise your policies.

• IAM Credentials Report (account-level)
• a report that lists all your account's users and the status of their various
credentials


• The EC2 User Data Script runs with the root user

Specified in the code or CLI
Environment variables 
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
Default credential profile in the credentials file
Linux, macOS, or Unix: ~/.aws/credentials
Windows: %UserProfile%/.aws/credentials
Instance profile


s3 event notification
object tags 
s3 access points

Amazon S3 access points are unique hostnames (named network endpoints). They are attached to buckets. Using access points, you can share access to S3 buckets with others.

Use cases include: 
Decentralized teams – Each group gets its own access point with tailored permissions and access.
Data lakes – Provide granular control of teams accessing the data lake.
Cross-account data exchange – Grant external users or users from other accounts access to Amazon S3 objects.
Centralized control – Many access points, but one set of policies is used for storage management.

Each Amazon S3 access point is configured with an access policy specific to the use case. Every access point is associated with a bucket. The access point contains a network origin control and a Block Public Access control. 

For example: 
Create an access point with a network origin control that permits storage access only from your virtual private cloud. 
Create an access point with the access point policy configured to allow access only to objects with a defined prefix, such as support.



s3api commands are low level, fine grained so more you can control
s3 - high level less control invokes may call many s3 api calls

JMESPATH Query Basics

