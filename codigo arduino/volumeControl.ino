int const potPin = A0;
int potVal;
int vol;


void setup() 
{
  Serial.begin(9600);  
}

void loop() 
{
  potVal = analogRead(potPin);//potenciometro
  vol = map(potVal,0,1023,61,0);//volumen PC
  Serial.println(vol);
  delay(100);
}
