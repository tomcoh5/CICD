import time
from subprocess import check_call
from urllib.request import urlopen

bashcommand = "docker run --rm -d --name=web -p 5000:5000 myflask"
process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
bashcommand2= "docker stop web"
# would poll in a loop:
time.sleep(5)
# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:5000").read()

    process = subprocess.Popen(bashcommand2.split(), stdout=subprocess.PIPE)
except:
    print("website not up")
    process = subprocess.Popen(bashcommand2.split(), stdout=subprocess.PIPE)

