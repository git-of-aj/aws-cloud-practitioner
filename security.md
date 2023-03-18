## IAM
- Root User = first acount + Full acess + responsible to onboard new users
[Root Users - actions that only he can perform..](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html)

*Types of Uses for IAM*:
1. Service Admin: I work with only RDS / DynamoDB / Redshift / atena - I am a DBA
2. I am the developer Manager - so I decide who, uses which services
3. IAM admin: his work only to grant take away permisssions.

## AWS users group only alllows to add users not group nesting

## IAM Role
- An IAM role is an identity within your AWS account that has specific permissions. It is similar to an IAM user, but is not associated with a specific person.
- Assume (temporarily) the permissions --> Console by switching roles. You can assume a role by calling an AWS CLI or AWS API operation or by using a custom URL


## IAM Permissions
- users -> permissions --> Inline policy : Permissions directly attached to the user not via a group,
- `inline policy`: added to that specific group,user only
- `managed policy`: create this policy --> reuse it --> add it to anywhere

## IAM Security
- `IAM --> left side --> credential report` --> when signed in --> when password change 
- `IAM --> user --> access advisor` --> see list of allowed services to the user --> when the users last accesed that service


