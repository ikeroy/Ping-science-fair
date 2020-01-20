import imp
import subprocess
import os
import time
from datetime import datetime
import platform

#Pings an IP
#IP:string. IP is inserted into the ping command
#returns the output of the ping command:String
def Ping(IP):
    #Checks if os is Windows
    if platform.system() == 'Windows':
        return subprocess.check_output("ping " + IP + " -n 1", shell=True).decode()
    #If it isn't do -c instead of -n
    else:
        return subprocess.check_output("ping " + IP + " -c 1", shell=True).decode()
    
#Get the IP adresses from this country and this file
#Filename:String. Is the input filename that contains all the IP adresses
#Country:The name of a country in the filename
#Reuturn getVarFromFile(referenced later)
def Readipfromcountry(filename, Country):
    #Open IP.py and return the data from the countries
    data = imp.load_source('data', filename)
    return data.IPs[Country]

#Write in this file the time it took to ping this country, the country, and the current time
#Time:Integer/Float/String. Time it took to ping a country
#Country:String. The country that got pinged
#File:the file it writes to
#Returns None
def writeresult(Time, Country, File):
    with open(File, "a") as f:
        print("{0}, {1}, {2}".format(Time, Country, datetime.now()), file = f)
        
#Trim output to just Avg.
#PingOutput:String. The output of the ping command
#Returns the Avg. time of the ping command
def ParseTimefromPingOutput(PingOutput):
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
   
#Gets all countries from a file
#Filename:String. The file that contains IP adresses in each country
#Returns all countries:List of strings
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
