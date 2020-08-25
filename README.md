# CI jenkins 
little project i made for testing and building in jenkins



## Installation

start by installing docker on your linux 

```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
```
dont forget to clone this repository

## Usage

build the image

```bash
docker build -t jenkins-docker .
```
and then run it with
```bash
docker run -d -p 50000:50000 -p 8080:8080 -v  -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker
```

