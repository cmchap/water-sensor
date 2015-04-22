What's It Do? 
============= 
This project is a water sensor. When it detects water, it sends an email and sounds an alarm. When the sensor is dry again, it sends another email and silences the alarm. 

Bill of Materials 
================= 
- Raspberry Pi Type B 
- 10μF capacitor 
- Piezo buzzer that works between 3.3 and 5 volts. 
- small piece of rigid plastic 
- 2 inches of copper or aluminum tape 
- Wire 
- breadboard 
- jumpers (MtM and FtF) 

Tools 
===== 
- soldering iron 
- Keyboard/Screen/ETC get the script onto the Raspberry pi 

The Water Sensor 
================= 

### Making the sensor 
The sensor is made of two pieces of copper tape stuck to a piece of rigid plastic. Put the copper strips parallel, and close together on the same side of the plastic. Solder a lead to each piece of copper. I used speaker wire as the leads because it is cheap to get in long lengths. The longer the leads, the farther from the Raspberry Pi your sensor can be. 

### Orienting and placing the sensor 
In my case, I was trying to determine if water had entered my basement, so I put the copper side down on the floor with a small weight on top of it. When water bridges between the two copper strips, it will close the circuit, and set off the alarm. 

The Code 
========
The code requires you to have a gmail account to send the email. It will store your gmail password in plaintext, which is insecure. I suggest you make a dummy account for your sensor. Name it something cool; get creative. Feel free to modify the code however you'd like. Make the speaker send S.O.S. in morse code. Have the Raspberry Pi update a web server when it detects water. Go nuts.  
The code is also available in a gist: https://gist.github.com/cmchap/5480533

Changelog 
============= 
Enno provided a better design in the comments on Fritzing, so I incorporated it into of this project. 
