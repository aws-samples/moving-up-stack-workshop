import * as cdk from '@aws-cdk/core';
import * as iam from '@aws-cdk/aws-iam'
import * as s3 from '@aws-cdk/aws-s3'
import * as cloudfront from '@aws-cdk/aws-cloudfront'

export class cloudfrontS3 extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const s3bucket = s3.Bucket.fromBucketArn(this,'S3CFServiceDeploymentBucket','arn:aws:s3:::s3cloudfronttest-s3bucket-3ut3w087h9b8')
    var cloudfrontDistro = cloudfront.Distribution.fromDistributionAttributes(this,'S3CFServiceDeploymentCFDistribution',{
      distributionId: "E24KFU32MLOFQS",
      domainName: "d22fjh6gw4b6fp.cloudfront.net"
    })


      new cdk.CfnOutput(this,'PipelineEndpoint',{
        value: "https://${AWS::Region}.console.aws.amazon.com/codesuite/codepipeline/pipelines/${Pipeline}/view?region=${AWS::Region}",
        description: "The URL to access the pipeline"
      })

    }
  }

