export AWS_DEFAULT_REGION=us-east-1
account_id=`aws sts get-caller-identity --query Account --output text`

aws s3api create-bucket \
  --bucket "proton-cli-templates-${account_id}" \

tar -zcvf s3CF-svc-template.tar.gz service/

aws s3 cp s3CF-svc-template.tar.gz s3://proton-cli-templates-${account_id}/s3CF-svc-template.tar.gz

rm s3CF-svc-template.tar.gz

  aws proton create-service-template \
  --name "Fargate-Public-Loadbalanced-Service" \
  --display-name "Fargate Public Loadblanced Service" \
  --description "Fargate Service with an Application Load Balancer"



aws proton create-service-template-version \
  --template-name "Fargate-Public-Loadbalanced-Service" \
  --source s3="{bucket=proton-cli-templates-${account_id},key=s3CF-svc-template.tar.gz}" \
  --compatible-environment-templates '[{"templateName":"Fargate-Public-VPC","majorVersion":"1"}]'
