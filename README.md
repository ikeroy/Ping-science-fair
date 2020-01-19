## Running locally

To run each program, open cmd and cd into the file directory of the program. Then if you have python 3.5 or later, run the python command and type "import (filename)" The only program that is runnable (except this file) is ping.py. Ping.py reads IP adresses from IP.py that go to aws servers.

## Running on ec2

Log in to the instance
`ssh -i <region>.pem ec2-user@<ec2 host>`

First check if it is already running
`screen -ls`

If `screen` doesn't return anything, check if git and python3 are installed. If they aren't, here's how to set it up
```
sudo yum -y install git python3
git clone https://github.com/ikeroy/Ping-science-fair.git
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
|London|a||ec2-3-10-180-172.eu-west-2.compute.amazonaws.com|
||b||ec2-3-9-181-152.eu-west-2.compute.amazonaws.com|
||c||ec2-3-11-81-223.eu-west-2.compute.amazonaws.com|
|Montreal|a||ec2-15-222-15-243.ca-central-1.compute.amazonaws.com|
||b||ec2-35-183-41-84.ca-central-1.compute.amazonaws.com|
|Singapore|a||ec2-52-77-217-241.ap-southeast-1.compute.amazonaws.com|
||b||ec2-18-138-58-21.ap-southeast-1.compute.amazonaws.com|
||c||ec2-18-138-228-155.ap-southeast-1.compute.amazonaws.com|
|N.Virginia|a||ec2-54-90-215-1.compute-1.amazonaws.com|
||b||ec2-54-91-16-137.compute-1.amazonaws.com|
||c||ec2-3-214-143-16.compute-1.amazonaws.com|
|Tokyo|a||ec2-3-112-220-162.ap-northeast-1.compute.amazonaws.com|
||c||ec2-18-182-38-146.ap-northeast-1.compute.amazonaws.com|
||d||ec2-18-177-153-44.ap-northeast-1.compute.amazonaws.com|

## Gathering results
For ec2s

***Careful to avoid overwriting Time.txt files! Be sure to make file names unique by adding in region and availability zone in the file the file name.***

`scp -i <region>.pem ec2-user@<ec2-host>:Ping-science-fair/Time.txt ./<region>-<AZ>-Time.txt`

This oughta do it
```
scp -i syndney.pem ec2-user@ec2-52-63-89-125.ap-southeast-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./syndney-a-Time.txt
scp -i syndney.pem ec2-user@ec2-54-252-150-92.ap-southeast-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./syndney-b-Time.txt
scp -i syndney.pem ec2-user@ec2-54-252-153-177.ap-southeast-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./syndney-c-Time.txt
scp -i sao-paulo.pem ec2-user@ec2-18-231-118-175.sa-east-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./sao-paulo-a-Time.txt
scp -i sao-paulo.pem ec2-user@ec2-54-94-183-14.sa-east-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./sao-paulo-c-Time.txt
scp -i hong-kong.pem ec2-user@ec2-18-162-244-94.ap-east-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./hong-kong-a-Time.txt
scp -i hong-kong.pem ec2-user@ec2-18-163-56-62.ap-east-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./hong-kong-b-Time.txt
scp -i hong-kong.pem ec2-user@ec2-18-163-73-210.ap-east-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./hong-kong-c-Time.txt
scp -i mumbai.pem ec2-user@ec2-15-206-80-139.ap-south-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Mumbai-a-Time.txt
scp -i mumbai.pem ec2-user@ec2-13-235-87-222.ap-south-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Mumbai-b-Time.txt
scp -i London_1.pem ec2-user@ec2-3-10-180-172.eu-west-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./London-a-Time.txt
scp -i London_1.pem ec2-user@ec2-3-9-181-152.eu-west-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./London-b-Time.txt
scp -i London_1.pem ec2-user@ec2-3-11-81-223.eu-west-2.compute.amazonaws.com:Ping-science-fair/Time.txt ./London-c-Time.txt
scp -i Canada.pem ec2-user@ec2-15-222-15-243.ca-central-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Montreal-a-Time.txt
scp -i Canada.pem ec2-user@ec2-35-183-41-84.ca-central-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Montreal-b-Time.txt
scp -i Singapore.pem ec2-user@ec2-52-77-217-241.ap-southeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Singapore-a-Time.txt
scp -i Singapore.pem ec2-user@ec2-18-138-58-21.ap-southeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Singapore-b-Time.txt
scp -i Singapore.pem ec2-user@ec2-18-138-228-155.ap-southeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Singapore-c-Time.txt
scp -i Virginia.pem ec2-user@ec2-54-90-215-1.compute-1.amazonaws.com:Ping-science-fair/Time.txt ./Virginia-a-Time.txt
scp -i Virginia.pem ec2-user@ec2-54-91-16-137.compute-1.amazonaws.com:Ping-science-fair/Time.txt ./Virginia-b-Time.txt
scp -i Virginia.pem ec2-user@ec2-3-214-143-16.compute-1.amazonaws.com:Ping-science-fair/Time.txt ./Virginia-c-Time.txt
scp -i TokYo.pem ec2-user@ec2-3-112-220-162.ap-northeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Tokyo-a-Time.txt
scp -i TokYo.pem ec2-user@ec2-18-182-38-146.ap-northeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Tokyo-c-Time.txt
scp -i TokYo.pem ec2-user@ec2-18-177-153-44.ap-northeast-1.compute.amazonaws.com:Ping-science-fair/Time.txt ./Tokyo-d-Time.txt
```
