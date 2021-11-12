export AWS_DEFAULT_REGION=us-east-1
account_id=`aws sts get-caller-identity --query Account --output text`

aws s3api create-bucket \
  --bucket "proton-cli-templates-${account_id}" \


  aws proton create-environment-template \
  --name "S3-Cloudfront" \
  --display-name "S3 Bucket and Cloudfront" \
  --description "Creates an S3 bucket and Cloudfront distribution that can be used to host static sites"


tar -zcvf s3CF-env-template.tar.gz environment/

aws s3 cp s3CF-env-template.tar.gz s3://proton-cli-templates-${account_id}/s3CF-env-template.tar.gz

rm s3CF-env-template.tar.gz

aws proton create-environment-template-version \
  --template-name "S3-Cloudfront" \
  --source s3="{bucket=proton-cli-templates-${account_id},key=s3CF-env-template.tar.gz}"


aws proton wait environment-template-version-registered \
  --template-name "S3-Cloudfront"