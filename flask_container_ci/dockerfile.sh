#!/bin/bash
cd /jenkins-pipeline/flask_container_ci/app
docker build -t myflask .

if [ $? -eq 0 ]; then
    echo image succesfuly built
else
    echo image didnt build
    exit
fi

