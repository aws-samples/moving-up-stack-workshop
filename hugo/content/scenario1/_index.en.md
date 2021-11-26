+++
title = "Modernize from monolith to microservices"
chapter = true
weight = 30
+++

Example corp is on a modernization journey, they are already in AWS cloud using lift and shift migration strategy, the leadership has set a goal for the organization to modernize the applications, infrastructure to quickly release application features and adapt to the customer needs faster then ever and make the most of the existing investments in AWS. The application team wants to modernize their three-tier application to reap the benefits of using the right service for the job. Application owner is expecting cost reduction and shorter time to market to deliver new features.


### The Ask

> Example Corp made the original decision to deploy all components on EC2 hosts. The Web and the Application tier are currently running in containers on top of docker installed on an EC2. The database is a running MySQL, installed directly on an EC2 instance. Example Corp IT has asked you to help deploy their services on modern managed AWS services, choosing to leverage serverless technologies wherever possible.

### The Task

> We are going to decouple the monolith application into micro-services. Each layer of a monolith three- tier web architecture will be moved to a managed service for using right service for the right job of Example corp. We will use Cloudfront for content delivery of static and dynamic assets.

You can follow these steps to do this:

* Deploy Cloudformation template to create the AWS managed service infrastructure. 
* Migrate the web application traffic to micro services.
* Move static assests to Amazon S3 which will act as origin for CloudFront.

{{% notice info %}}
If you need help at any time please raise your hand.
{{% /notice %}}