import network 
import time
import machine
import socket



routername = ""
password = ""


#setting the Pin
led = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(15, machine.Pin.OUT)
led4 = machine.Pin(16, machine.Pin.OUT)
led5 = machine.Pin(18, machine.Pin.OUT)
servo1 = machine.PWM(machine.Pin(14))
servo2 = machine.PWM(machine.Pin(13))


servo1.freq(50)
servo2.freq(50)


def muovi_servo(posizione_iniziale, posizione_finale, durata):
    passi = 100
    intervallo = durata/passi
    for i in range(passi+1):

        posizione = posizione_iniziale+(posizione_finale-posizione_iniziale)*i/passi
        servo1.duty_u16(int(posizione))
        servo2.duty_u16(int(posizione))

        time.sleep(intervallo)





connection = network.WLAN(network.STA_IF)
connection.disconnect()
connection.active(True)
connection.connect(routername, password)

def WebPage():
    if led.value() == 1:
        gpio_state = 'On'
    else:
        gpio_state = 'OFF'

    html = """
    <html>
        <head>
            <title>Pico 2W Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}
                p{font-size: 1.5rem;}
                .button{display: inline-block; background-color: #4286f4; border: none;border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                .button2{background-color: #f44336;}
                .button3{background-color: #FFD700}
            </style>
        </head>
        <body> <h1>CUBOT REMOTE CONTROLLER</h1> 
          <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
          <p><a href="/?led=on"><button class="button">ON</button></a></p>
          <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
          <p><a href="/?servo1=on"><button class="button button3">SERVO ON</button></a></p>
          <p><a href="/?servo1=off"><button class="button button3">SERVO OFF</button></a></p>
          <p><a href="/?servo1=disabled"><button class="button button3">DISABLED SERVO</button></a></p>


        </body>
    </html>
    """

 
    return html

#checking del wifi
while connection.isconnected() == False:
    print("Connect to a wireless network")
    time.sleep(10)
print("Connected!, your informations are:", connection.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #indirizzi IPv4 e comunicazione tramite TCP
s.bind(("",80))
s.listen(5)

try:
    while True:
        conn, addr = s.accept()
        req = conn.recv(1024)
        req = str(req)
        print("Connect = %s" %req)
        led_on = req.find("/?led=on")
        led_off = req.find("/?led=off")
        servo1_off = req.find("/?servo1=off")
        servo1_on = req.find("/?servo1=on")
        disabled_servo = req.find("/?servo1=disabled")

        if "/?led=on" in req:
            print("LED ON")
            led.value(1)
            led2.value(1)
            led3.value(1)
            led4.value(1)
            led5.value(1)

        elif "/?servo1=on" in req:
            muovi_servo(1536, 2500, 5)
            print("SERVO ON")

        elif "/?servo1=off" in req:
            muovi_servo(2500, 1536, 5)
            print("SERVO OFF")

        elif "/?servo1=disabled" in req:
            servo1.duty_u16(0)
            servo2.duty_u16(0)

            print("DISABLED SERVO")





        elif "/?led=off" in req:
                print("LED OFF")
                led.value(0)
                led2.value(0)
                led3.value(0)
                led4.value(0)
                led5.value(0)
                


                   
        



        if led.value() == 1:
            gpio_state = "On"
        else:
            gpio_state = "Off"
        response = WebPage()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
        conn.close()
except:
    conn.close()
    s.close()
    pass        
