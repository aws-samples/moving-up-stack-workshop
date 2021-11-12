IMAGE_NAME="modernization-workshop-api-posts"

for var in "$@"
do
  case "$var" in
    run)
      flask run
      ;;
    docker-build)
      docker build --tag ${IMAGE_NAME}:latest .
      ;;
    docker-run)
      docker run --name ${IMAGE_NAME} -p 5000:5000 --rm ${IMAGE_NAME}:latest
      ;;
    docker-rm)
      docker stop ${IMAGE_NAME} && docker rm ${IMAGE_NAME}
      ;;
    rbr)
      bash ./run.sh docker-rm docker-build docker-run
      ;;
    *)
      ;;
  esac
done
