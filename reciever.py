import network
import espnow
import machine

sta = network.WLAN(network.STA_IF) 
sta.active(True)
sta.disconnect()      

esp = espnow.ESPNow()
esp.active(True)


while True:
    _, msg = esp.recv()
    if msg:            
        print(msg)
            
