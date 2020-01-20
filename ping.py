import imp
import subprocess
import os
import time
from datetime import datetime
import platform

def Ping(IP):
    #Checks if os is Windows
    if platform.system() == 'Windows':
        return subprocess.check_output("ping " + IP + " -n 1", shell=True).decode()
    #If it isn't do -c instead of -n
    else:
        return subprocess.check_output("ping " + IP + " -c 1", shell=True).decode()

def Readipfromcountry(filename, Country):
    return getVarFromFile(Country, filename)

def writeresult(Time, Country, File):
    with open(File, "a") as f:
        print("{0}, {1}, {2}".format(Time, Country, datetime.now()), file = f)

def ParseTimefromPingOutput(PingOutput):
    #Trim output to just Avg.
     X = PingOutput.split(",")
     if platform.system() == 'Windows':
        Y = X[5].split(" = ")
        XX = Y[1].split("ms")
        return int(XX[0])
     elif platform.system() == 'Darwin':
        y = X[2]
        z = y.split(' = ')[1]
        return float(z.split('/')[1])
     else:
        y = X[3]
        z = y.split(' = ')[1]
        return float(z.split('/')[2])


def getVarFromFile(Country, filename):
    #Open IP.py and return the data from the countries
    data = imp.load_source('data', filename)
    return data.IPs[Country]

def GetAllCountries(Filename):
    data = imp.load_source('data', Filename)
    return data.IPs.keys()

OutputFile = "Time.txt"
InputFile = "IP.py"
#If the output file exits, remove all the contents
if os.path.exists(OutputFile):
  os.remove(OutputFile)

#Get list of all countries
while True:
    for Country in GetAllCountries(InputFile):
        print("pinging " + Country)
        #Read IP addresses for a single county from IP.py
        IP = Readipfromcountry(InputFile, Country)

        for x in IP:
            try:
                #Ping IP address once
                PingOutput = Ping(x)
                #Parse Avg. Time from PingOutput
                Time = ParseTimefromPingOutput(PingOutput)
                #Write ping time to .txt file (ms)
                writeresult(Time, Country, OutputFile)
            #If KeyboardInterrupt is activated, stop the program 
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
               print("exception while pinging " + Country + ": " + x)
