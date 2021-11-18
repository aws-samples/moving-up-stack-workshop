+++
title = "Cleanup"
chapter = false
weight = 60
+++

### Cleanup

In this workshop you have learned how to modernize and achieve developer agility using multiple AWS services.

Now you can proceed to cleaning up.

If you completed this workshop at AWS event using an AWS provided account, you do not need to clean-up the CloudFormation resources. The accounts will be terminated at a later time. If you completed the workshop in your own AWS account follow the steps below to cleanup the resources.


### S3 bucket
{{%expand "Click here to expand" %}}

* Navigate to the [Amazon S3 console](https://console.aws.amazon.com/s3/home)
* In the Bucket name list, select the option next to the name of the bucket **decoupletomicroservices-s3bucket-xxxxxxx** that you want to empty, and then choose Empty.
* On the Empty bucket page, confirm that you want to empty the bucket by entering the bucket name into the text field, and then choose Empty.
* Monitor the progress of the bucket emptying process on the Empty bucket: Status page.
{{% /expand%}}

### ECS Service
{{%expand "Click here to expand" %}}
* Navigate to the [Amazon ECS console](https://console.aws.amazon.com/ecs/home?)
* Select the Cluster name **Workshop-MovingUpTheTechStack**
* Under **Tasks** tab, select the relevants task related to the workshop i.e (threads, posts, users) and choose `stop`
* Under **Services** tab select the three microservices individually (threads, posts, users) and choose `Delete`
* In the new window that pops up type `delete me`
{{% /expand%}}

### Application Load Balancer
{{%expand "Click here to expand" %}}
* Navigate to the Listeners tab for the Application-Load-Balancer [EC2 Console](https://console.aws.amazon.com/ec2/v2/home?#LoadBalancers:).
* Choose view/edit rules -> Delete rules -> Select three rules(api/posts, api/threads, api/users) and choose `Delete`
* Navigate to the Application Load Balancer [Traget Groups](https://console.aws.amazon.com/ec2/v2/home?#TargetGroups:).
* Select all three microservices target groups that start with `ecs-Worksh` and choose `Actions` then `Delete`. Choose `Yes, Delete` to successfully delete the target groups.
{{% /expand%}}

### Proton
{{%expand "Click here to expand" %}}
#### Services
* Open the [Proton Console](https://console.aws.amazon.com/proton/home?).
* In the service detail page, choose `Services`.
* In the list of services, choose the name of the service that you want to delete, in this case `api-posts`,`api-users`, `api-threads`.
* In the service detail page, choose `Actions` and then `Delete`.
* A modal prompts you to confirm the delete action.
* Follow the instructions and choose Yes, delete.

#### Environments
* In the AWS Proton console, choose `Environments`.
* In the list of environments, select the radio button to the left of the environment you want to delete.
* Choose `Actions` and then `Delete`.
* A modal prompts you to confirm the delete action. Follow the instructions and choose Yes, delete.

#### Templates
* In the list of (environment or service) templates.
* In the AWS Proton console, choose (Environment or Service) Templates.
* In the list of templates, select the radio button to the left of the template you want to delete.
* You can only delete an entire template if there are no AWS Proton resources deployed to its versions.
* Choose `Actions` and then `Delete` to delete the entire template.
* A modal prompts you to confirm the delete action. Follow the instructions and choose Yes, delete. 
{{% /expand%}}


## CloudFormation
{{%expand "Click here to expand" %}}
* Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home)

* On the Stacks page in the CloudFormation console, select the stack that you want to delete. The stack must be currently running.
* Stacks to delete in the order listed below
    1) DecoupletoMicroservices
    2) Monolith
* In the stack details pane, choose Delete.
* Select Delete stack when prompted.
{{% /expand%}}