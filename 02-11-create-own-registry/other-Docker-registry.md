# 4. Краткий обзор сторонних Docker registry, установка Harbor

Бывает, что GitLab не хватает, тогда помогут
Полноценные registry:
- Nexus от SonarType один из самых популярных
- Portus от Suse уже устарел
- Quay от RedHat платный
- Artifactory от JFrog есть бесплатный
- Harbor от VMware с этим мы будем практиковаться

## Установка Harbor

Скачаем с github конкретныйю версию, с которой все работает
'''
wget https://github.com/goharbor/harbor/releases/download/v2.3.4/harbor-offline-installer-v2.0.6.tgz
'''
распакуем архив
'''
tar xvf harbor-offline-installer-v2.0.6.tgz
'''
И передем в дирректорию
и скопируем туда свой harbor.yml c нужными настройками

Запускаем
'''
./prepare
'''
Установка выполнена, в итоге у нас был созадан docker-compose, вот его мы щас и запустим.
'''
docker-compose up -d
'''

harbor registry создан
