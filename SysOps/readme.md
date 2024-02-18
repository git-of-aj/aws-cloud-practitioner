# aws cost allocation tags
[user-defined tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html)

# AWS Cloudwatch - repository to store metric data
- [What is It](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
-  An AWS service—such as Amazon EC2—puts metrics into the repository, and you retrieve statistics based on those metrics. If you put your own custom metrics into the repository, you can retrieve statistics on these metrics as well.
- Metrics are stored separately in Region
![](https://docs.aws.amazon.com/images/AmazonCloudWatch/latest/monitoring/images/CW-Overview.png)

### [Cloudwatch Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
1. **Namespace:** A namespace is a container for CloudWatch metrics. Metrics in different namespaces are isolated from each other
2. **Metric:**  A metric represents a time-ordered set of data points
3. [Tutorial](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/gs_monitor_estimated_charges_with_cloudwatch.html)

# [AWS CFT Concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html)
- [basics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html)
- [webserver tutorial](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer-walkthrough-createbasicwebserver.html)
- [Drift Detection in CFT](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html)

# Systems Manager 
- [Ec2 Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html)
- [Private Endpoint with SSM](https://repost.aws/knowledge-center/ec2-systems-manager-vpc-endpoints)
- [Private Endpoint Demo](https://repost.aws/knowledge-center/vpc-fix-gateway-or-interface-endpoint)
- [entra sso](https://learn.microsoft.com/en-us/entra/identity/saas-apps/aws-single-sign-on-tutorial)

# AWS Config
- [Preventive creation of non compliant aws resources](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-proactive-rules-and-aws-cloudformation-hooks-to-prevent-creation-of-non-complaint-cloud-resources/)
- [aws config - what it records](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html)
- config rules = s3-bucket-public-read-prohibited and vpc-sg-open-only-to-authorized-port

# AWS GuardDuty
[get Started](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html#startup-samples)

# AWS instance connect
- [basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-ec2-instance-connect-endpoint.html)
