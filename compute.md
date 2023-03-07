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
