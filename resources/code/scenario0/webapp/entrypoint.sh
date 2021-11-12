echo "******************************"
echo "API_URL_VALUE=${API_URL_VALUE}"

path="/usr/share/nginx/html/js/"
FILE_NAME=$(ls ${path} | grep -m 1 app.)
sed -i "s|VUE_APP_API_URL|${API_URL_VALUE}|g" "${path}${FILE_NAME}"
nginx -g 'daemon off;'
