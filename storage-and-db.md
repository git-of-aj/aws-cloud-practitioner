## block storage 
[aws instance store - aws docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
1. instance store: An instance store provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host computer.
-  ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content, or for data that is replicated across a fleet of instances
![](https://docs.aws.amazon.com/images/AWSEC2/latest/UserGuide/images/instance_storage.png)
- can't detach an instance store volume from one instance 
- If an instance reboots (intentionally or unintentionally), data in the instance store persists. However, data in the instance store is lost under any of the following circumstances:

The underlying disk drive fails

The instance stops

The instance hibernates

The instance terminates

Therefore, do not rely on instance store for valuable, long-term data. Instead, use more durable data storage, such as Amazon S3, Amazon EBS, or Amazon EFS
