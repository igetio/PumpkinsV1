int myPins[] = {2, 3, 4, 5, 6};
int inPIR = 10;
int serialIn;
int lastPick = 100;
int currPick;
boolean  inDialogue = false;

String readString;
void setup()
{
  for (int pinNum = 0; pinNum < 5; pinNum++){
    pinMode(myPins[pinNum], OUTPUT);
  }
  pinMode(inPIR, INPUT);
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  
  
  if (digitalRead(inPIR) == HIGH && inDialogue == false){
     currPick = random(5);
    if (currPick != lastPick){
     lastPick =  currPick;
     Serial.println(currPick);
     inDialogue = true;
     }    
   }
  
  if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    } 
   if (readString.length() >=5) {
      //Serial.println(readString);
     if (readString[0] == '9'){
       inDialogue = false;
     }
     
     for (int i = 0; i < 5; i++){
    
    //Serial.println(readString[i]); 
    
    if (readString[i] == '1'){
      digitalWrite(myPins[i], HIGH);
    }else{
     digitalWrite(myPins[i], LOW);
    }
  }
  readString = "";
  }
}
