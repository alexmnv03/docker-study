Процесс создания Dockerfile для бэка
Dockerfile практически ни чем не отличается , т.к. бэк написан на nodejs

EXPOSE 5000 единственное отличие

Создадим образ
'''
docker build . -t time-pp-backend
'''

