FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
#RUN mkdir -p /usr/share/nginx/html
#COPY app/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]