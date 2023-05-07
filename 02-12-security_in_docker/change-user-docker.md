# Как сменить пользователя в контейнере с root

Вот пример Dockerfile:
```
From ubuntu
RUN mkdir /apt
RUN groupadd -r user && useradd -r -s /bin/false -g user
user
WORKDIR /apt
COPY ./apt
RUN chown -R user:user /apt
USER user
CMD node index.js
```
Тут мы создаем пользователя user, меняем права приложению на этого пользователя и добавляем 
диррективу user, т.е. сменили пользователя на user

Некоторые контейнеры имеют встроеных пользователей (например nodejs), тогда все еще проще, 
просто меняем пользователя и все:
```
Node node
```
