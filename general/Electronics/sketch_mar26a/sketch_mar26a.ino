int LEDPURPLE=7;
int LEDRED=6;

int blink_number_PURPLE;
int blink_number_RED;

int time_on_PURPLE;
int time_off_PURPLE;
int time_on_RED;
int time_off_RED;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LEDPURPLE,OUTPUT);
  pinMode(LEDRED,OUTPUT);
  Serial.println("Blinking LED in #");
  Serial.println(" ");

  Serial.println("How many purple blinks?");
  Serial.println(" ");
  while(Serial.available()==0){};
  blink_number_PURPLE=Serial.parseInt();


Serial.println("How many red blinks?");
Serial.println(" ");
  while(Serial.available()==0){};
  blink_number_RED=Serial.parseInt();


  Serial.println("How long Purple on?");
  Serial.println(" ");
  while(Serial.available()==0){};
  time_on_PURPLE=Serial.parseInt();

 Serial.println("How long Purple off?");
  Serial.println(" ");
  while(Serial.available()==0){};
  time_off_PURPLE=Serial.parseInt();

   Serial.println("How long Red on?");
   Serial.println(" ");
   while(Serial.available()==0){};
   time_on_RED=Serial.parseInt();

   Serial.println("How long Red off?");
   Serial.println(" ");
   while(Serial.available()==0){};
   time_off_RED=Serial.parseInt();

  


}

void loop() {
  for(int j=1; j<=blink_number_PURPLE; j=j+1){
    Serial.print("This is the PURPLE LED blinking");
    Serial.print(" ");
    Serial.println(j);
    

    digitalWrite(LEDPURPLE,HIGH);
    delay(time_on_PURPLE);
    digitalWrite(LEDPURPLE,LOW);
    delay(time_off_PURPLE);
  }
    Serial.println(" ");
    
  
  for(int k=1; k<=blink_number_RED; k=k+1){
    Serial.print("This is the RED LED blinking");
    Serial.print(" ");
    Serial.println(k);
    

    digitalWrite(LEDRED,HIGH);
    delay(time_on_RED);
    digitalWrite(LEDRED,LOW);
    delay(time_off_RED);
    
  }   
    Serial.println(" ");
    
  
  }
   
  // put your main code here, to run repeatedly:


