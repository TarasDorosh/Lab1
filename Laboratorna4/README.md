# Lab4
---
### 1. Ознайомився з Docker.
---
### 2. Виконав команди:
   - sudo docker -v
   - sudo docker -h
   - sudo docker run docker/whalesay cowsay Docker is fun
   - **Перенаправив вивід в my_work.log:**
       - docker -v > my_work.log && docker -h >> my_work.log && sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log
---
### 3. Ознайомилася з документацією
---
### 4. - Виконав команди:
   - sudo docker pull python:3.8-slim
   - sudo docker images
   - sudo docker inspect python:3.8-slim
   - *Створив файл з іменем Dockerfile;*
   - *Замінив посилання на власний Git репозиторій*
---
### 5. Створив власний репозиторій на Docker Hub
---
### 6. Виконав команди:
   - sudo docker build -t tarasdorosh/test:django .
   - sudo docker images
   - sudo docker push tarasdorosh/test:django 
   - [my repository](https://hub.docker.com/repository/docker/tarasdorosh/test)
   - [django image](https://hub.docker.com/layers/131220110/tarasdorosh/test/django/images/sha256-d4ed082780dd4fce6343f8480ec67f7c9bc9d5de61c9e5556d8cd2726fb8d506?context=explore)
---
### 7. Веб-сайт працює
---
### 8. 
   - створив Dockerfile.site
   - Виконав білд імеджа:
       - sudo docker build -f Dockerfile.site -t tarasdorosh/test:monitoring .
       - sudo docker images
       - sudo docker push tarasdorosh/test:monitoring
       - [monitoring image](https://hub.docker.com/layers/131220705/tarasdorosh/test/monitoring/images/sha256-332eb2d08cb07d0a8950ae2f88f950ed4e521bfffed52d3065466c1171ba3095?context=explore)
   - Щоб отримати логи виконав команди:
       -  sudo docker run -it --rm -p 8000:8000 tarasdorosh/test:django
       -  sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log tarasdorosh/test:monitoring
