int senserval;
const int analog_0=0;
int l1=13;
int l2=12;
int l3=11;
int l4=10;
int l5=9;
int l6=8;
int l7=7;
int l8=6;
int l9=5;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(l1,OUTPUT);
  pinMode(l2,OUTPUT);
  pinMode(l3,OUTPUT);
  pinMode(l4,OUTPUT);
  pinMode(l5,OUTPUT);
  pinMode(l6,OUTPUT);
  pinMode(l7,OUTPUT);
  pinMode(l8,OUTPUT);
  pinMode(l9,OUTPUT);
}

void loop() {
  
  // put your main code here, to run repeatedly:
senserval=analogRead(analog_0);
if(senserval<30)
{digitalWrite(l1,HIGH);
}
if(senserval>20&&senserval<25)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
}
if(senserval>25&&senserval<30)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
}

if(senserval>30&&senserval<35)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
}


if(senserval>35&&senserval<38)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
}


if(senserval>38&&senserval<40)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
}

if(senserval>40&&senserval<42)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
digitalWrite(l6,HIGH);
}

if(senserval>42&&senserval<44)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
digitalWrite(l6,HIGH);
digitalWrite(l7,HIGH);
}


if(senserval>44&&senserval<46)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
digitalWrite(l6,HIGH);
digitalWrite(l7,HIGH);
digitalWrite(l8,HIGH);

}


if(senserval>46&&senserval<50)
{digitalWrite(l1,HIGH);
digitalWrite(l2,HIGH);
digitalWrite(l3,HIGH);
digitalWrite(l4,HIGH);
digitalWrite(l5,HIGH);
digitalWrite(l6,HIGH);
digitalWrite(l7,HIGH);
digitalWrite(l8,HIGH);
digitalWrite(l9,HIGH);
}


}
