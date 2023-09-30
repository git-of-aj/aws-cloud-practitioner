**Secure VPC Architecture with Public and Private Subnets**

**Build a secure VPC**

* **Use a separate subnet for each tier of your application (web, application, database).**
* **Place your web app tier in a public subnet so that it can be accessed from the Internet.**
* **Place your application and database tiers in private subnets so that they are isolated from the public Internet.**
* **Use security groups to control inbound and outbound traffic to your EC2 instances.**
* **Use network access control lists (NACLs) to provide additional security at the subnet level.**
* **Use a bastion host to access your EC2 instances in private subnets.**

**Set up VPC peering for inter-VPC communication**

* **Peer two VPCs together to allow resources in each VPC to communicate with each other.**
* **Use route tables to control the traffic flow between the two VPCs.**
* **Use security groups and NACLs to control the inbound and outbound traffic between the two VPCs.**

**Enhance VPC design and connectivity**

* **Use AWS Transit Gateway to connect multiple VPCs and on-premises networks.**
* **Use AWS Global Accelerator to improve the performance and availability of your applications.**
* **Use AWS PrivateLink to provide secure access to AWS services from your VPC.**

**Here is an example of a secure VPC architecture with public and private subnets, VPC peering, and AWS Transit Gateway:**

```
VPC 1 (Web tier)
  |
  |
  +-- Public subnet (10.0.1.0/24)
     |
     |
     +-- Web app EC2 instances

VPC 2 (Application tier)
  |
  |
  +-- Private subnet (10.0.2.0/24)
     |
     |
     +-- Application EC2 instances

VPC 3 (Database tier)
  |
  |
  +-- Private subnet (10.0.3.0/24)
     |
     |
     +-- Database EC2 instances

Transit Gateway
  |
  |
  +-- Peering connection to VPC 1
  |
  |
  +-- Peering connection to VPC 2
  |
  |
  +-- Peering connection to VPC 3

```

**Traffic flow:**

* **Users:** Access the web application by sending HTTP requests to the web app EC2 instances in VPC 1.
* **Web app instances:** Send HTTP requests to the application and database EC2 instances in VPC 2 and VPC 3 through the Transit Gateway.
* **Application and database instances:** Communicate with each other directly.

**Benefits:**

* **Isolating the application and database tiers in private subnets makes them inaccessible from the public Internet.**
* **Using VPC peering to connect the different VPCs allows resources in each VPC to communicate with each other.**
* **Using AWS Transit Gateway to connect the different VPCs provides a central point of management and control for the VPC connectivity.**
* **Using AWS PrivateLink to provide secure access to AWS services from the VPCs allows applications in the VPCs to access AWS services without exposing them to the public Internet.**

By following these best practices, you can create a secure, scalable, and highly available VPC architecture.
