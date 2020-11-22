# Project Light number counter
Created by Timur Garifullin and Kien Le Trung

## Criteria A: Planing
### Context of the problem
In the Computer Science class we are styding Data Representation topic. We have already learned how to work with Binary and Hexadecimal counting systems. 
We've also learned about logic gates and k-maps. And now using the knowledge that we gathered from this unit to crete a project.
Finished project should be able to show numbers 0-9 using only 7 LED and by controlled by up to 4 buttons. 


Example: I have 4 buttons and I press 3 of them, our project should be able to read and analyse the signal from the buttons and turn on correct LEDs.


Our tasks for this project are following:
* Use up to 7 LEDS and up to 4 buttons
* Use Arduino(microcontroller)
* Create a documentation on Github
* Create sketches of ideas
* Create Flow diagram
* Create truth table
* Create K-maps
* We can also use laser cutter to create a body for our project

### The sketches of our idea:
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3803_new.jpeg" alt = "The_sketches_of_our_idea" width="700">
Fig.1 Our sketch for how the buttons will turn on the lights and values associate with the lights

### Justification of the solution

We want to create a number counter that is looks like a palm. We will use 6 LEDs, each LED on each finger and the last one in the center of a palm. 
To conrol it, we will use 4 buttons and we are going to use Binary system to count. We are going to use wood and laser cutter to create the palm.


## Criteria for Success
1. The display should count from 0-9.
1. A table showing each number 0-9 and the corresponding LEDs is included.
1. A table showing the operations of the buttons and number 0-9 is included.
1. The display uses maximum 7 LEDs and 4 buttons.
1. The main body of the project is made out of wood with the help of laser cutter.

## Criteria B: Design


### System diagram
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3827.JPG" alt = "System_diagram" width="700">
Fig.2 System digram of our program

### Flow diagram
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/Project%20Light_Number_Counter_Kien%20and%20Timur%20(1)%20(1).png)
Fig.3 Flow diagram of how the action of pushing buttons will turn on the light

### Design of a palm(circles represent LEDs)
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/Screen%20Shot%202020-11-09%20at%2014.42.58.png" height="700">


### A table showing the operations of the buttons and number 0-9
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/Number_counter_table.png" height="700">


## Criteria C: Development
### Truth table
After we thought over of all the aspects of our idea we started realising it.
First, we created a truth table for the number counter.
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3807.jpg" height="700">
Fig.4 Truth tables of our program

### K-maps
Then based on the truth table, we created K-maps for each LEDs(A-E).
<img src="New%20IMG_3808.JPG" height="700">
Fig.5 K-maps of our program

### Project circuit and code
After that, we used equations that we got from K-maps to create a program for our project.
To test if our program is working we assempled a circuit in TinkerCad and run the program there.
<img src="Screen%20Shot%202020-11-09%20at%2019.09.09.png" weight="800">

```.py
unsigned long last_time;

int button_x_port = 4; 
int button_y_port = 5; 
int button_z_port = 6; 
int button_w_port = 7; 

int light_a = 13;
int light_b = 8;
int light_c = 9;  
int light_d = 10;
int light_e = 11;
int light_f = 12;

int button_x_value = 0;
int button_y_value = 0;
int button_z_value = 0; 
int button_w_value = 0;

void setup()
{
  pinMode(light_a, OUTPUT);
  pinMode(light_b, OUTPUT);
  pinMode(light_c, OUTPUT);
  pinMode(light_d, OUTPUT);
  pinMode(light_e, OUTPUT);
  pinMode(light_f, OUTPUT); 
  Serial.begin(9600);
}

void loop()
{
  
  button_x_value = digitalRead(button_x_port);
  button_y_value = digitalRead(button_y_port);
  button_z_value = digitalRead(button_z_port);
  button_w_value = digitalRead(button_w_port);
  
 //a
 int eq_a = ((!button_y_value)&&(!button_z_value)&&(!button_w_value))||((button_x_value)&&(!button_y_value)&&(!button_z_value))||((!button_x_value)&&(button_y_value)&&(button_z_value));
  digitalWrite(light_a,eq_a);
 //b
 int eq_b = ((button_x_value)&&(!button_y_value)&&(!button_z_value))||((!button_x_value)&&(button_y_value))||((!button_x_value)&&(!button_y_value)&&(button_w_value))||((!button_x_value)&&(!button_y_value)&&(button_z_value));
  digitalWrite(light_b,eq_b);

  
 //c
 int eq_c = ((!button_x_value)&&(button_y_value)&&(!button_z_value))||((button_x_value)&&(!button_y_value)&&(!button_z_value))||((!button_x_value)&&(!button_y_value)&&(button_z_value))||((!button_x_value)&&(button_y_value)&&(button_w_value));
 digitalWrite(light_c,eq_c);

 //d
 int eq_d = (!button_x_value)&&(button_y_value)&&(!button_z_value)||(button_x_value)&&(!button_y_value)&&(!button_z_value)||(!button_x_value)&&(!button_y_value)&&(button_z_value)&&(button_w_value);
 digitalWrite(light_d,eq_d); 

 //e 
 int eq_e = (!button_x_value)&&(button_y_value)&&(!button_z_value)||(button_x_value)&&(!button_y_value)&&(!button_z_value)&&(button_w_value);
 digitalWrite(light_e,eq_e); 
 
 //f                    
 int eq_f = (!button_x_value)&&(button_y_value)&&(!button_z_value)&&(button_w_value);
 digitalWrite(light_f,eq_f);  
 Serial.print(eq_a);
 Serial.print(eq_b);
 Serial.print(eq_c);
 Serial.print(eq_d);
 Serial.print(eq_e);
 Serial.println(eq_f); 
}
```
# Criteria E: Evaluation
| Test                                                                                          | Expected Outcome                                                                                                                                                                                                                   | Met?          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Criteria 1: See if our product count number 0-9.                                              | If you pressed the button's combination for a number,  the display shows a pattern for that number  (customers can do this while looking at our  "Button Operation Table") Ex: Click no buttons-> no light turned on (value=0); Click the green button-> turn on 1 light (value=1); Click the red button-> turn on 2 lights (value=2)... |   Yes            |
| Criteria 2: See if we provided you with a table showing LED  sequences for each number 0-9    | You are able to see a table showing patterns of LEDs for each number 0-9 that is  presented.                                                                                                                                       |       Yes        |
| Criteria 3: See if we provided you with a table showing buttons sequences for each number 0-9 | You are able to see a table showing patterns of buttons (4 buttons with 4 colors: yellow, blue, red, green) for each number 0-9 that is presented.                                                                                                                                     |       Yes        |
| Criteria 4: Check if our product uses maximum of 7 LEDs and 4 buttons.                        | You will see that our product uses no more than 7 LEDs  and 4 buttons.                                                                                                                                                             |   Yes            |
| Criteria 5: See if our product contains a wood-body.                                          | You will see that our product's body is created from wood.                                                                                                                                                                         |    Yes           |

### Finished product
Next, we laser cutted the palm and assembled everthying.
and this is our final product:
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3857.JPG" width="700">
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3858.JPG" width="700">

### Videos of working project

Day time test:
https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/New_CS.mov

Dark time test:
https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3855.MOV

