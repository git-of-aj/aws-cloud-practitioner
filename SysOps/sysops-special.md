# IAM 
- federated users
- Rotate old access keys using aws config (Azure Policy):https://docs.aws.amazon.com/config/latest/developerguide/1-click-setup.html + https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
- AWS Credential Report: You can download a credential report that lists all users in your account and the status of their various credentials, including passwords, access keys, and MFA devices. You can generate a credential report from the AWS Management Console, the AWS SDKs and command line tools, or the IAM API.: DEMO: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html#getting-credential-reports-console
- Permission boundary
## networking 
- peering: https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html
- trnsit gateway: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html
- Privatelink and vpc endpoints: use case example = https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/use-case-examples.html
- demo: https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html
- Cloudfront , WAF, Sheild, ACM
## OPerations 
1. ✅✅ [part of aws system manager] => AWS Sessions Manager (Azure Bastion):Provides secure access to your EC2 instances over SSH or RDP without having to open ports in your firewall
2. why use it - https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
3. aws service catalog - azure blueprints : https://docs.aws.amazon.com/servicecatalog/latest/adminguide/autotags.html
4. demo: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-keypair.html
5. aws control tower
6. ELB & More on Route 53:
routing policy: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

## Mod-3: Interactions with AWS
- CLI, Powershell, console, cloudshell
- Boto3
- Cloudformation template basics: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html

## Mod-4: Storage 
s3 presigned url - https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html
s3 block public access at account level & bucket level
s3 object versioning: https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html
s3 object locks: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-console.html
retrieving archived objects
EBS Multi attach: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html
create ebs snaphot

## AWS Cloudfront
- Docs: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- demo: Create a public s3 bucket => https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStartedCreateBucket.html
## MOd-5: Backup and Monitoring
- **Cloudtrail**: As a best practice, create a trail that applies to all AWS Regions. This is the default setting when you create a trail in the CloudTrail console. When a trail applies to all Regions, CloudTrail delivers log files from all Regions in the AWS partition in which you are working to an S3 bucket that you specify. After you create the trail, AWS CloudTrail automatically starts logging the events that you specified.
use aws backup service for auto ebs backup: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
Cloudwatch
Xray
VPC flow logs
