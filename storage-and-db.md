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

- `instance store only with large instances like c or above not in t family`

## s3
think storage class like cupborad (ka-bird)

S3 Standard: This is like the top shelf of your closet where you store items that you need to access frequently. It's easy to reach and you can quickly grab what you need.

S3 Intelligent-Tiering: This is like the middle section of your closet where you store items that you use occasionally, but not as often as the top shelf items. The items are automatically moved to the appropriate shelf based on their usage.

S3 Standard-Infrequent Access: This is like the bottom shelf of your closet where you store items that you don't need to access as often, but you still want to keep them within reach.

S3 One Zone-Infrequent Access: This is like a storage bin or container outside of your closet that you can access when you need to, but it's not as easily accessible as the items in your closet.

S3 Glacier: This is like a storage unit that you rent to store items that you don't need to access often but want to keep for a long time. It's not easily accessible, and you need to plan ahead to retrieve items.

S3 Glacier Deep Archive: This is like a storage unit in a remote location that you use to store items that you may never need to access again. It's the furthest away from your closet and takes the longest time to retrieve items.

## file storage 
- An Amazon EFS file system can have mount targets in only one VPC at a time.
- NFS: You can access your Amazon EFS file system concurrently from multiple NFS clients, so applications that scale beyond a single connection can access a file system.
- You can mount your Amazon EFS file systems on your on-premises data center servers when connected to your Amazon VPC with AWS Direct Connect or AWS VPN You can mount your EFS file systems on on-premises servers to migrate datasets to EFS, enable cloud bursting scenarios, or back up your on-premises data to Amazon EFS.
> if you need to support Linux file systems or require general-purpose file storage, EFS may be the better choice. However, if you require high-performance file storage for Windows workloads or advanced features such as support for SMB protocol, multi-AZ deployment, and data deduplication, FSx may be the better choice.

```sh
# install nfs client package 
#below is for amazon linux -2
sudo yum install -y nfs-utils

# create a dir 
sudo mkdir /mnt/efs

# mount 
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 <EFS_DNS_NAME>:/ /mnt/efs

# verify
df -h
```

## Databases

## Relational Databases uses:
1. CRM 
2. HR system
3. financial data, such as transactions, budgets, and forecasting, providing insights into the financial health of an organization.

## Non-Realtional Databases aka NoSQL
 non-relational databases are well-suited for use cases that involve handling large amounts of unstructured or semi-structured data, and require high scalability and flexibility. Some examples of use cases for non-relational databases include e-commerce sites, social media platforms, real-time analytics, and IoT applications.
 [aws docs - types of nosql DB](https://aws.amazon.com/nosql/)

## RDS
- Backups,scaling, DR all configured by aws
- popular db engines are supported - maria-db, mysql, postgreSQL
- you can't ssh into it !!!!!
- 
### Basics

|| ---> Amazon EBS provides durable, block-level storage volumes that you can attach to a running instance.
==============================================================================
DB instance class determines the computation and memory capacity of a DB instance
======================================================
DB engine like MSSQL,SQL,MqriaDb
========================================================
DB instance can contain one or more user-created databases.
=========================================================


> A burstable instance class, also known as a T-class instance, is designed for workloads that do not require sustained high CPU performance but may occasionally require more CPU resources than allocated. With burstable instances, you accrue CPU credits when your workload is utilizing less than the baseline level of CPU performance, and can use these credits to burst beyond the baseline level when needed.
-----------------------------------------------------------------------------------------------------
Burstable instances are ideal for workloads with unpredictable traffic patterns or intermittent high CPU usage, such as development and testing environments, low traffic web applications, and small databases. They are cost-effective because you only pay for the CPU usage you actually consume, rather than for a high-performance instance that you might not fully utilize.

## AWS Aurora
- optimised to run in cloud hence faster 
- create `read only replica of db` ----> reduce IOPS -----> increase performance [how to create read only copy after creating DB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create)
- Aurora stores copies of the data in a DB cluster across multiple Availability Zones in a single AWS Region
- written to the primary DB instance, Aurora synchronously replicates the data across Availability Zones to six storage nodes associated with your cluster volume.
- [create aurora global replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html)

## once backup done --> create snapshot --> restore snapshot --> copy snapshot to other region --> transfer to other account -> restore that

## DynamoDB for key value store
- A Ecommerce site or library find using attribute -> bettr performance + faster

## Elasticache
 -• ElastiCache is to get managed Redis or Memcached
• Caches are in-memory databases with high performance, low latency
• Helps reduce load off databases for read intensive workload

## redshift
Redshift is based on PostgreSQL, but it’s not used for OLTP
• It’s OLAP – online analytical processing (analytics and data warehousing)
• Load data once every hour, not every second
• 10x better performance than other data warehouses, scale to PBs of data
• Columnar storage of data (instead of row based)
• Massively Parallel Query Execution (MPP), highly available
• Pay as you go based on the instances provisioned
• Has a SQL interface for performing the queries
• BI tools such as AWS Quicksight or Tableau integrate with i

