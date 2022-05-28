#ifndef __DISPLAY__
#define __DISPLAY__
#include "Arduino.h"
//https://www.youtube.com/watch?v=iZI1GjCvIiw&t video que vi

class Display
{
public:

  Display(){;}
  
  void setUp();
  
  //Função que mete no display o que quer que esteja guardado
  void display();

  //Man isto mete um int no buffer do display
  void setInt(int num);

  //Man isto mete um float no buffer do dislpay
  void setFloat(float num);

  //igual ao setInt mas os espaços em branco ficam 0
  void setInt0(int num);
  
  //mete as hr nos primeiros dois digitos e mi nos outros dois
  void seTime(int hr, int mi, bool dot = 0);

private:

  //arrays com os pins de A a G e dos Dígitos
  const int pin[8] = {12, 10, 6, 8, 9, 11, 5, 7};
  const int dig[4] = {3, 2, 13, 4};

  //cada bool do array corresponde ao estado do led de um segmento do display
  //cada elemento do num é a forma de um número
  const bool num[10][7] = {{1,1,1,1,1,1,0},{0,1,1,0,0,0,0},{1,1,0,1,1,0,1},{1,1,1,1,0,0,1},{0,1,1,0,0,1,1},{1,0,1,1,0,1,1},
  {1,0,1,1,1,1,1}, {1,1,1,0,0,0,0}, {1,1,1,1,1,1,1}, {1,1,1,1,0,1,1}};

  //array com o número e ponto de cada dígito do display, tipo um buffer
  int numdig[4][2] = {{-1,0}, {-1,0}, {-1,0}, {-1,0}};
};

#endif
