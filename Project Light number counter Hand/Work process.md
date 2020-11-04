# Project Light number counter
Created by Timur Garifullin and Kien Le Trung

## Criteria A: Planing
### Context of the problem
In the Computer Science class we are now styding Data Representation topic. We have already learn how to work with Binary and Hexadecimal counting systems. 
We've also learned about logic gates and k-maps. And now using the knowledge that we gathered from this Unit we need to create the project.
Finished project should be able to show numbers 0-9 using only 7 LED, we should be able to use buttons to control the product. 
Ex. I have 4 buttons and I press 3 of them, our project should be able to read and analyse the signal from the buttons 
The boundaries for this project are following:
* We need Arduino Uno(microcontroller), up to 7 LED lights and up to 4 buttons.

![Photo](https://github.com/TimurGar/Unit-2/blob/main/Project%20Light%20number%20counter%20Hand/IMG_3803.JPG)

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
