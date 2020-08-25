# CI jenkins 
little project i made for testing and building in jenkins to flask web app that i made 

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
docker run -d -p 50000:50000 -p 8080:8080 --name myjenkins -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker
```

now get in the container 
```bash
docker exec -u root --it myjenkins bash
```
run some commands 
```bash
apt-get update -y && apt-get install vim -y 
```
now clome the repository 
```bash
git clone https://github.com/tomcoh5/jenkins-pipeline.git
```
from here you just need to create the pipeline with the jenkinsfile and you should be done 
