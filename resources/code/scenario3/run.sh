for var in "$@"
do
  case "$var" in
    instance_infrastructure)
      python ./helper.py \
        "instance_infrastructure" \
        "./loadbalanced-fargate-redis-mysql/service/instance_infrastructure/cloudformation.yaml" \
        "./service_template/instance_infrastructure/cloudformation.yaml"
      ;;
    schema)
      python ./helper.py \
        "schema" \
        "./loadbalanced-fargate-redis-mysql/service/schema/schema.yaml" \
        "./service_template/schema/schema.yaml"
      ;;
    specs)
      python ./helper.py \
        "specs" \
        "./loadbalanced-fargate-redis-mysql/specs/posts-api.yaml" \
        "./service_template/specs/posts.yaml"
      ;;
    *)
      ;;
  esac
done
