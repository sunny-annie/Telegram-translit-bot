# Telegram-translit-bot
Бот транслитерирует ФИО на латиницу в соответствии с [Приказом](https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/)

## Порядок работы
* Установитe [Docker](https://docs.docker.com/engine/install/)
* С помощью [BotFather](https://t.me/BotFather) создайте новый бот в Telegram
* Полученный токен поместите в значение переменной TOKEN в файле Dockerfile
* В терминале (в папке проекта) введите команду sudo docker build .
* С помощью команды sudo docker images проверьте созданный образ (image) и скопируйте IMAGE ID
* Введите команду sudo docker run -d -p 80:80 [IMAGE ID], подставив значение [IMAGE ID], чтобы запустить бота
* Для получения логов запущенного контейнера используется команда docker logs [OPTIONS] CONTAINER. Список Options доступен [здесь](https://docs.docker.com/engine/reference/commandline/logs/)
* Чтобы узнать ID контейнера, воспользуйтесь командой sudo docker ps, скопируйте значение CONTAINER ID
* Для остановки работы бота выполните команду sudo docker stop [CONTAINER ID], подставив значение [CONTAINER ID]
