# Python/C - Arduino RC Car

## Sections 
- [Description](#description)
    - [Media](#media)
- [Getting Started](#getting-started)
    - [Dependencies/Libraries](#dependencies/libraries)
    - [Installing](#installing)
    - [Setting Up](#setting-up)
    - [Executing](#executing)
- [Author](#author)
- [License](#license)

---
## Description
This RC car project was made using an arduino, a small microcontroller, along with other modules such as the HC-06 bluetooth module and the L298N motor drive. The car's frame was entirely 3D printed with a custom design and a python script was develloped to control teh car using wither WSAD keyboard keys or by pressing/holding the buttons on the GUI. 

<br />

**Future Plans:**
 - Add a camera onto the top of the car frame which cna then be used to stream directly to the Python GUI. 
 - Incorporate OpenCV to add semi autonomous functions which as wall avoidance and the ability to follow a line set on the ground. 


 ### Media
 Images of the finished RC car can be seen below.
 
<br />
<img src="Images\car_front.jpeg" width=400> 
<img src="Images\car_side.jpeg" width=400>  <br />
<img src="Images\inside_front.jpeg" width=400> 
<img src="Images\inside_side.jpeg" width=400> 
<img src="Images\inside_top.jpeg" width=800> 





---
## Getting Started

### Dependencies/Libraries
- Python >= 3.6.0
- pyserial == 8.0.22 `pip install pyserial`
- [Arduino IDE](https://www.arduino.cc/en/software) 
- Mac/Windows OS

<br />

### Installing 
```bash
$ git clone https://github.com/JugalBili/Arduino-RC-Car-With-GUI
```
Or you can download the zip directly from github. 

<br />


### Setting Up
First, download the Arduino IDE [here](https://www.arduino.cc/en/software), connect your arduino to your computer, then copy and upload the contents of the `Motor_Control.ino` file found in the Motor_Control folder. 
> **IMPORTANT NOTE:** You may need to change the pin numbers in the program respective to the pin numbers which you have connected your motor drive to. 

In order to make use of the bluetooth capabilities, you will first need to pair your HC-05/HC-06 bluetooth module to your computer. The default pairing password should be 1234, or look at your specefic models instruction sheet. 

Next, on line 10 in `GUI_Controller.py`, you will need to enter the COM port which your bluetooth module has conencted to on your computer. TO find which COM port you module has connected to, on Windows 10, follow the steps below: 
 1. Open control panel and click on "Devices and Printers"
 2. Right click on your bluetooth module device and select properties
 3. Goto the services tab and write down the COM port listed below in the code where it says "COM4"

<br />


### Executing
To execute to program, open the zip file into an IDE of your choice, or use the following in the termial: 
```bash
python GUI_Controller.py
```
> **Make Sure** to run the command inside the Motor_Control folder

To run the arduino code, open the Motor_Controlelr.ino file in the arduino software. 

---
## Authors 
**Jugal Bilimoria and Henry Gu**
<br />January 7th 2021

<br />This project was made as an investigations into bluetooth modules, arduino microcontrollers, and motors with Python integration. 

---
## License 


MIT License

Copyright (c) 2020 Jugal Bilimoria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.