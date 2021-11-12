from __future__ import print_function
import logging as log
import urllib3
import json
import boto3

log.getLogger().setLevel(log.INFO)

SUCCESS = "SUCCESS"
FAILED = "FAILED"

http = urllib3.PoolManager()


def get_environment_outputs(serviceName):

    proton = boto3.client('proton')
    taggingAPI = boto3.client('resourcegroupstaggingapi')
    cf = boto3.client('cloudformation')

    # Start with getting service details
    # We do this to find the environment Name
    serviceResponse = proton.get_service(
        name=serviceName
    )

    # Need to parse out the environment name from the spec
    environmentName = re.search(
        r"(environment\: )(\S+)", serviceResponse['service']['spec']).group(2)
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
            })

        if(key['key'] == 'aws:proton:template'):
            protonTemplate = key['value']
            outputItems.append({
                'OutputKey': 'ProtonTemplate',
                'OutputValue': key['value'],
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
        outputItems.append({
          'OutputKey': output['OutputKey'],
          'OutputValue': output['OutputValue'],
        })

    return outputItems


def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False, reason=None):
    responseUrl = event['ResponseURL']

    print(responseUrl)

    responseBody = {
        'Status': responseStatus,
        'Reason': reason or "See the details in CloudWatch Log Stream: {}".format(context.log_stream_name),
        'PhysicalResourceId': physicalResourceId or context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'NoEcho': noEcho,
        'Data': responseData
    }

    json_responseBody = json.dumps(responseBody)

    print("Response body:")
    print(json_responseBody)

    headers = {
        'content-type': '',
        'content-length': str(len(json_responseBody))
    }

    try:
        response = http.request(
            'PUT', responseUrl, headers=headers, body=json_responseBody)
        print("Status code:", response.status)

    except Exception as e:

        print("send(..) failed executing http.request(..):", e)


def on_event(event, context):
    print(event)
    request_type = event['RequestType']
    if request_type == 'Create':
        return on_create(event)
    if request_type == 'Update':
        return on_update(event)
    if request_type == 'Delete':
        return on_delete(event)
    raise Exception("Invalid request type: %s" % request_type)


def on_create(event):
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)

    environmentData = get_environment_outputs('my-s3-dev-service')
    physical_id = "LambdaProtonEnviromentCustomResource"

    return {'PhysicalResourceId': physical_id}


def on_update(event):
    physical_id = event["PhysicalResourceId"]
    props = event["ResourceProperties"]
    print("update resource %s with props %s" % (physical_id, props))
    # ...


def on_delete(event):
    physical_id = event["PhysicalResourceId"]
    print("delete resource %s" % physical_id)
