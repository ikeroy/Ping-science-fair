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

### ec2 hosts
|Region|Availabilty Zone|IP address|DNS|
|-|-|-|-|
|Sydney|a|52.63.89.125|ec2-52-63-89-125.ap-southeast-2.compute.amazonaws.com|
||b|54.252.150.92|ec2-54-252-150-92.ap-southeast-2.compute.amazonaws.com|
||c|54.252.153.177|ec2-54-252-153-177.ap-southeast-2.compute.amazonaws.com|
|Sao Paulo|a|18.231.118.175|ec2-18-231-118-175.sa-east-1.compute.amazonaws.com|
||c|54.94.183.14|ec2-54-94-183-14.sa-east-1.compute.amazonaws.com|
|Hong Kong|a|18.162.244.94|ec2-18-162-244-94.ap-east-1.compute.amazonaws.com|
||b|18.163.56.62|ec2-18-163-56-62.ap-east-1.compute.amazonaws.com|
||c|18.163.73.210|ec2-18-163-73-210.ap-east-1.compute.amazonaws.com|
|Mumbai|a|15.206.80.139|ec2-15-206-80-139.ap-south-1.compute.amazonaws.com|
||b|13.235.87.222|ec2-13-235-87-222.ap-south-1.compute.amazonaws.com|
|London|a|||
||b|||
||c|||
|Montreal|a|||
||b|||
||c|||
|Singapore|a|||
||b|||
||c|||
|N.Virginia|a|||
||b|||
||c|||
|Tokyo|a|||
||b|||
||c|||

