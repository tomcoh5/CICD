#!/bin/bash
echo "running test for the website"
curl localhost:5000
if [ $? -eq 0 ]; then
    echo website running
else
    echo website not running
    exit 1
fi
