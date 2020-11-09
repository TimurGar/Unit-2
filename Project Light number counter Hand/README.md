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

### Justification of the solution

We want to create a number counter that is looks like a palm. We will use 6 LEDs, each LED on each finger and the last one in the center of a palm. 
To conrol it, we will use 4 buttons and we are going to use Binary system to count. We are going to use wood and laser cutter to create the palm.


## Criteria for Success
1. Provides clear output(number) to the user by using LEDs(Usability)
1. There are no bugs in the code
1. User is be able to understand what number it is even in the darkness
1. The main body of the project is made out of wood with the help of laser cutter.

## Criteria B: Design
### The sketches of our idea:
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3803.JPG" alt = "The_sketches_of_our_idea" width="700">

### System diagram
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3827.JPG" alt = "System_diagram" width="700">

### Flow diagram
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/Project%20Light_Number_Counter_Kien%20and%20Timur.png)

### Design of a palm(circles represent LEDs)
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/Screen%20Shot%202020-11-09%20at%2014.42.58.png" height="700">

## Criteria C: Development
After we thought over of all the aspects of our idea we started realising it.
First, we created a truth table for the number counter.
<img src="https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3807.jpg" height="700">

Then based on the truth table, we created k-maps for each LEDs(A-E).
<img src="IMG_3808.JPG" height="700">

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