#ByNick

'''⢰⣶⣶⣦⡀⠀⠀⠀⠀⢰⣶⣶⡆⠀⠀⠀⠀⢀⣴⣶⣶⡆
   ⢸⣿⣿⣿⣿⣦⠀⠀⠀⠸⠿⠿⠇⠀⠀⠀⣴⣿⣿⣿⣿⡇
   ⢸⣿⣿⣏⠙⢿⣷⣄⠀⢠⣤⣤⡄⠀⣠⣾⡿⠋⢸⣿⣿⡇
   ⢸⣿⣿⡇⠀⠀⠹⣿⣶⣸⣿⣿⣇⣶⣿⠏⠀⠀⢸⣿⣿⡇
   ⢸⣿⣿⣇⠀⣀⣀⠈⢿⣿⣿⣿⣿⡿⠁⣀⣀⠀⢸⣿⣿⡇
   ⢸⣿⣿⡇⣾⡟⠁⠀⠀⣹⣿⣿⣏⠀⠀⠈⢻⣷⢸⣿⣿⡇
   ⢸⣿⣿⣷⣿⠁⠀⢀⣼⣿⣿⣿⣿⣷⡀⠀⠈⣿⣾⣿⣿⡇
   ⢸⣿⣿⣿⣿⡀⣰⣿⠿⢹⣿⣿⡏⠿⣿⣆⢀⣿⣿⣿⣿⡇
   ⢸⣿⣿⡇⣿⣿⡿⠋⠀⢸⣿⣿⡇⠀⠙⢿⣿⣿⢸⣿⣿⡇
   ⢸⣿⣿⣿⣿⠿⣿⣦⣀⢸⣿⣿⡇⣀⣴⣿⠿⣿⣿⣿⣿⡇
   ⠸⠿⠿⠟⠁⠀⠈⠙⠻⠿⠿⠿⠿⠟⠋⠁⠀⠈⠻⠿⠿⠇
'''
import socket #connect to ThinkGear(connection between Mindwave and pc)
import serial #Connect to Arduino
import re     #Make list of datas
import json   #parse the datas we got as Json

TCP_IP='127.0.0.1'
TCP_PORT=13854

def main():

     WTA=serial.Serial('COM9',9600) #Change the COM number with your connected arduino COM Number
     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#initializing the socket
     sock.connect((TCP_IP,TCP_PORT))#connecting to the ThinkGear
     sock.send(b'{"enableRawOutput": true, "format": "Json"}')#set order to geting datas as json
     while True:
         data=sock.recv(1024)

         if data:

             
             ds=data.decode()
             result=re.split('\r',ds)#make list from datas

             for i in range(len(result)):

                try:

                    pdata= json.loads(result[i])#parse the json
                    ddata1=pdata['eSense']# get the value of the eSense key(The value is another josn)
                    ddata = str(ddata1) #Turn it to string for some changes
                    adata=ddata.replace("'","\"") # Turn ' to " 
                    ldata=json.loads(adata)#now parsing the new Json
                    print(int(ldata["attention"]))#getting attention value
                    #check attention level:
                    if ldata["attention"] < 44:

                        WTA.write(b'S')#This code sends the stop message to Arduino

                    elif ldata["attention"] > 90:

                        WTA.write(b'F')#This code sends the forward message to Arduino

                    elif ldata["attention"] > 80:

                        WTA.write(b'L')#This code sends the turn left message to Arduino

                    elif ldata["attention"] > 45:

                        WTA.write(b'R')#This code sends the turn right message to Arduino

                    ReadfromMindWave.close()


                except:

                    #print(0)
                    continue



if __name__ == "__main__":
    main()
