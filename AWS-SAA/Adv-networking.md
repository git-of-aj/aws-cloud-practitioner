## VPC Endpoints 
docs - https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html
`PROBLEM`: Ec2 in Private Subnet => s3 => Ec2 => NAT Gateway (Public subnet) => Internet (🥲)
1. --Explain AWS Backbone Network--
2. Communicate using AWS Backbone Newtork (1 endpoint == 1 aws service) 
3.  Amazon VPC instances do not require public IP addresses to communicate with resources of the service. Traffic between an Amazon VPC and a service does not leave the Amazon network
