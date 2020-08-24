import time
from subprocess import check_call
from urllib.request import urlopen

check_call(
        "docker run --rm --name=web -p 5000:5000 -d myflask".split()
)
# Wait for the server to start. A better implementation
# would poll in a loop:
time.sleep(5)
# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:5000").read()
finally:
    check_call("docker kill smk".split())
