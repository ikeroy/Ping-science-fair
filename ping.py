import imp
import subprocess
import os
import time
from datetime import datetime

start_time = datedame.now().strftime("%H:%M:%S")

def Ping(IP):
    return subprocess.check_output("ping " + IP + " -n 1", shell=True).decode()

def Readipfromcountry(filename, Country):
    return getVarFromFile(Country, filename)

def writeresult(Time, Country, File):
    with open(File, "a") as f:
        print("{0}, {1}, {2}".format(Time, Country, datetime.now()), file = f)

def ParseTimefromPingOutput(PingOutput):
     X = PingOutput.split(",")
     Y = X[5].split(" = ")
     XX = Y[1].split("ms")
     return int(XX[0])

def getVarFromFile(Country, filename):
    data = imp.load_source('data', filename)
    return data.IPs[Country]

def GetAllCountries(Filename):
    data = imp.load_source('data', Filename)
    return data.IPs.keys()

OutputFile = "Time.txt"
InputFile = "IP.py"
if os.path.exists(OutputFile):
  os.remove(OutputFile)

#Get list of all countries
while True:
    for Country in GetAllCountries(InputFile):
        #Read IP addresses for a single county from IP.py
        IP = Readipfromcountry(InputFile, Country)

        for x in IP:
            #Ping IP address once
            PingOutput = Ping(x)
            #Parse Avg. Time from PingOutput
            Time = ParseTimefromPingOutput(PingOutput)
            #Write ping time to .txt file (ms)
            writeresult(Time, Country, OutputFile)
