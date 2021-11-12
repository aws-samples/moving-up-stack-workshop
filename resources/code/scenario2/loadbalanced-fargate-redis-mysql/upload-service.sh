export AWS_DEFAULT_REGION=us-east-1
account_id=`aws sts get-caller-identity --query Account --output text`

aws s3api create-bucket \
  --bucket "proton-cli-templates-${account_id}" \

tar -zcvf farRedMy-svc-template.tar.gz service/

aws s3 cp farRedMy-svc-template.tar.gz s3://proton-cli-templates-${account_id}/farRedMy-svc-template.tar.gz

rm farRedMy-svc-template.tar.gz

  aws proton create-service-template \
  --name "Fargate-Public-Loadbalanced-Service-Redis-MySQL" \
  --display-name "Fargate Public Loadblanced Service with Redis and MySQL" \
  --description "Fargate Service with an Application Load Balancer, Redis and MySQL"



aws proton create-service-template-version \
  --template-name "Fargate-Public-Loadbalanced-Service-Redis-MySQL" \
  --source s3="{bucket=proton-cli-templates-${account_id},key=farRedMy-svc-template.tar.gz}" \
  --compatible-environment-templates '[{"templateName":"Fargate-Public-Private-VPC","majorVersion":"1"}]'
