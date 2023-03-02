# Список основных комманд

|Commands|Description|
|-----------------|-----------------------|
|docker ps |Список всех запущенных контейнеров|
|docker ps -a |Список всех запущенных и остановленных контейнеров|
|docker  images|спсок всех образов|
|docker run name_image |создаем и запускаем контейнер из образа name_image, если образа нет на хосте, он будет скачан из докерхаба|
|docker run -d name_image |создаем и запускаем контейнер из образа name_image в фоне |
|docker run -it name_image|создаем и запускаем контейнер из образа name_image и заходим в его терминал|
|docker container prune |удалить все контейнеры и работающие и остановленые|
|docker container inspect id_or_name_container |подробная информация о контейнере|
|docker container inspect id_or_name_container &#124; grep IPAdress |подробная информация о контейнере c фильтром по полю IPAdress|
|docker pull name_image |скачать образ из dockerhub|
|docker stop id_or_name_container |остановка контейнера|
|docker kill id_or_name_container |остановка контейнера, если на stop не реагирует|
|docker exec -it id_or_name_container bash |запускаем дополнительный процесс в нашем контейцнере bash не во всех образах работает, можно попробовать sh, запувская данную оболочку мы попадаем во внутрь контейнера|     
|docker  ||     
|docker  ||     
|docker  ||     
