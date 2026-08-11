# Docker Command Cheat Sheet

| Task | Command |
|---|---|
| Running containers | `docker ps` |
| All containers | `docker ps -a` |
| Images | `docker images` |
| Build image | `docker build -t <image> .` |
| Run container | `docker run -d -p <host>:<container> <image>` |
| Stop container | `docker stop <container>` |
| Start stopped container | `docker start <container>` |
| Restart container | `docker restart <container>` |
| Remove container | `docker rm <container>` |
| Force-remove container | `docker rm -f <container>` |
| Remove image | `docker rmi <image>` |
| Container logs | `docker logs <container>` |
| Follow logs | `docker logs -f <container>` |
| Enter container | `docker exec -it <container> /bin/sh` |
| Container details | `docker inspect <container>` |
| Resource usage | `docker stats` |
| Compose build | `docker compose build` |
| Compose up | `docker compose up --build` |
| Compose up detached | `docker compose up -d --build` |
| Compose status | `docker compose ps` |
| Compose logs | `docker compose logs -f` |
| Compose restart | `docker compose restart` |
| Compose stop | `docker compose stop` |
| Compose down | `docker compose down` |
| Docker Hub login | `docker login` |
| Tag image | `docker tag <image>:<tag> <user>/<repo>:<tag>` |
| Push image | `docker push <user>/<repo>:<tag>` |
| Pull image | `docker pull <user>/<repo>:<tag>` |
| Docker version | `docker version` |
| Docker information | `docker info` |
| Networks | `docker network ls` |
| Volumes | `docker volume ls` |

## Port Mapping

Always remember:

```text
-p HOST_PORT:CONTAINER_PORT
```

Example:

```bash
docker run -d -p 8000:6001 my-fastapi-app
```

means:

```text
localhost:8000  →  container:6001
```

The application inside the container must actually listen on the container-side port.
