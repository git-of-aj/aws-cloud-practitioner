[Purpose Build databases - All databases Types in AWS](https://aws.amazon.com/products/databases/#Databaseservices)
HVAC - Heating, Ventilation AIr conditioning
Rack and stack - Placing hardware into datacenter
Patches - Software and OS Updates taht adresses a security Vulnerability

- Amazon Aurora: With Amazon Aurora, you need to provision a specific instance size (e.g., db.r5.large) for your Aurora cluster. You have control over the compute and storage capacity, and you can scale up or down manually based on your workload requirements.
- While serverless all auto

  ### DynamoDB
[good demo on SQL Vs DynanoDb](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.CreateTable.html)
  [aws docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

**DAX: **
- Amazon DynamoDB is designed for scale and performance. In most cases, the DynamoDB response times can be measured in single-digit milliseconds. However, there are certain use cases that require response times in microseconds. For these use cases, DynamoDB Accelerator (DAX) delivers fast response times for accessing eventually consistent data.
- Still Use DAX for In memory Caching - [AWS docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) 
