import * as cdk from '@aws-cdk/core';
import * as codebuild from '@aws-cdk/aws-codebuild';
import * as codepipeline from '@aws-cdk/aws-codepipeline';
import * as codepipeline_actions from '@aws-cdk/aws-codepipeline-actions';
import * as iam from '@aws-cdk/aws-iam'
import * as s3 from '@aws-cdk/aws-s3'
import * as cloudfront from '@aws-cdk/aws-cloudfront'

export class pipeline extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);




    const s3bucket = s3.Bucket.fromBucketArn(this, 'S3CFServiceDeploymentBucket', 'arn:aws:s3:::s3cloudfronttest-s3bucket-3ut3w087h9b8')
    const cloudfrontDistro = cloudfront.Distribution.fromDistributionAttributes(this, 'S3CFServiceDeploymentCFDistribution', {
      distributionId: "E24KFU32MLOFQS",
      domainName: "d22fjh6gw4b6fp.cloudfront.net"
    })


    const S3CFServiceBuild = new codebuild.PipelineProject(this, 'S3CFServiceBuild', {
      projectName: "S3CFService_Workshop",
      buildSpec: codebuild.BuildSpec.fromSourceFilename("buildspec.yaml"),
      environment: {
        buildImage: codebuild.LinuxBuildImage.STANDARD_5_0
      }
    });

    // Create the build project that will invalidate the cache
    const S3CFServiceInvalidateCF = new codebuild.PipelineProject(this, `InvalidateProject`, {
      buildSpec: codebuild.BuildSpec.fromObject({
        version: '0.2',
        phases: {
          build: {
            commands: [
              'aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_ID} --paths "/*"',
            ],
          },
        },
      }),
      environmentVariables: {
        CLOUDFRONT_ID: { value: cloudfrontDistro.distributionId },
      },
    });

    // Add Cloudfront invalidation permissions to the project
    const distributionArn = `arn:aws:cloudfront::${this.account}:distribution/${cloudfrontDistro.distributionId}`;
    S3CFServiceInvalidateCF.addToRolePolicy(new iam.PolicyStatement({
      resources: [distributionArn],
      actions: [
        'cloudfront:CreateInvalidation',
      ],
    }));



    const sourceOutput = new codepipeline.Artifact()
    const buildOutput = new codepipeline.Artifact()
    const S3CFServicePipeline = new codepipeline.Pipeline(this, "S3CFServicePipeline", {
      pipelineName: "S3CFService-Pipeline",
      stages: [
        {
          stageName: "S3CFServiceSource",
          actions: [
            new codepipeline_actions.CodeStarConnectionsSourceAction({
              actionName: "Checkout",
              connectionArn: "arn:aws:codestar-connections:us-east-1:724050724157:connection/a777e566-e814-43b1-af2e-b95229e78e4a",
              output: sourceOutput,
              owner: "AWS",
              repo: "service_repository_id_here",
              branch: "service_branch_name_here"
            })
          ]
        },
        {
          stageName: "S3CFServiceBuild",
          actions: [
            new codepipeline_actions.CodeBuildAction({
              actionName: "BuildStaticSite",
              project: S3CFServiceBuild,
              input: sourceOutput,
              outputs: [buildOutput]
            })
          ]
        },
        {
          stageName: "S3CFServiceDeployment",
          actions: [
            new codepipeline_actions.S3DeployAction({
              actionName: "S3Deployment",
              bucket: s3bucket,
              input: buildOutput,
              runOrder: 1
            }),
            new codepipeline_actions.CodeBuildAction({
              actionName: "InvalidateCache",
              project: S3CFServiceInvalidateCF,
              input: buildOutput,
              runOrder: 2
            })
          ]
        }
      ]
    })

    new cdk.CfnOutput(this, 'PipelineEndpoint', {
      value: "https://${AWS::Region}.console.aws.amazon.com/codesuite/codepipeline/pipelines/${Pipeline}/view?region=${AWS::Region}",
      description: "The URL to access the pipeline"
    })

  }
}

