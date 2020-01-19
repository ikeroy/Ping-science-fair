## Running locally

To run each program, open cmd and cd into the file directory of the program. Then if you have python 3.5 or later, run the python command and type "import (filename)" The only program that is runnable (except this file) is ping.py. Ping.py reads IP adresses from IP.py that go to aws servers.

## Running on ec2

Log in to the instance
`ssh -i <region>.pem ec2-user@<ec2 host>`

First check if it is already running
`screen -ls`

If `screen` doesn't return anything, check if git and python3 are installed. If they aren't, here's how to set it up
```
sudo yum -y install git
git clone https://github.com/ikeroy/Ping-science-fair.git
sudo yum -y install python3
```

When running the program, use screen so you can disconnect and it will keep running
```
cd Ping-science-fair/ 
screen -S pinger -d -m python3 ping.py
```

Confirm it is running. You should see pinger now when you run `screen -ls`

To reattach to the program: `screen -S pinger -r`

To detach, type `ctrl-a, ctrl-d`

