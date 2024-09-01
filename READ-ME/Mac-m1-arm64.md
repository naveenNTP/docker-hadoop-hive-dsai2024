Got it! Here's the updated README section with a dedicated section for setting up Docker Compose for Hadoop on your system:

---

## 💻 **Special Instructions for Mac M1/M2/M3 (ARM64) Users**

If you're using a Mac with an M1, M2, or M3 chip, follow these steps to build Docker images in the amd64 format:

### 1. **Install Docker Desktop**

First, ensure Docker Desktop is installed. You can download it from [Docker Desktop for Apple M1](https://docs.docker.com/desktop/install/mac-install/).

### 2. **Install Brew Package Manager (Optional)**

If you don't have Homebrew installed and want to use it for managing packages, you can install it with the following command (optional if you only need Docker):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. **Install Rosetta**

Rosetta is required for x86_64/amd64 emulation on Apple Silicon. Install it with the following command:

```bash
softwareupdate --install-rosetta --agree-to-license
```

### 4. **Enable Rosetta in Docker Desktop**

To enable Rosetta in Docker Desktop:

1. Open Docker Desktop.
2. Go to the top right corner and click on **Settings**.
3. Navigate to **General**.
4. Tick the option **Use Rosetta for x86_64/amd64 emulation on Apple Silicon**.
5. Restart Docker Desktop.

---

## 🐋 **Set Up Docker Compose for Hadoop on Your System**

### 5. **Install Docker Buildx**

Docker Buildx is included with Docker Desktop, but you might need to enable it. Ensure you have Docker Desktop installed and then enable Buildx:

```bash
docker buildx create --use
```

### 6. **Set the Default Platform**

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

### 7. **Build Docker Images**

For the initial build, use:

```bash
docker-compose build --no-cache
```

### 8. **Launch the Docker Compose System**

Once the images are built, you can launch the Docker Compose system:

```bash
docker-compose up -d
```

---

## 🤝 **Good luck**

Reach out for any help - [Naveen](https://www.linkedin.com/in/naveen-devops-sre/)

**Happy building! 🚀 & experimenting with your Big Data environment!** 🐋

---

Feel free to reach out if you need any more assistance!