+++
title = "Create Proton Environment"
weight = 10
+++

---

## What are we going to do?
In this section we will provision the environment for our microservices.
This environment will include a VPC with public and private subnets, an ECS Cluster, and the shared Application Load Balancer.

## Step by step guide


With the registered and published environment template, you can now create a Proton environment from the template.

Open the [Proton Console](https://console.aws.amazon.com/proton/home#/environments).
Click on ```Create environment```

Choose the ```Fargate Public and Private VPC``` template we created in the previous step and then click ```Configure```.

![ProtonEnvironmentTemplate](images/10_environment-template.png)

On the ```Configure Environment``` screen.
 - Give the environment a name of ```MyFargateEnvironment```.
 - Under environment roles, choose existing service role and select ```ProtonServiceRole```

Then click the ```Next``` button.

![ConfigureEnvironment](images/10_configure-environment.png)

Leave on the defaults on the ```configure custom settings``` screen and click ```Next```.

![CustomEnvironment](images/10_environment_custom.png)

Finally on the ```Review``` screen, click ```Create```.
Wait a few minutes for your environment to be created.

{{% notice tip %}}
***What did we just do?***
We just used our Proton environment template to create an environment.
{{% /notice %}}
