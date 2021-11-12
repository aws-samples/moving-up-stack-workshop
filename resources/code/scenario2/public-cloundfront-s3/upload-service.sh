export AWS_DEFAULT_REGION=us-east-1
account_id=`aws sts get-caller-identity --query Account --output text`

aws s3api create-bucket \
  --bucket "proton-cli-templates-${account_id}" \

tar -zcvf s3CF-svc-template.tar.gz service/

aws s3 cp s3CF-svc-template.tar.gz s3://proton-cli-templates-${account_id}/s3CF-svc-template.tar.gz

rm s3CF-svc-template.tar.gz

  aws proton create-service-template \
  --name "S3-CloudFront-Service" \
  --display-name "S3 CloudFront Service" \
  --description "Creates an S3 bucket and Cloudfront distribution that can be used to host static sites"


aws proton create-service-template-version \
  --template-name "S3-CloudFront-Service" \
  --source s3="{bucket=proton-cli-templates-${account_id},key=s3CF-svc-template.tar.gz}" \
  --compatible-environment-templates '[{"templateName":"S3-Cloudfront","majorVersion":"2"}]'

aws proton wait environment-template-version-registered \
  --template-name "S3-Cloudfront-Service"