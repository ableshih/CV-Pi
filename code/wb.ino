#include <AFMotor.h>
//#include <AFMotor.h>
#include <Wire.h> //BH1750 IIC Mode 
#include <math.h> 
#include <Servo.h> 
Servo servo;
int angle;
//char ch;
int Sen1 = 0x23; //setting i2c address
int Sen2 = 0x5C;
int val;
byte buff[2];
//int angle;
char ch;
const int stp=A0;      
const int enp=A1; 

AF_Stepper motor(48, 1);
AF_DCMotor motora(1);
void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");
  Wire.begin();
servo.attach(10);
  motor.setSpeed(800);  // 10 rpm   
  motora.run(RELEASE);
  motor.step(0, FORWARD, INTERLEAVE);
  // motor.run(FORWARD);      // turn it on going forward
   //motor.run();
   //motor.run(BACKWARD);
   pinMode(stp, INPUT);     
   pinMode(enp, INPUT);     
  delay(1000);
   if(stp==1)
   {
    Serial.println("stp");
    motor.step(100, BACKWARD, DOUBLE);
    }

      val=digitalRead(stp);  
  if(val==HIGH)   
     {
    Serial.println("stp");
    motor.step(100, BACKWARD, DOUBLE);
    }
   // Serial.println("stp1");//digitalWrite(led,HIGH); 
  else          
    Serial.println("stp0");//digitalWrite(led,LOW); 
}

void loop() {
        val=digitalRead(stp);  
  if(val==HIGH)   
    Serial.println("stp1");//digitalWrite(led,HIGH); 
  else          
    Serial.println("stp0");//digitalWrite(led,LOW); 
loopiic();
  if(Serial.available())
  {
     ch=Serial.read();
     Serial.println(ch);            
  } 
  if(ch=='a')


  {
  Serial.println("Single coil steps");
  motor.step(100, FORWARD, SINGLE); 
  motor.step(100, BACKWARD, SINGLE);
  }
else if(ch=='b')
  {
  Serial.println("Double coil steps");
  motor.step(100, FORWARD, DOUBLE); 
  motor.step(100, BACKWARD, DOUBLE);
}
else if(ch=='0')
  {
  Serial.println("Double coil steps");
  motor.step(10, FORWARD, DOUBLE); 
  //motor.step(100, BACKWARD, DOUBLE);
}
else if(ch=='1')
  {
  Serial.println("Double coil steps");
  //motor.step(10, FORWARD, DOUBLE); 
  motor.step(100, BACKWARD, DOUBLE);
}
else if(ch=='c')
{
  Serial.println("c1 Interleave coil steps");
  delay(1000);
  motor.step(3000, FORWARD, DOUBLE); //INTERLEAVE
  Serial.println("c2 Interleave coil steps");
  delay(1000);
  motor.step(3000, BACKWARD, DOUBLE);
}
else if(ch=='d')
{
#if 1//def MICROSTEPPING
  Serial.println("Micrsostep steps");
  motor.step(100, FORWARD, MICROSTEP); 
  motor.step(100, BACKWARD, MICROSTEP); 
#endif
}
 else if(ch=='p')
  {
    for(angle=5;angle<=180;angle++)
    { 
      servo.write(angle);
      delay(10);
    }
    for(angle=180;angle>=5;angle--)
    { 
      servo.write(angle);
      delay(10);
    }   
  }  
    else if(ch=='l')
     servo.write(90);  
}
void loopiic()
{
  int i;
  uint16_t val1=0, val2=0;
  
  BH1750_Init(Sen1);
  delay(200);

  if(2==BH1750_Read(Sen1))
  {
    val1=((buff[0]<<8)|buff[1])/1.2;
    Serial.print(val1,DEC);     
    Serial.println("[lx]"); 
  }
  delay(200);
  
  if(2==BH1750_Read(Sen2))
  {
    val2=((buff[0]<<8)|buff[1])/1.2;
    Serial.print(val2,DEC);     
    Serial.println("[lx]/n"); 
  }
  delay(200);
  //Serial.print("bbbb"); 
}

int BH1750_Read(int address) //
{
  int i=0;
  Wire.beginTransmission(address);
  Wire.requestFrom(address, 2);
  while(Wire.available()) //
  {
    buff[i] = Wire.read();  // receive one byte
    i++;
  }
  Wire.endTransmission();  
  return i;
}

void BH1750_Init(int address) 
{
  Wire.beginTransmission(address);
  Wire.write(0x10);//1lx reolution 120ms
  Wire.endTransmission();
}
/*
 * 
 * 
 * http://zhongbest.com/2016/09/01/%E7%94%B5%E6%9C%BA%E9%A9%B1%E5%8A%A8%E6%9D%BFl293d/
[L293D接腳說明]
• 1 Enable 1-2：作為左半邊IC控制用。當這個Pin為高電壓時，左半邊IC可作用，反之，低電壓時，左半邊IC無作用。
• 2 INPUT 1：當這個Pin為高電壓時，電流會流出至Output 1。
• 3 OUTPUT 1：這個Pin要接到終端馬達的一個接腳。
• 4,5 GND：接地。
• 6 OUTPUT 2：這個Pin要接到終端馬達的一個接腳。
• 7 INPUT 2, 當這個Pin為高電壓時，電流會流出至Output 2。
• 8 VC：供給給馬達使用的電壓，如果要驅動的馬達是12V，那就要供給這個Pin 12V直流電。
• 9 Enable 3-4：作為右半邊IC控制用。當這個Pin為高電壓時，右半邊IC可作用，反之，低電壓時，右半邊IC無作用。
• 10 INPUT 3,：這個Pin為高電壓時，電流會流出至Output 3。
• 11 OUTPUT 3：這個Pin要接到終端馬達的一個接腳。
• 12,13 GND：接地。
• 14 OUTPUT 4：這個Pin要接到終端馬達的一個接腳。
• 15 INPUT 4：當這個Pin為高電壓時，電流會流出至Output 4。
• 16 VSS：提供給IC的電源，這個Pin要供給5V電壓。


 数字引脚2和13可用。

 下面的引脚只有在下面提到的直流或者步进电机工作时才会被用到

    数字引脚11: 1号直流电机或者1号步进电机

    数字引脚3: 2号直流电机或者1号步进电机

    数字引脚5: 3号直流电机或者2号步进电机

    数字引脚6：4号直流电机或者2号步进电机

 下面的引脚只有在下面的直流或者步进电机工作时才会被用到

    数字信号4,7,8,和12通过74hc595（serial-to-parallel）来驱动直流或者步进电机

 下面的引脚只有在舵机工作时才会被用到

    数字信号9：1号舵机

    数字信号10： 2号舵机
*/
