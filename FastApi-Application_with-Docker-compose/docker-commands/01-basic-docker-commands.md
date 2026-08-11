# Docker Basic Commands

## 1. Check Running Containers

```bash
docker ps
```

Shows only currently running containers.

---

## 2. Check All Containers

```bash
docker ps -a
```

Shows all containers, whether they are running or stopped.

---

## 3. Remove a Container

```bash
docker rm <container_id>
```

Example:

```bash
docker rm 5fccdc56e8c4
```

If the container is running, stop it first:

```bash
docker stop <container_id>
docker rm <container_id>
```

Or force-remove it:

```bash
docker rm -f <container_id>
```

---

## 4. Remove a Docker Image

```bash
docker rmi <image_name>
```

Example:

```bash
docker rmi hello-world
```

If Docker says the image is being used by a container, remove the related container first:

```bash
docker ps -a
docker rm <container_id>
docker rmi <image_name>
```

You can also remove an image by image ID:

```bash
docker rmi <image_id>
```

---

## 5. Build a Docker Image

From the directory containing the `Dockerfile`:

```bash
docker build -t <image_name> .
```

Example:

```bash
docker build -t my-fastapi-app .
```

- `-t` = assign a name/tag to the image
- `.` = current directory is the build context

---

## 6. List Docker Images

```bash
docker images
```

Shows local Docker images.

Modern equivalent:

```bash
docker image ls
```

---

# Running Containers

## 7. Run a Container

```bash
docker run -d -p 6001:6001 --name my-fastapi-container my-fastapi-app
```

Meaning:

- `-d` = detached mode; run in background
- `-p 6001:6001` = map host port 6001 to container port 6001
- `--name my-fastapi-container` = assign a custom container name
- `my-fastapi-app` = image to run

General syntax:

```bash
docker run -d -p HOST_PORT:CONTAINER_PORT --name <container_name> <image_name>
```

---

## 8. Docker Port Mapping

```bash
-p HOST_PORT:CONTAINER_PORT
```

```text
-p HOST_PORT:CONTAINER_PORT
   │              │
   │              └── Port where the application is
   │                  listening inside the container
   │
   └───────────────── Port on your host/machine
                      that receives the request
```

Example:

```bash
docker run -d -p 8000:6001 my-fastapi-app
```

Mapping:

```text
Your Computer                 Docker Container
localhost:8000  ────────────>  6001
                                │
                                └── FastAPI
```

The application can continue listening on `6001` inside the container while users access it through `8000` on the host.

---

## 9. Stop a Running Container

```bash
docker stop <container_id>
```

Example:

```bash
docker stop my-fastapi-container
```

Stopping a container does not remove it.

You can start it again with:

```bash
docker start my-fastapi-container
```

---

## 10. Restart a Container

```bash
docker restart <container_id>
```

Example:

```bash
docker restart my-fastapi-container
```

---

# Container Logs and Debugging

## 11. View Container Logs

```bash
docker logs <container_name>
```

Example:

```bash
docker logs my-fastapi-container
```

Useful for seeing application output such as `print()` statements and stdout/stderr logs.

---

## 12. Follow Live Logs

```bash
docker logs -f <container_name>
```

Example:

```bash
docker logs -f my-fastapi-container
```

`-f` means follow. New logs will continue appearing in the terminal.

Press `Ctrl + C` to stop following the logs. It does not stop the container.

---

## 13. Show Last N Log Lines

```bash
docker logs --tail 100 my-fastapi-container
```

---

## 14. Execute a Command Inside a Running Container

```bash
docker exec -it <container_name> /bin/bash
```

If Bash is not available:

```bash
docker exec -it <container_name> /bin/sh
```

This opens a shell inside the container.

Example:

```bash
docker exec -it my-fastapi-container /bin/sh
```

---

## 15. Run a Single Command Inside a Container

```bash
docker exec <container_name> <command>
```

Examples:

```bash
docker exec my-fastapi-container pwd
docker exec my-fastapi-container ls
docker exec my-fastapi-container python --version
docker exec my-fastapi-container pip list
docker exec my-fastapi-container env
```

---

## 16. Inspect a Container

```bash
docker inspect <container_name>
```

Useful for detailed configuration such as:

- Environment variables
- Network settings
- Mounts
- Port mappings
- Container configuration
- Image information

---

## 17. Check Container Resource Usage

```bash
docker stats
```

Shows live CPU, memory, network, and other resource usage for running containers.

---

# Image Commands

## 18. Inspect an Image

```bash
docker image inspect <image_name>
```

Example:

```bash
docker image inspect my-fastapi-app
```

---

## 19. Remove Unused Docker Objects

Be careful with cleanup commands.

Remove stopped containers:

```bash
docker container prune
```

Remove unused images:

```bash
docker image prune
```

Remove unused Docker resources:

```bash
docker system prune
```

Preview/check carefully before using aggressive cleanup commands.

---

# Docker Compose Commands

These commands should be run from the directory containing `compose.yml` or `docker-compose.yml`.

## 20. Build Images and Start Services

```bash
docker compose up --build
```

Builds required images and starts the services.

Runs in the foreground and shows logs in the terminal.

---

## 21. Build and Start in Detached Mode

```bash
docker compose up -d --build
```

- `-d` = detached mode
- `--build` = build images before starting services

---

## 22. Stop and Remove Compose Services

```bash
docker compose down
```

Stops and removes the containers and network created by Compose.

---

## 23. Check Compose Containers

```bash
docker compose ps
```

Shows the containers belonging to the current Compose project.

---

## 24. Restart Compose Services

```bash
docker compose restart
```

Restart all Compose services.

Restart a specific service:

```bash
docker compose restart <service_name>
```

---

## 25. View Compose Logs

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

View logs for one service:

```bash
docker compose logs -f <service_name>
```

Example:

```bash
docker compose logs -f backend
```

---

## 26. Rebuild Compose Images

```bash
docker compose build
```

Rebuilds the images without starting the services.

Without cache:

```bash
docker compose build --no-cache
```

---

## 27. Start Existing Compose Services

```bash
docker compose start
```

Starts previously created/stopped Compose containers.

This is different from:

```bash
docker compose up
```

because `up` can create/recreate containers and networks as needed.

---

## 28. Stop Compose Services Without Removing Them

```bash
docker compose stop
```

The containers remain and can later be started with:

```bash
docker compose start
```

---

# Docker Hub: Push an Image

## 29. Login to Docker Hub

```bash
docker login
```

Docker asks for credentials if they are not already available.

If Docker Desktop has already authenticated your account, the CLI may authenticate using existing credentials.

---

## 30. Check Local Images

```bash
docker images
```

Find the image you want to push.

Example:

```text
singleapp:latest
```

---

## 31. Tag an Image for Docker Hub

General syntax:

```bash
docker tag <local_image>:<local_tag> <username>/<repo_name>:<tag>
```

Example:

```bash
docker tag singleapp:latest ranjitsingh00786/demo:latest
```

This does not create a separate copy of the image. It creates another image reference/tag pointing to the same image.

Conceptually:

```text
singleapp:latest
       │
       └──────────────┐
                      ▼
                  Same Image
                      ▲
       ┌──────────────┘
       │
ranjitsingh00786/demo:latest
```

---

## 32. Push the Image

```bash
docker push ranjitsingh00786/demo:latest
```

Docker uploads the image's layers to Docker Hub.

---

# Docker Hub: Pull an Image

## 33. Pull an Image

```bash
docker pull ranjitsingh00786/demo:latest
```

This downloads the image from Docker Hub to the local Docker Engine.

---

## 34. Run a Pulled Image

```bash
docker run -d -p 6001:6001 --name my-fastapi-container ranjitsingh00786/demo:latest
```

---

# Docker Image Layers

A Docker image is made up of multiple layers.

When you push an image, you may see:

```text
be1274d3cce0: Pushed
56c3764f426f: Pushed
e9e92f492463: Pushed
...
latest: digest: sha256:...
```

These are image layers, not separate images.

Docker can reuse layers that already exist in the registry. This makes subsequent pushes and pulls more efficient.

---

# Useful Docker Information Commands

## 35. Docker Version

```bash
docker version
```

---

## 36. Docker System Information

```bash
docker info
```

---

## 37. Docker Help

```bash
docker --help
```

Command-specific help:

```bash
docker run --help
docker build --help
docker compose --help
```

---

# Useful Naming and Filtering Commands

## 38. Show Running Container IDs Only

```bash
docker ps -q
```

---

## 39. Show All Container IDs Only

```bash
docker ps -aq
```

---

## 40. Show Docker Networks

```bash
docker network ls
```

---

## 41. Show Docker Volumes

```bash
docker volume ls
```

---

## 42. Inspect a Docker Network

```bash
docker network inspect bridge
```

---

# Quick Workflow

## Build → Run → Check → Logs

```bash
docker build -t my-fastapi-app .
docker run -d -p 6001:6001 --name my-fastapi-container my-fastapi-app
docker ps
docker logs -f my-fastapi-container
```

## Stop → Remove Container → Remove Image

```bash
docker stop my-fastapi-container
docker rm my-fastapi-container
docker rmi my-fastapi-app
```

## Build → Tag → Push

```bash
docker build -t singleapp:latest .
docker tag singleapp:latest ranjitsingh00786/demo:latest
docker push ranjitsingh00786/demo:latest
```

## Pull → Run

```bash
docker pull ranjitsingh00786/demo:latest
docker run -d -p 6001:6001 --name my-fastapi-container ranjitsingh00786/demo:latest
```
