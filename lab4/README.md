1. Виконав команди та перенаправив вивід у файл:
``` Bash
docker -v > my_work.log
docker -h >> my_work.log
docker run docker/whalesay cowsay Docker is fun >> my_work.log
```