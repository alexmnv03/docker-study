# 2 Теория работы с образами в командной строке, практическое задание

Вот такая команда для сборки образов не рекомендуется
'''
docker container commit 80353456342
'''
если надо присвоить тэг образу, то вот команда
'''
docker image tag ab80353456342 my-app:1.1
'''
или лучше указать имя где он будет храниться
'''
docker image tag ab80353456342 registry-host:5000/myname/my-app:1.1
'''
Если мы хотим отправить образ на хранение в репозиторий, то запушим
'''
docker image push registry-host:5000/myname/my-app:1.1
'''

Остановите контейнер mirror и запустите такой же, но с именем registry и без указания переменных. Это будет наш простой локальный registry.
'''
docker rm -f bc934783247843
'''
'''
docker run \
-d \
-p 5000/5000 \
--name=registry \
registry
'''
Попробуйте теперь пересобрать образ с тэгом localhost:5000/app:1.1 и запушить его.
'''
docker build -t localhost:5000/app:1.1 .
'''
'''
docker push localhost:5000/app:1.1
'''
удалим его
'''
docker rm -f registry
'''
