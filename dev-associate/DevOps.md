what is Devops - https://aws.amazon.com/devops/what-is-devops/
1. codecommit - VCS
2. codebuild - build pipeline 
3. code pipeline - Release pipeline
4. code catalysts - unifies software dev
-------------------------------------------------------
## CodeCommit 
### Basics
without permissions - codecommit poweruser {simple user} and codecommit {full access}
- git clone url 
- asks for username and password 
- no policy then =>  The requested URL returned error: 403

[Hands on all features of code commmit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-cc.html)

without git config username git commit gives error : unknown users - who you are?
### Merge Types:
1. Fast forward merge
`git merge --ff-only`
Merges the branches and moves the destination branch pointer to the tip of the source branch. This is the default merge strategy in Git
2. Sqaush and Merge
`git merge --squash`
Combines all commits from the source branch into a single merge commit in the destination branch.
3. 3-way merge
`git merge --no-ff`
Creates a merge commit and adds individual source commits to the destination branch.
------------------------------------------------------------------------------
## CodeDeploy
you create the Amazon EC2 instance where you deploy a sample application. As part of this process, create an instance role that allows install and management of the CodeDeploy agent on the instance. The CodeDeploy agent is a software package that enables an instance to be used in CodeDeploy deployments. You also attach policies that allow the instance to fetch files that the CodeDeploy agent uses to deploy your application and to allow the instance to be managed by SSM.
[complete AWS CI - CD using Code Commit + Code Pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-codecommit.html)
