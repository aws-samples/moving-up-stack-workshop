## Running the container on ECS

## See docker commands below as reference when creating ECS Task Definition


### Frontend
API_URL_VALUE="https://ALB_DNS"
IMAGE="public.ecr.aws/d5d1e3w4/modernization-workshop-frontend:latest"
docker run --name frontend-nginx -p 8080:80 -e API_URL_VALUE=${API_URL_VALUE} ${IMAGE}

### API-Monolith
IMAGE="public.ecr.aws/d5d1e3w4/modernization-workshop-api-monolith:latest"
docker run --name api-monolith -p 5000:5000 \
    -e REDIS_HOST=<REDIS_HOST> \
    -e REDIS_PORT=<REDIS_PORT> \
    -e DB_HOST=<DB_HOST> \
    -e DB_USER=<DB_USER> \
    -e DB_PASSWORD=<DB_PASSWORD> \
    -e DATABASE=<DATABASE> \
    ${IMAGE}

### API-Users
IMAGE="public.ecr.aws/d5d1e3w4/modernization-workshop-api-users:latest"
docker run --name api-users -p 5000:5000 \
    -e REDIS_HOST=<REDIS_HOST> \
    -e REDIS_PORT=<REDIS_PORT> \
    -e DB_HOST=<DB_HOST> \
    -e DB_USER=<DB_USER> \
    -e DB_PASSWORD=<DB_PASSWORD> \
    -e DATABASE=<DATABASE> \
    ${IMAGE}

### API-Posts
IMAGE="public.ecr.aws/d5d1e3w4/modernization-workshop-api-posts:latest"
docker run --name api-posts -p 5000:5000 \
    -e REDIS_HOST=<REDIS_HOST> \
    -e REDIS_PORT=<REDIS_PORT> \
    -e DB_HOST=<DB_HOST> \
    -e DB_USER=<DB_USER> \
    -e DB_PASSWORD=<DB_PASSWORD> \
    -e DATABASE=<DATABASE> \
    ${IMAGE}

### API-Threads
IMAGE="public.ecr.aws/d5d1e3w4/modernization-workshop-api-threads:latest"
docker run --name api-threads -p 5000:5000 \
    -e REDIS_HOST=<REDIS_HOST> \
    -e REDIS_PORT=<REDIS_PORT> \
    -e DB_HOST=<DB_HOST> \
    -e DB_USER=<DB_USER> \
    -e DB_PASSWORD=<DB_PASSWORD> \
    -e DATABASE=<DATABASE> \
    ${IMAGE}
