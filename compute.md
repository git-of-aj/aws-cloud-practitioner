Barista == who makes coffee

## Ec2
- on demand scalable computing capacity (virtual servers)
- get cpu,gpu,os,disk of your choice --> use it --> delete it 
- [aws docs - ec2 and dependencies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- 
**Launch ec2 from launch Template:**
- ![](https://docs.aws.amazon.com/images/AWSEC2/latest/UserGuide/images/launch-template-diagram.png)
- **Spot instances vs On-demand**
- here are key differences between Spot Instances and On-Demand Instances:

1. The price for Spot Instances varies based on demand

2. Amazon EC2 can terminate an individual Spot Instance as the availability of, or price for, Spot Instances changes
3. [ec2 saving plans](https://aws.amazon.com/savingsplans/compute-pricing/)

## ASG
[aws docs - what when how asg](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

![](https://docs.aws.amazon.com/images/autoscaling/ec2/userguide/images/as-basic-diagram.png)
- [predictive scaling:](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) Proactive approach: needs atleast past 24 hour cloudwatch data to identify traffic pattern --> forcast only mode -> test & deploy
- dynamic scaling: reactive approach

-The instance scale-in protection setting controls whether the Auto Scaling group can terminate a particular instance when scaling in. 

## ELB
1. ELB is the umbrella term for the load balancer service, which provides both Application Load Balancers (ALB) and Network Load Balancers (NLB). ELB also provides a third type of load balancer, called Classic Load Balancer, which is the original type of load balancer in AWS and supports both HTTP and HTTPS traffic.

2.ALB is designed to provide Layer 7 (application layer) load balancing and supports HTTP and HTTPS traffic. It can route traffic based on content-based routing rules, such as path-based routing and host-based routing. ALB also supports advanced features such as sticky sessions, SSL/TLS termination, and authentication.

3. NLB, on the other hand, is designed to provide Layer 4 (transport layer) load balancing and supports TCP, UDP, and other protocols. It can handle a much larger volume of traffic than ALB and has lower latencies. NLB also supports advanced features such as source IP-based routing, cross-zone load balancing, and SSL/TLS passthrough.

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





