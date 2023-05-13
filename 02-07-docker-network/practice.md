Разбираемся в имеющимися сетями

Инструкция подключения к стенду. Чтобы запустить стенд данного модуля, нужно запустить стенд с любой страницы данного модуля.

    Посмотрим какие сети уже есть в Docker:

docker network ls

    По-умолчанию, все контейнеры подключаются к Bridge-сети. Проверим это, установив brctl:

yum install bridge-utils -y

    Посмотрим состояние текущего bridge и подключенных интерфейсов:

brctl show
ip a

    Запустим два контейнера:

docker run -dit --name alpine1 alpine ash
docker run -dit --name alpine2 alpine ash

    Посмотрим теперь на состояние нашего bridge и увидим два подключенных интерфейса контейнеров:

brctl show
docker network inspect bridge

Или же воспользуемся следующим выражением, для короткого отображения IP адресов наших контейнеров

docker network inspect bridge -f '{{range .Containers}}{{println .Name}}{{println .IPv4Address}}{{end}}'

    Зайдем внутрь контейнера и посмотрим сетевые интерфейсы:

docker attach alpine1
ip a

    Попингуем внешний мир и соседний контейнер по IP-адресу:

ping -c 3 ya.ru
ping -c 3 <ip-адрес второго контейнера>

    Но если мы попробуем попинговать второй контейнер по имени, то ничего не выйдет:

ping -c 3 alpine2

    Глянем настройки DNS у контейнера и увидим, что он использует такие же настройки, что и хост:

cat /etc/resolv.conf
exit
cat /etc/resolv.conf

    Подчистим за собой:

docker container stop alpine1 alpine2
docker container rm alpine1 alpine2

Создаем свою сеть в Docker

    Создадим свою сеть типа bridge:

docker network create --driver bridge alpine-net

    Проверим что все ок:

docker network ls
brctl show
docker network inspect alpine-net

    Запустим три контейнера, два из них будут подключены к нашей новой сети, а один нет:

docker run -dit --name alpine1 --network alpine-net alpine ash
docker run -dit --name alpine2 --network alpine-net alpine ash
docker run -dit --name alpine3 alpine ash

    Проверим выполненные действия:

docker network inspect bridge
docker network inspect alpine-net
brctl show

    Подключимся к контейнеру в нашей созданной сети и попингуем соседние:

docker container attach alpine1
ping -c 2 alpine2
ping -c 2 alpine3

    Видим, что контейнер в той же сети теперь пингуется по имени, а в другой сети нет. Т.е. 
когда мы создаем свою сеть, то мы можем обращаться по имени контейнера. 
Более того, к контейнеру другой сети нельзя будет подключиться даже по IP-адресу. Посмотрим его настройки DNS:

cat /etc/resolv.conf
exit

    Почистим за собой:

docker container stop alpine1 alpine2 alpine3
docker container rm alpine1 alpine2 alpine3
docker network rm alpine-net

