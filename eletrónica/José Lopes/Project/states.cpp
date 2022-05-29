#include "states.h"

void States::setUp()
{
  Display::setUp();
  pinMode(pinBt1, INPUT_PULLUP);
  pinMode(pinBt2, INPUT_PULLUP);
  setTime(19,59,40,14,5,2022);
}

//vai mudar de estado se os dois botões estiverem pressed
void States::upDate()
{

  if(!digitalRead(pinBt2) && !digitalRead(pinBt1) && !flag_reset)
  {
    if(st== 4) st = 0;
    else st++;
    flag_reset = 1;
    flag_bt1 = 1;
    flag_bt2 = 1;
    Serial.print("st");
    Serial.println(st);
  }

  else if(flag_reset && digitalRead(pinBt1))
  {
    flag_reset = 0;
    flag_bt1 = 1;
    flag_bt2 = 1;
  }


  switch(st)
  {
    case 0 :
      timeMain();
      break;

    case 1 :
      timeSetup();
      break;

    case 2 :
      timer();
      break;

    case 3:
      dist();
      break;

    case 4:
      sound();
      break;
  }
  display();
}

void States::timeMain()
{
  if(!digitalRead(pinBt1) && !flag_bt1)
  {
    if(st_timemain == 3) st_timemain = 0;
    else st_timemain ++;
    flag_bt1 = 1;
  }

  if(digitalRead(pinBt1) && flag_bt1)
  {
    flag_bt1 = 0;
  }

  if(!digitalRead(pinBt2) && !flag_bt2)
  {
    flag_bt2 = 1;
    st_timemain = 0;
  }
  else{flag_bt2 = 0;}

  switch(st_timemain)
  {
    case(0):
      seTime(hour(), minute(), second()%2);
      break;

    case(1):
      seTime(0,second());
      break;

    case(2):
      seTime(day(), month(), 1);
      break;

    case(3):
      setInt(year());
      break;
  }
}

void States::timeSetup()
{
  setInt0(8888);
  //Serial.println("TIMESETUP");
  int time_stuff[7];
  int i = 0;
  while (Serial.available() > 0)
  {
    time_stuff[i] = Serial.parseInt();
    //Serial.print(time_stuff[i]);  
    i++;
  }
  if(i)
  {
    setTime(time_stuff[0],time_stuff[1],time_stuff[2],time_stuff[3],time_stuff[4],time_stuff[5]);  
    setInt(8888);
  }
}

void States::timer()
{
  //Começar contagem
  if(!digitalRead(pinBt1) && !flag_bt1 && !flag_play)
  {
    //Serial.println("bruh");
    //if(flag_play) stopwatch += millis()-mili;
    flag_play = 1;
    flag_bt1 = 1;
    mili = millis();
  }

  //Parar contagem
  if(!digitalRead(pinBt1) && !flag_bt1 && flag_play)
  {
    //Serial.println("bruh2");
    flag_play = 0;
    flag_bt1 = 1;
    stopwatch_buffer = stopwatch;
  }

  if(!digitalRead(pinBt2) && !flag_bt2)
  {
    //Serial.println("bruh3");
    flag_play = 0;
    flag_bt2 = 1;
    stopwatch = 0;
    stopwatch_buffer = 0;
    mili = 0;
  }

  if(digitalRead(pinBt1) && flag_bt1)
  {
    //Serial.println("bruh4");
    flag_bt1 = 0;
  }

  if(digitalRead(pinBt2) && flag_bt2)
  {
    //Serial.println("bruh5");
    flag_bt2 = 0;
  }

  if(flag_play)
  {
    stopwatch = stopwatch_buffer + millis() - mili;
  }

  //[][]seg . [][][]ms
  if(stopwatch < 60000)
  {
    seTime(stopwatch/1000, stopwatch%1000/10, 1);
    //Serial.println(stopwatch-stopwatch%1000);
  }

  //[][]min . [][]s
  else
  {
    seTime((stopwatch/60000), stopwatch%60000/1000, 1);
  }
  //Serial.println("TEST");
  //Serial.println(stopwatch);
  display();

}


//https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6
void States::dist()
{
  // Clears the trigPin condition
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(pinEcho, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  setInt(int(distance));
}


//vai ser um bocado igual ao dist, lamento o boilerplate
void States::sound()
{
  // Clears the trigPin condition
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(pinEcho, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  if(note != int(distance) / 4)
  {
    note = int(distance) / 4;
    Serial.println(note);

  }
  
  setInt(note);
}
