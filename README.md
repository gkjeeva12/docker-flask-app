## Internship Details
- Name: G K Jeeva
- Intern ID: CITS3332
- Domain: DevOps
- Duration: 3rdJune 2026 – 1stJuly 2026
# Dockerized Flask Web Application

## Project Overview
A Flask web application containerized using Docker.

## Technologies Used
- Python Flask
- Docker
- Git
- GitHub

## Project Structure

DockerFlaskApp/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/

## Steps Performed

### 1. Created the project folder

```text
DockerFlaskApp
```

### 2. Created the following files

```text
app.py
requirements.txt
Dockerfile
```

### 3. Added Flask application code in app.py

### 4. Added dependency in requirements.txt

```text
Flask==3.0.0
```

### 5. Created Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### 6. Built the Docker image

```bash
docker build -t flask-app .
```

### 7. Verified the image

```bash
docker images
```

### 8. Ran the Docker container

```bash
docker run -d -p 5000:5000 flask-app
```

### 9. Verified the running container

```bash
docker ps
```

### 10. Accessed the application

Open:

```text
http://localhost:5000
```

### Output

The Flask application was successfully deployed inside a Docker container and accessed through the browser.


## Screenshots

### Docker Build
![Docker Build](screenshots/image.png)

### Running Container
![Container](screenshots/Container.png)

### Application Output
![Browser](screenshots/brower.png)
