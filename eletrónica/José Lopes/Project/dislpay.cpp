#include "display.h"

void Display::setUp()
{
  for(int i = 0; i < 8; i++)
  {
    pinMode(pin[i], OUTPUT);
  }
  for(int i = 0; i < 4; i++)
  {
    pinMode(dig[i], OUTPUT);
  }
}

//Função que mete no display o que quer que esteja guardado
void Display::display()
{
  digitalWrite(dig[0], HIGH);
  digitalWrite(dig[1], HIGH);
  digitalWrite(dig[2], HIGH);
  digitalWrite(dig[3], HIGH);

  for(int i = 0; i < 4; i++)
  {
    int n = numdig[i][0];
    if(n != -1)
    {
      digitalWrite(dig[i], LOW);

      //desenhar a letra
      for(int i = 0; i < 7; i++)
      {
        if(num[n][i] != digitalRead(pin[i])) digitalWrite(pin[i], num[n][i]);
        //else digitalWrite(pin[i], LOW);
      }

      //tratar do ponto
      if(numdig[i][1] == 1) digitalWrite(pin[7], HIGH);
      else digitalWrite(pin[7], LOW);

      delay(5);
      digitalWrite(dig[i], HIGH);
    }

  }

}

void Display::setInt(int num)
{
  for(int i = 0; i < 4; i++)
  {
    numdig[i][0] = -1;
    numdig[i][1] = 0;
  }
  for(int i = 3; i >= 0; i--)
  {
    if(num < 1)
    {
      numdig[i][0] = -1;
    }
    else
    {
      numdig[i][0] = num %10;
      num/=10;
    }
  }
}
void Display::setFloat(float num)
{
  int dot = 3;

  for(int i = 0; i < 4; i++)
  {
    numdig[i][0] = -1;
    numdig[i][1] = 0;
  }

  while(num < 1000)
  {
    num *= 10;
    dot --;
  }

  setInt(int(num));
  numdig[dot][1] = 1;
}

void Display::setInt0(int num)
{
  for(int i = 0; i < 4; i++)
  {
    numdig[i][0] = -1;
    numdig[i][1] = 0;
  }
  for(int i = 3; i >= 0; i--)
  {
    if(num < 1)
    {
      numdig[i][0] = 0;
    }
    else
    {
      numdig[i][0] = num %10;
      num/=10;
    }
  }
}

void Display::seTime(int hr, int mi, bool dot)
{
  for(int i = 0; i < 4; i++)
  {
    numdig[i][1] = 0;
  }

  numdig[1][0] = hr%10;
  numdig[0][0] = (hr/10)%10;
  numdig[3][0] = mi%10;
  numdig[2][0]= (mi/10)%10;

  if(dot) numdig[1][1] = 1;


}
