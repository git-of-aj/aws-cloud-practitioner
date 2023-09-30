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
4. aws control tower
5. ELB & More on Route 53
