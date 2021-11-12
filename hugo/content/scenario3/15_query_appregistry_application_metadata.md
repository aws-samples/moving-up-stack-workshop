+++
title = "Query AppRegistry application metadata"
weight = 15
+++

#### What are we going to do?

#### We are going to perform the following steps:

* Query AppRegistryApplication metadata to find information cross all resources belonging
to an AppRegistry application

---
 
[Open the AppRegistry console](https://console.aws.amazon.com/servicecatalog/home#applications/) and click at the
`EcsApp` application to see more details. Observe that at this point there are a total of four resources
and also four attribute groups associated with this application.

![env_templates](images/15_appregistry_resources_and_attributes.png?classes=shadow)

Because all the resources and metadata are linked to the application, you can query AppRegistry to find
information cross resources belonging to the application. For instance, if you'd like to find out:

How many resources belong to the application?

```shell
NO_RES=$(aws servicecatalog-appregistry list-associated-resources \
  --application EcsApp \
  --query resources | jq length)
 
echo "Total application resources: ${NO_RES}"
```

What is the cost center for this application?

```shell

attr=$(aws servicecatalog-appregistry list-associated-attribute-groups \
	--application EcsApp \
	--max-results 1 \
	--query 'attributeGroups' \
	--output text)

COST_CENTER=$(aws servicecatalog-appregistry get-attribute-group \
	--attribute-group "${attr}" \
	--query attributes \
	--output text | jq -r .CostCenter)
	
echo "Cost center: ${COST_CENTER}"
```

Find the URL to the architecture reference of each microservice.

```shell
attrGroups=$(aws servicecatalog-appregistry list-associated-attribute-groups \
  --application EcsApp \
  --query 'attributeGroups' \
  --output text)
  
for group in ${attrGroups[*]}
do
	aws servicecatalog-appregistry get-attribute-group \
		--attribute-group "${group}" \
		--query 'attributes' \
		--output text | jq -r 'select(.AppMeta != null).AppMeta.ReferenceArchitecture'
done
```

Try to find the answers to the following queries using AWS command line:

{{% notice tip %}}
See
[servicecatalog-appregistry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/index.html)
CLI docs to find supported commands.
{{% /notice %}}

- How many resources are associated with the `EcsApp` application and what are their resource names?
<!---
# Possible solution. Note: there are multiple ways to solve it. 
```bash
aws servicecatalog-appregistry \
  list-associated-resources \
  --application EcsApp \
  --query 'resources[*].name'
```
-->
- Who is `OnCall` for the `users-api` microservice?
<!---
# Possible solution. Note: there are multiple ways to solve it.
```bash
attrGroups=$(aws servicecatalog-appregistry list-associated-attribute-groups \
  --application EcsApp \
  --query 'attributeGroups' \
  --output text)
  
for group in ${attrGroups[*]}
do
	aws servicecatalog-appregistry get-attribute-group \
		--attribute-group "${group}" \
		--query 'attributes' \
		--output text \
		| jq -r '. 
			| select(.AppMeta)
			| select(.AppMeta.ReferenceArchitecture | contains("users-api"))
			| .OnCall.PrimaryName'
done
```
-->

- Who is the `EscalationVP` for each microservice?
<!---
# Possible solution. Note: there are multiple ways to solve it.
```bash
attrGroups=$(aws servicecatalog-appregistry list-associated-attribute-groups \
  --application EcsApp \
  --query 'attributeGroups' \
  --output text)
  
for group in ${attrGroups[*]}
do
	aws servicecatalog-appregistry get-attribute-group \
		--attribute-group "${group}" \
		--query 'attributes' \
		--output text \
		| jq '. | select(.OnCall)' \
		| jq -r '.OnCall.EscalationVP'
done
```
-->

{{% notice tip %}}
***What did we just do?***
We just used AppRegistry to query the application metadata to understand the context 
of your application and resources across your resources.
{{% /notice %}}
