IMAGE_NAME="modernization-workshop-frontend"

for var in "$@"
do
  case "$var" in
    install)
      npm install
      ;;
    run)
      npm run serve
      ;;
    build)
      ENV_VALUE=$(cat .env)
      echo "VUE_APP_API_URL=VUE_APP_API_URL" > .env
      npm run build
      echo "${ENV_VALUE}" > .env
      ;;
    docker-build)
      docker build --tag ${IMAGE_NAME} .
      ;;
    docker-run)
      API_URL_VALUE="https://random-data-api.com"
      echo "Exposing container on port 8080"
      docker run --name ${IMAGE_NAME} -p 8080:80 -e API_URL_VALUE=${API_URL_VALUE} --rm ${IMAGE_NAME}
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
