#include <TimeLib.h>
#include "display.h"
#include "states.h"

int pinEcho = 18;
int pinTrig = 19;

int t = 0;
float ni = 0;
long duration;
float distance;
float dists[20];
States state;

void setup()
{
  state.setUp();
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Native USB only
  }
  //Serial.println("Goodnight moon!");

  pinMode(pinTrig, OUTPUT);
  pinMode(pinEcho, INPUT);



  setTime(19,59,40,14,5,2022);
}

void loop() {

  state.upDate();


}
