export AWS_DEFAULT_REGION=us-east-1
account_id=`aws sts get-caller-identity --query Account --output text`

aws s3api create-bucket \
  --bucket "proton-cli-templates-${account_id}" \


  aws proton create-environment-template \
  --name "Fargate-Public-Private-VPC" \
  --display-name "Fargate Public and Private VPC" \
  --description "VPC with Public and Private Access and ECS Cluster"


tar -zcvf far-pubpriv-env-template.tar.gz environment/

aws s3 cp far-pubpriv-env-template.tar.gz s3://proton-cli-templates-${account_id}/far-pubpriv-env-template.tar.gz

rm far-pubpriv-env-template.tar.gz

aws proton create-environment-template-version \
  --template-name "Fargate-Public-Private-VPC" \
  --source s3="{bucket=proton-cli-templates-${account_id},key=far-pubpriv-env-template.tar.gz}"


aws proton wait environment-template-version-registered \
  --template-name "Fargate-Public-VPC"