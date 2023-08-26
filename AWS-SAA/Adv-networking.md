## VPC Peering
WHat is ? - https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html
demo - https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html

The following diagram is an example of one VPC peered to two different VPCs. There are two VPC peering connections: VPC A is peered with both VPC B and VPC C. VPC B and VPC C are not peered, and you cannot use VPC A as a transit point for peering between VPC B and VPC C. If you want to enable routing of traffic between VPC B and VPC C, you must create a unique VPC peering connection between them.
![image](https://github.com/Ananyojha/aws-cloud-practitioner/assets/76782360/ea9a2401-7732-40a8-8933-49fd90300b5f)


## VPC Endpoints 
docs - https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html
`PROBLEM`: Ec2 in Private Subnet => s3 => Ec2 => NAT Gateway (Public subnet) => Internet (🥲)
1. --Explain AWS Backbone Network--
2. Communicate using AWS Backbone Newtork (1 endpoint == 1 aws service) 
3.  Amazon VPC instances do not require public IP addresses to communicate with resources of the service. Traffic between an Amazon VPC and a service does not leave the Amazon network
`Types`;
1. An interface endpoint is a collection of one or more elastic network interfaces with a private IP address that serves as an entry point for traffic destined to a supported service.
   - uses AWS PRivate Link service
2. Gateway Endpoint: Gateway VPC endpoints provide reliable connectivity to Amazon S3 and DynamoDB without requiring an internet gateway or a NAT device for your VPC
   ![image](https://github.com/Ananyojha/aws-cloud-practitioner/assets/76782360/1fc1ce50-b3da-4d7a-af94-9968012ed6f2)
When you create a gateway endpoint, you select the VPC route tables for the subnets that you enable. The following route is automatically added to each route table that you select. The destination is a prefix list for the service owned by AWS and the target is the gateway endpoint.

|Destination|	Target|
-----------------------------------------
|prefix_list_id	| gateway_endpoint_id|

