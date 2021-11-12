+++
title = "Automate management for deployments"
chapter = true
weight = 35
+++

Scenario 2

The Ask

Cloud usage within Example Corp has picked up significantly as Example Corp continues to accelerate the migration and modernization of their applications. A number of teams  are now using Amazon Elastic Container Service (Amazon ECS) in innovative ways. However, Example Corp has noticed that development teams are challenged with provisioning the infrastructure components and resources are created in different ways. This is leading to increased infrastructure management and a lack of consistent standards and best practices, resulting in slower time-to-market application innovation. Example corp is on a mission to modernize their infrastructure team to give developers an easy way to deploy their code using containers and serverless technologies, leveraging the management tools, governance, and visibility needed to provide consistent standards and best practices.

To help the customer, we will design and then deploy container services using management tools and promote best practices for their development tools.

The Task

We are going to create and deploy a governance model using AWS Proton to ensure greater visibility into the infrastructure resources, provide consistent standards, best practices, and automation using CI/CD pipeline. Using the new CI/CD pipeline, we’re going to push new code, build, and deploy the application to ECS.

You can follow those steps to do this:

* Create Proton templates that describe infrastructure resources
* Deploy container application onto ECS
* Use CI/CD pipeline to deploy new application version
