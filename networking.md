## Computer Network
group of devices that speak a common language (protocol) like My laptop (broswer) -> HTTPS -> Web server (waiting for a Https Request) --> they found each other via internet(a big network)..
- [TCP-IP network model](https://www.geeksforgeeks.org/tcp-ip-model/)

## working of TCP-IP
> how machines find each other?
NIC Card --> SIM card --> 
1. MAC address
2. IP address

## DHCP Server
the DHCP server assigns a unique IP address to each NIC card in the network. 
In windows:
- Get Ip of Server by: ```ipconfig /all``` 
- Get MAC Address by ```arp -a``` 

## CIDR

## extended network
connect 2 different network together. In this case, make internet know about your private machine.

## VPC

* IPAM pool: 
create a big pool of ip addess => create vpc in different region / m here
![](https://docs.aws.amazon.com/images/vpc/latest/ipam/images/ipam-example-1-570px.png)

## internet gateway
1 vpc : 1 internet gateway
- there is no additional charge for an IGW itself. However, data transfer fees apply for traffic that flows through the IGW. Outbound data transfer from an EC2 instance in a VPC to the internet is charged based on the data transfer out pricing tier. Inbound data transfer from the internet to an EC2 instance in a VPC is free.

You can find more information on AWS data transfer pricing here: https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_Pricing

## public / private subnet (theoritical)
- If a subnet is `associated with a route table that has a route to an internet gateway`, it's known as a `public subnet`. If a subnet is associated with a route table that does not have a route to an internet gateway, it's known as a private subnet.

## transit gateway vs internet gateway
Transit Gateway is used for interconnecting multiple VPCs and on-premises networks, while Internet Gateway is used to provide internet connectivity to a single VPC.

It's worth noting that TGW also supports VPN and Direct Connect connections to on-premises networks, while IGW only provides internet connectivity. Additionally, TGW is priced per-hour and per-GB data processing charges, while there is no additional charge for IGW itself, but data transfer fees apply for traffic that flows through it.
