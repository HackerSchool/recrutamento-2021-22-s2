#ifndef __STATES__
#define __STATES__
#include "Arduino.h"
#include "display.h"
#include <TimeLib.h>


//esta classe trata dos estados do display
class States : public Display
{
public:
  States(){;}

  void setUp();

  //vai mudar de estado se os dois botões estiverem pressed
  void upDate();

  //estado do tempo (hihihi) clicas no botão 1 dá cycle pelas horas, segundos, dia do mes ano
  void timeMain();

  //liga em serial ao processing à espera das horas atualizadas
  void timeSetup();

  //não sei porque é que isto se chama timer quando na realidade é um stopwatch
  void timer();

  //distance aparece no display ig
  void dist();

  //toca um sonzinho no processing cuja frequcencia varia com a distância
  void sound();

private:

  int pinEcho = 18;
  int pinTrig = 19;
  int pinBt1 = 15;
  int pinBt2 = 16;
  int st = 0;
  int st_timemain = 0;

  //stopwatch
  int mili = 0;
  long int stopwatch = 0;
  long int stopwatch_buffer = 0;

  //distance
  float distance;
  long duration;

  //sound
  int note = 0; //isto vai guardar tipo a nota musical e só quando muda é que manda por serial, para combater o lag
  
  bool flag_reset = 0;
  bool flag_bt1 = 0;
  bool flag_bt2 = 0;
  bool flag_play = 0;

};

#endif
