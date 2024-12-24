import network
from machine import Pin
import espnow
import utime


sta = network.WLAN(network.STA_IF)  
sta.active(True)

esp = espnow.ESPNow()
esp.active(True)

peer = b'\xe4e\xb8\x83V\xf4' #The address of the reciever, change with every esp
esp.add_peer(peer)
while(1):
    
    message = "hi"
    print("Sending command :",message)
    esp.send(peer, message)
    utime.sleep(5)

        
