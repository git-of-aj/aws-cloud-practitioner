## high level api = multiple api are called in single call

## AWS CLOUD 9:
- uses an ec2 instances BTS
- There is no additional charge for AWS Cloud9. If you use an Amazon EC2 instance for your AWS Cloud9 development environment, you pay only for the compute and storage resources (e.g., an EC2 instance, an EBS volume) that are used to run and store your code. You can also connect your AWS Cloud9 development environment to an existing Linux server (e.g., an on-premises server) via SSH for no additional charge.
-  AWS Free Tier can use AWS Cloud9 for free
- setup: https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial-create-environment.html
## lambda creates s3 thumbnail: https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html
## codewispher
- Amazon CodeWhisperer is an AI coding companion that generates whole line and full function code suggestions in your IDE in real-time, to help you quickly write secure code.
- `AWS Builder ID` is a personal profile that provides access to select tools and services including Amazon CodeCatalyst, Amazon CodeWhisperer, and AWS Training and Certification. AWS Builder ID represents you as an individual and is independent from any credentials and data you may have in existing AWS accounts
- https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html

## aws iam demo of service role and aws cli user profile etc
`The --generate-cli-skeleton` : creates a file in json/yaml to fill all paramaters in it then use by `--cli-input-json/yaml`:
https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html

## aws s3 prefix and delimiter
https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html

## aws s3 access point - https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html
- Let's explore a real-life example to illustrate how AWS S3 Access Points can be used effectively:

**Scenario: Cloud-Based Content Delivery for a Media Streaming Service**

Imagine you are running a media streaming service that stores and serves video content to users globally. You use Amazon S3 to store your media files in multiple AWS regions for redundancy and performance reasons. Here's how AWS S3 Access Points could be applied in this scenario:

1. **Fine-Grained Access Control**: You have different types of media content, including free and premium content. With AWS S3 Access Points, you can create separate access points for each content type, each with its own access policies. For example, you can ensure that only paying subscribers have access to premium content.

2. **Isolation**: You have a separate AWS account for billing and auditing purposes. Access Points can be created in this billing account, providing isolation for billing and audit data while still allowing access to the media files stored in your main AWS account's S3 buckets.

3. **Customized Endpoints**: Each access point can have a custom DNS name like `premium-content.example.com` and `free-content.example.com`, making it easier for your application to direct users to the appropriate content without exposing the full bucket names.

4. **Network Policies**: Access Points allow you to configure VPC endpoint policies. You can restrict access to the S3 buckets containing your media content only from specific VPCs, adding an extra layer of security.

5. **Logging and Auditing**: You enable access logging for each access point, ensuring that all access to the media files is logged for security and compliance reasons.

6. **Multi-Region Replication**: You use S3 Replication with Access Points to replicate premium content across multiple AWS regions for redundancy and low-latency access. This replication is controlled through access points to ensure consistent access control across regions.

7. **IAM Role Integration**: You associate IAM roles with access points to grant temporary credentials to your application servers, ensuring secure and temporary access to the media files during playback.

8. **Scaling**: As your user base grows, Access Points can handle requests from thousands of clients simultaneously, ensuring that your media streaming service remains responsive and scalable.

In this real-life example, AWS S3 Access Points provide the necessary security, manageability, and scalability to efficiently deliver media content to users while ensuring access control, compliance, and high availability. They simplify the management of access to S3 data and enhance the overall architecture of the media streaming service.
