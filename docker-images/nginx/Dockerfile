FROM nginx
 
# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
 
# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
 
COPY server.crt /etc/nginx/ssl.crt
COPY server.key /etc/nginx/ssl.key
COPY myca.crt /etc/nginx/ca-cert.pem
 
EXPOSE 443
