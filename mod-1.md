## WHat is cloud ??
- Less Managemnt
- Global Reach
- Rapid 

> How my company can implement Cloud? ||| Assume I have to Travel from Mumbai to Pune with 10 People....
### [OPtion-1] --> Own Car ===> Private Cloud
- I buy,manage and update Pool of IT Infra used by my Employees
- Either buy car yourself (create DC Yourself) OR Via Nutanix or Openshift (A vendor)

### Slides

### Characteristics of Cloud Computing
- on-demand self service : Help Yourself --> No human intervemntion needeed --> Just you and your cloud provider 
Example: Need a VM of 8 GB with Windows Server 2022 --> you don't configure virtualisation --> install OS 🚫🚫  -> ask it get it
- Broad Network Connection:  cloud services must be available for remote access over the network connection, and you are not expected to walk into a the DC to access it.
It must be available to you over a network using standard mechanisms such as INTERNET using HTTPS 
- Resource Pooling ---> Hardware maintained by cloud provider ---> Customers rent accordingly
- Rapid Elasticity -->  customer of cloud services must be allowed to increase or decrease the capabilities in any quantity and at any time.
- Measured Service -> This feature means that the cloud services and resource usage are allowed to Mesa monitor, report, and control transparently to the customers.

### Cloud Service Model
1. IaaS: (got fully furnished kitchen --> Cook Food) ====> Physical Hardware maintained by cloud provider --> you build things 
2. PaaS: (Order food online) -> Baisc Infra (food) managed by the cloud provider -----> washing dishes sending invitations to guest your responsibility
3. SaaS: (go to restaurent) : EVrything fixed (menu price services) ---> use it pay for it --> M365, Gmail every fetures predecided  --> just use it

[SPOILER ALERT!] Where and How Saas Used?
AWS marketPlace: https://aws.amazon.com/marketplace OR  in console search AWS MarketPlace ------> Subscribe 
- get ready to deploy services (SaaS,free, paid)
- assume it lioke Gooogle Play Store / Apple I-store

# AWS Global Infra
1. AWS Region : AWS Region is a physical location in the world ====> Asia Pacific {Geography} (Mumbai) ===> ap-south-1
* Console top right shows Resources from that region (VPC,EC2 etc)
* Contains 1+ AZ
2. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities
3. [show in AWS console go to Oregon](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html#getting-started-find-local-zone)
4. Local Zone: like Oregon (us-west-2) --> Los Angeles is a few 100 miles away from the Northern California region. But Los Angeles local Zone is connected to the California region. due to very high traffic 
5. Wavelength: AWS Wavelength embeds AWS compute and storage services within 5G networks, providing mobile edge computing infrastructure for developing, deploying, and scaling ultra-low-latency applications
6. Edge Network locations :Networking services Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 sit at AWS’ global edge locations connected by dedicated 100Gbps redundant fiber to deliver data with single digit millisecond AWS network latency.
7. aws outposts = Azure stack = search in portal about outposts

## Demonstration:
1. AWS Service Categories: Services -----> See list
2. Creating AWS account -> AWS Free tier
3. create IAM user for New account -> create a aws service
4. aws pricing calculator
