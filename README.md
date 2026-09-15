#cardboard-humanoid

#about the project:
Hi and welcome to my first project in the world of elettronics and robotics! As you read in the description, I've just finished building my first robot and it's something really special to me!
To learn how to build a simple robot like this I started learning all the fundamentals of electronics such as blinking an LED, building simple circuits, using a potentiometer etc...
But everything was only on the breadboard, at that point I wanted to bring what I had learned into physical world using cardobard.
Why did I chose cardobard?
When I started thinking about a robot I discovered how important it was to design and print every piece using software like Fusion, but I still have to learn that kind of software, so I thought that building a first prototype using cardboard would be a great way to learn and face problems that could help me understand several important aspects of robotics like center of gravity, cable layout etc...


##features:
This cardboard-humanoid has three simple things that it can do:
first of all I created a web page for my Raspberry Pi Pico 2W from which I can control the entire robot with 4 button: LED ON (turn on all the LEDs), LED OFF (turn off all the LEDs), SERVO ON (move the arms thanks to 2 SG90), SERVO OFF (moves the arms in the opposite direction).

##hardware:
white cardboard to create the entire body, Raspberry Pi Pico 2W,  5 LEDs (2 on the central body, 2 like eyes and 1 in the head), 2 SG90 SERVO MOTORS (to move the arms).

##development:
I started by building 2 small legs (3.5cm in lenght and depht, 5cm in height) to keep the center of gravity low, then I built the central body (19.5cm in lenght and height, 7cm in depth) where inside there is the main breadboard with the Raspberry Pi Pico 2W
Next I built the neck (5cm in depth and lenght, 10cm in height) and head (10cm in lenght, 7cm in height and depth).
To finish, I created the arms (17.5cm in height, 4cm in lenght and 7cm in depth) and a small box (8cm in lenght and depth, 7cm in height ) on the central body which contains a secondary breadboard to control the servo motors because they require a 5V power supply.

##timeline:
#elettronics:
15 JULY: I bought my first electronics kit and I immediately start trying to turn on the Pico 2W's LED. In the same day I blinked my first physical LED.
During the following weeks I learned how to use a button, potentiometer, UART serial communication, photoresistor and more.

##timeline:
#robot:
28 AUGUST: I used cardboard from Amazon packages to create my first robotics leg, however I discarded this solution beacuse it wasn't the best material, as its 1mm thickness wasn't enough to support the weight of the robot.
2 SEPTEMBER: I tried to use a thicker cardboard and everything became possible! During the same day I built the legs and central body with the first 2 LEDs (red and white)
4 SEPTEMBER: I created the neck and head including its mouth and 2 LEDs for the eyes.
8 SEPTEMBER: I created the first arm
11 SEPTEMBER: I finished to create the second arm and the small box on the central body.


##WHAT I LEARNED:
This first project was very useful in my opinion, not because I learned how to create an "attractive robot", but because I learned the foundamentals of robotics using simple materials which allowed me to understand how a simple robot can be built.
Obviously this robot wasn't born to be cool but to be a first simple example for all the other robots I will build, and I'm pretty grateful to have spent two weeks building a robot that I can see one day and say:"WOW, I started from this".


##IMPORTANT NOTES:
All the measurements provided in this README are approximate because the cardboard thickness may vary.
