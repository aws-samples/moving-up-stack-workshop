import re
import boto3



def getEnvironmentOutputs(serviceName):

    proton = boto3.client('proton')
    taggingAPI =boto3.client('resourcegroupstaggingapi')
    cf = boto3.client('cloudformation')

    # Start with getting service details
    # We do this to find the environment Name
    serviceResponse = proton.get_service(
        name=serviceName
    )
    
    # Need to parse out the environment name from the spec
    environmentName = re.search(r"(environment\: )(\S+)",serviceResponse['service']['spec']).group(2)
    environmentResponse = proton.get_environment(
        name=environmentName
    )
    environmentNameArn = environmentResponse['environment']['arn']

    # Use the ARN to get the tags
    resourceTagResponse = proton.list_tags_for_resource(
        resourceArn=environmentNameArn
    )

    
    outputItems = list(())
    for key in resourceTagResponse['tags']:
        if(key['key'] == 'aws:proton:environment'):

            protonEnvironment = key['value']
            outputItems.append({
                'OutputKey': 'ProtonEnvironment', 
                'OutputValue': key['value'], 
                'Description': 'Proton Environment Name'
            })    
        
        if(key['key'] == 'aws:proton:template'):
            protonTemplate = key['value']
            outputItems.append({
                'OutputKey': 'ProtonTemplate', 
                'OutputValue': key['value'], 
                'Description': 'Proton Template Name'
            })    

    # Once we have the tags, we can query for the CF stack for the outputs
    tagginAPIresponse = taggingAPI.get_resources(
        TagFilters=[
            {
            'Key': 'proton:environment',
            'Values': [protonEnvironment]
            },
                        {
            'Key': 'proton:template',
            'Values': [protonTemplate]
            }
        ],
        ResourceTypeFilters=[
            'cloudformation:stack'
        ]
    )

    cloudfromationARN = tagginAPIresponse['ResourceTagMappingList'][0]['ResourceARN']

    cfresponse = cf.describe_stacks(
        StackName=cloudfromationARN
    )

    for output in cfresponse['Stacks'][0]['Outputs']:
        outputItems.append(output)

    return outputItems
    
getEnvironmentOutputs('my-s3-dev-service')

