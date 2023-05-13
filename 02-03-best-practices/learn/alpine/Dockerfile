FROM alpine:3.11.5

COPY ../.. /opt

RUN apk add --no-cache nginx && mkdir -p /run/nginx
    && rm -rf /var/lib/apt/lists/*

COPY custom.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off"]


