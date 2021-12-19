#!/usr/bin/env python3

import sys
import os
from datetime import datetime
#variable for any pcap file from the command line
file_name = sys.argv[1]

about = "Welcome to PyBash Auto-parsing Tool!"
print(about)
#user input variable
key = input("***Press ENTER to Contiue***")
print(key)

#variable for current time
now = datetime.now()
#formating for current time
current = now.strftime("%H:%M:%S")


#create a directory called "exports" 
cmd_dir = 'mkdir exports' + current
print("                                ")
print("********************************")
print('"exports" Directory Created!    ')
print("********************************")
#call create directory command
os.system(cmd_dir)

#read pcap with tshark and save to file
cmd_file = 'tshark -r ' + str(file_name) + ' > /home/kali/finalproject/pcap.log'

os.system(cmd_file)

#cut timestamp out of pcap log file
cut_cmd = 'cut -d " " -f 2 /home/kali/finalproject/pcap.log > timestamp.log'
#call cut command
os.system(cut_cmd)
#cut timestamp into first part only, at the (.)
cut_cmd2 = 'cut -d "." -f 1 timestamp.log | sort > cutstamp.log'
#call cut command
os.system(cut_cmd2)

#parse all src ips sort and count them
cmd = 'tshark -r ' + str(file_name) + ' -Y tcp -T fields -e ip.src | sort | uniq -c | sort -n'
#parse all dst ips sort and count them
cmd2 = 'tshark -r ' + str(file_name) + ' -Y tcp -T fields -e ip.dst | sort | uniq -c | sort -n'
#parse all src ports and count them
cmd3 = 'tshark -r ' + str(file_name) + ' -Y tcp -T fields -e tcp.srcport | sort | uniq -c | sort -n'
#parse all dst ports and count them
cmd4 = 'tshark -r ' + str(file_name) + ' -Y tcp -T fields -e tcp.dstport | sort | uniq -c | sort -n'
# parse all http traffic 
cmd5 = 'tshark -r ' + str(file_name) + ' -Y http | sort -n'
#export all http objects to current exports directory and redirected stdout to dev null
cmd6 = 'tshark -r ' + str(file_name) + ' --export-object http,/home/kali/finalproject/exports' + current + '> /dev/null'

#header formating
print("---------------------")
print("SOURCE IPs")
print("---------------------")
print("Count | Ips          ")
print("---------------------")
#call tshark shell command()
os.system(cmd)

#hearder formating
print("                     ")
print("---------------------")
print("DESTINATION IPs      ")
print("---------------------")
print("Count | Ips          ")
print("---------------------")
#call tshark shell command(2)
os.system(cmd2)

#header formating
print("                     ")
print("---------------------")
print("SOURCE PORTS         ")
print("---------------------")
print("Count | Port         ")
print("---------------------")
#call tshark shell command(3)
os.system(cmd3)

#header formating
print("                     ")
print("---------------------")
print("DESTINATION PORTS    ")
print("---------------------")
print("Count | port         ")
print("---------------------")
#call tshark shell command(4)
os.system(cmd4)

#header formating
print("                     ")
print("---------------------")
print("ALL HTTP TRAFFIC     ")
print("---------------------")
#call tshark shell command(5)
os.system(cmd5)

#header formating
print("                                                ")
print("************************************************")
print("HTTP OBJECTS SAVED TO RECENT EXPORTS DIRECTORY  ")
print("************************************************")
#call tshark shell command(5)
os.system(cmd6)

#header formating
print("                     ")
print("---------------------")
print("TIMELINE (DECODED)   ")
print("---------------------")

#function to convert unix timestamp 
def timeconvert(file):
    #emtpy timestamp list
    ts = []
    #empty trash list (for unwanted chars)
    trash = []
    #iterate through cutstamp.log file and remove unwanted chars
    for line in file:
        line = line.rstrip()
        #if the line is a number, then add to the timestamp list
        if line.isnumeric():
            ts.append(line)
        #if line is not a number, then add to the trash list
        else:
            trash.append(line)
    #iterate through the timestamp list
    for num in ts:
        #decode every unix timestamp into human readable format
        dt = datetime.fromtimestamp(int(num))
        #print decoded timestamp in stdout
        print(dt)
    #remove timestamp files from system
    cmd_rm = 'rm -r cutstamp.log timestamp.log pcap.log'
    os.system(cmd_rm)
            
        
        
        
#main function to open a file
def main():
    #open the cutstamp.log file as file_name
    file_name = ('/home/kali/finalproject/cutstamp.log')
    with open(file_name) as file_name:
        #call function
        timeconvert(file_name)

#dunder check
if __name__ == "__main__":
 main()
