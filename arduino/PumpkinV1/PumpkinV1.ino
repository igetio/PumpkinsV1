int myPins[] = {2, 3, 4, 5, 6}; // pins for the pumpkins
int inPIR = 10; //pin for the PIR sensor
int serialIn; // stores serial values from Pi
int lastPick = 100; //variable for last dialogue played
int currPick; //current dialogue choosen for playback
boolean  inDialogue = false; //flag for if PI is playing back dialogue chain or not

String readString;
void setup()
{
 // Initializes output pins for pumpkins
  for (int pinNum = 0; pinNum < 5; pinNum++){
    pinMode(myPins[pinNum], OUTPUT);
  }
  pinMode(inPIR, INPUT); // intialize PIR sensor pin
  Serial.begin(9600); // sets up serial connection
  randomSeed(analogRead(0)); // seeds the random function to give more "random" results
}

void loop() {
  
  // Checks if the PIR is seeing motion and the pumpkins are currently not talking
  if (digitalRead(inPIR) == HIGH && inDialogue == false){
     currPick = random(5); // selects which dialogue chain to run
	 
	 // check to make sure that the last chain is not repeated
    if (currPick != lastPick){
     lastPick = currPick;
     Serial.println(currPick); // send choice to Pi
     inDialogue = true;
     }    
   }
  
  if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    } 
	//checks that the length of serial input is 5 ascii characters long.
   if (readString.length() >=5) {
      //checks for an ascii 9 in the serial string to indicate dialogue has ended
     if (readString[0] == '9'){
       inDialogue = false; // sets the dialogue flag back to false
     }
     
	 //loops through serial string and sets pumpkins to either talking or idle
    for (int i = 0; i < 5; i++){ 
      if (readString[i] == '1'){ //sets pumpkin to talking
        digitalWrite(myPins[i], HIGH);
      }else{ //sets pumpkins to idle
        digitalWrite(myPins[i], LOW);
      }
    }
  readString = ""; // blanks out serial string variable after it has been read
  }
}
