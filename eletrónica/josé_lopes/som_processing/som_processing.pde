import processing.sound.*;
import processing.serial.*;

//source: https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all

Serial myPort;  // Create object from Serial class
String val;     // Data received from the serial port
SinOsc sine;
Integer state;

void setup()
{
 
  String portName = Serial.list()[0]; //change the 0 to a 1 or 2 etc. to match your port
  sine = new SinOsc(this);
  myPort = new Serial(this, portName, 115200);
}

void draw()
{
  if ( myPort.available() > 0) // If data is available,
  {  
    val = myPort.readStringUntil('\n');  // read it and store it in val
    println(val);
    switch(val)
    {
      case "st0\r\n":
        state = 0;
        sine.stop();
        break;
      case "st1\r\n":
        timeSetup();
        state = 1;
        break;
      
      case "st2\r\n":
        state = 2;
        break;
      
      case "st3\r\n":
        state = 3;
        break;
        
      case "st4\r\n":
        state = 4;
        sine.play();

        break;
      
      default:
        if(state == 4)
        {
          soundPlay(val.substring(0, val.length() - 2));
        }
        break;
    }
    
    //que cena parva https://www.javatpoint.com/string-comparison-in-java
  }

  
}


//https://discourse.processing.org/t/multiple-values-from-processing-to-arduino-through-serial-port/4152/2
void timeSetup()
{
  myPort.write(hour() + ";" + minute() + ";" + second() + ";" +day()+ ";" + month()+ ";" + year());
  
  println("Time Sent");

}


//isto recebe um número a começar em 1, e associa a 1 a nota A = 440Hz, e vai em intervalos de 1/12 dessa nota 
void soundPlay(String dist)
{
  //https://stackoverflow.com/questions/5585779/how-do-i-convert-a-string-to-an-int-in-java odeio java
  try
  {
    int note = Integer.parseInt(dist);
    float freq = 440 * (1 + ((float)note-1) /12);
    print(freq);
    sine.freq(freq);
  } 
  
  catch (NumberFormatException e)
  {
    //print("huh?");
  }
  

}
