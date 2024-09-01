Sure, here's the updated README section for Mac M1/M2/M3 ARM64 users, including instructions to install Docker Buildx and up to the `docker-compose up` command:

---

## 💻 **Special Instructions for Mac M1/M2/M3 (ARM64) Users**

If you're using a Mac with an M1, M2, or M3 chip, follow these steps to build Docker images in the amd64 format:

### 1. **Install Docker Buildx**

Docker Buildx is included with Docker Desktop, but you might need to enable it. Ensure you have Docker Desktop installed and then enable Buildx:

```bash
docker buildx create --use
```

### 2. **Set the Default Platform**

You can set the default platform to `linux/amd64` for the build process. There are two ways to do this:

#### Option 1: Using Environment Variable in Command

Set the environment variable directly in the build command:
```bash
DOCKER_DEFAULT_PLATFORM=linux/amd64
```

#### Option 2: Using a .env File

Alternatively, you can create a `.env` file in the same directory as your `docker-compose.yml` file and add the environment variable there.

Create a `.env` file with the following content:
```
DOCKER_DEFAULT_PLATFORM=linux/amd64
```

### 3. **Build Docker Images**

For the initial build, use:
```bash
docker-compose build --no-cache
```


### 4. **Launch the Docker Compose System**

Once the images are built, you can launch the Docker Compose system:
```bash
docker-compose up -d
```

---

## 🤝 **Good luck**

Made with ❤️ by [Naveen](https://www.linkedin.com/in/naveen-devops-sre/)

**Happy building! 🚀 & experimenting with your Big Data environment!** 🐋

---