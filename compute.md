Barista == who makes coffee

## On-prem 
When you buy an on-premises server, you get CPU, memory, storage, and IOPS, all bundled together. With Amazon EC2, these are split apart so that you can scale them independently. If you need more CPU, less IOPS, or more storage, you can easily allocate them.

## Ec2
- on demand scalable computing capacity (virtual servers)
- get cpu,gpu,os,disk of your choice --> use it --> delete it 
- [aws docs - ec2 and dependencies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

## ec2 instance types
Imagine you're building a pizza. The size of the pizza is the instance type, and the toppings are the resources available with that instance type.

General Purpose Instances - These instances are like a basic cheese pizza. They provide a balance of compute, memory, and networking resources, suitable for a wide range of applications.

Compute Optimized Instances - These instances are like a meat lover's pizza. They offer a high-performance CPU for applications that require significant computational power, like scientific computing or batch processing.

Memory Optimized Instances - These instances are like a supreme pizza with extra cheese. They provide more memory than other instances, making them ideal for memory-intensive workloads like large-scale databases or analytics.

Storage Optimized Instances - These instances are like a pizza with lots of toppings. They come with high disk I/O (input/output) and large storage capacity, making them suitable for applications that require a lot of data processing, like data warehousing or big data analytics.

GPU Instances - These instances are like a customized pizza with unique toppings. They come with powerful graphics processing units (GPUs), ideal for applications that require intense graphical processing, such as 3D modeling, rendering, or machine learning.

## AWS Reserved instance vs Compute saving plan
- `reserved`: say to aws in this particular region,this size, os 
-  Booking a Reserved Instance is like renting a specific property for a certain period. You are guaranteed that specific property, and you will pay a discounted rate for that rental

`computing saving plan`: offer flexibility by providing a discount on your compute usage, regardless of instance family, size, AZ, or region. You commit to a specific dollar amount per hour of usage, and AWS provides a discount on all eligible usage, up to the amount you've committed to. CSPs are best suited for workloads that are more flexible in terms of instance type and usage patterns.
- give upper bound $$$

## aws dedicated vs instances vs hosts
[link to blog of dedicated instance vs dedicated host](https://www.trek10.com/blog/dedicated-hosts-and-dedicated-instances)
1. `aws dedicated instances`: 
2. `aws dedicated host`:
AWS Dedicated Hosts, on the other hand, provide you with a physical server that is dedicated to your account, and you have full control over the underlying hardware. You can choose the number of sockets, the number of cores, and the amount of memory you need for your workloads. This level of control allows you to bring your own licenses or software that require specific hardware configurations. AWS Dedicated Hosts provide the highest level of isolation and control available on AWS.
**Launch ec2 from launch Template:**
- ![](https://docs.aws.amazon.com/images/AWSEC2/latest/UserGuide/images/launch-template-diagram.png)
- **Spot instances vs On-demand**
- here are key differences between Spot Instances and On-Demand Instances:

1. The price for Spot Instances varies based on demand

2. Amazon EC2 can terminate an individual Spot Instance as the availability of, or price for, Spot Instances changes
3. [ec2 saving plans](https://aws.amazon.com/savingsplans/compute-pricing/)

> AWS Dedicated Hosts are dedicated physical servers within the AWS cloud infrastructure, while AWS Outposts are fully managed computing and storage racks located on-premises. 

## AWS Placemement group => https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html

## AMI
> (AMI) from an EC2 instance, it includes the attached Elastic Block Store (EBS) volumes by default. This means that the data stored on the EBS volumes will be included in the AMI, allowing you to launch new instances with the same data and configuration as the original instance.

However, it's important to note that the EBS volumes must be in a consistent state before you create the AMI. You can either shut down the instance before creating the AMI or use the built-in Amazon EC2 tools to freeze the file system and ensure data consistency during the AMI creation process.

## Instance store 
- Physical storage physically atttached to ec2 hardware
- available only in big instances like in `i` or `c` series

## ASG
[aws docs - what when how asg](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

![](https://docs.aws.amazon.com/images/autoscaling/ec2/userguide/images/as-basic-diagram.png)
- [predictive scaling:](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) Proactive approach: needs atleast past 24 hour cloudwatch data to identify traffic pattern --> forcast only mode -> test & deploy
- in scaling policy --> in aws console ---> Target Tracking Policy
- dynamic scaling: reactive approach

-The instance scale-in protection setting controls whether the Auto Scaling group can terminate a particular instance when scaling in. 

## ELB
1. ELB is the umbrella term for the load balancer service, which provides both Application Load Balancers (ALB) and Network Load Balancers (NLB). ELB also provides a third type of load balancer, called Classic Load Balancer, which is the original type of load balancer in AWS and supports both HTTP and HTTPS traffic.

2.ALB is designed to provide Layer 7 (application layer) load balancing and supports HTTP and HTTPS traffic. It can route traffic based on content-based routing rules, such as path-based routing and host-based routing. ALB also supports advanced features such as sticky sessions, SSL/TLS termination, and authentication.

3. NLB, on the other hand, is designed to provide Layer 4 (transport layer) load balancing and supports TCP, UDP, and other protocols. It can handle a much larger volume of traffic than ALB and has lower latencies. NLB also supports advanced features such as source IP-based routing, cross-zone load balancing, and SSL/TLS passthrough.
# microservices why ?
Now, in a monolith, it is common to have some components that do more work (receive and process user requests) than others. For example, in our case, not every user who logs in or signs up would make an order or pay for an order.
- https://www.freecodecamp.org/news/message-queues-in-distributed-systesms/#:~:text=Some%20examples%20of%20message%20queues,a%20microservice%20to%20communicate%20asynchronously.
## Messaging service
[what is pub/sub -> aws docs](https://aws.amazon.com/pub-sub-messaging/)
- Like a youtube channel bell icon 
- Publisher -> Youtube content creator
- central msg broker (youtube channel) --> recives the content -> alert to all subscribers.
- same for any Publish-Subscribe (Pub/Sub) is a messaging pattern where senders, known as publishers, send messages to a central message broker, known as a topic or channel. Subscribers then register to receive messages from that topic or channel.
- example Apache Kafka, RabbitMQ, SNS
- **Benefits**
1.  Pub/Sub pattern enables asynchronous communication between decoupled components or services, where senders and receivers don't have to know about each other. 
2.   commonly used in modern distributed systems architecture, where components can be added, removed or scaled dynamically
[SNS:](https://aws.amazon.com/sns/)

1. sns use 1
![](https://d1.awsstatic.com/Product-Page-Diagram_Amazon-SNS_Event-Driven-SNS-Compute%402x.03cb54865e1c586c26ee73f9dff0dc079125e9dc.png)

2. sns send msg to customers and app push notifications
![](https://d1.awsstatic.com/Product-Page-Diagram_Amazon-SNS-Mobile-Push%402x.08ac920f6c0bcf10c713be9e423b13e6fd9bd50c.png)

## SQS
> Send notification back and forth to app component. in serial wise order ----> 1 come 1 served aka (FIFO) ==> first in first out
- biding service --> bids place --> wait 
- Example: in Ecommerce Webiste ===> when a customer places an order, the order information is sent to an SQS queue. The order processing service retrieves the order information from the queue and processes the order.

## SNS Vs SQS
both are siblings
SNS --> arrogant ||||||| SQS --> patient
- SNS aya gya ||| SQS aaya --> busy --> wait kia  

> Container orchestration is the process of managing and deploying containerized applications across a cluster of servers. These services typically include features such as automated deployment, load balancing, scaling, monitoring, and logging, which simplify the process of managing containers and help to ensure that applications are always available and performing at their best. Some popular container orchestration services include Kubernetes, Docker Swarm, and Amazon ECS.


## container in aws
- ECS: Run docker containers over Ec2 (if you have permanent use patterns, need full control over security, networking, patching etc) 
- or
- fargate: complete abstraction from infra. serverless container orchestration service

2. EKS: managed k8 service




--------------------------------------------------------------------------------------

## ECS Components:
Task Definition: A task definition is like a blueprint for your application. It specifies the Docker container image to use, the resources to allocate to the container, and other settings such as networking, logging, and environment variables.

Container Instance: A container instance is a server that runs the Docker daemon and can run one or more containers. It can be an EC2 instance or a Fargate instance, which is a serverless option for running containers.

Cluster: A cluster is a logical grouping of container instances that you can manage as a single entity. A cluster can contain one or more container instances.

Service: A service is a group of tasks that are run together and managed by ECS. A service can be configured to automatically start or stop tasks, maintain a desired number of running tasks, and optionally load balance traffic across them.

Task: A task is a running instance of a task definition. It can run one or more containers that are specified in the task definition. A task runs on a container instance in a cluster.

Container: A container is a lightweight and portable executable package that contains all the necessary code, libraries, and dependencies to run an application. It runs within a Docker engine and can be managed by ECS.





