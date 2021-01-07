int incomingByte;      // a variable to read incoming serial data into
auto builtInLED = LED_BUILTIN; 

//Pin numbers for motors
int motorL1 = 2;
int motorL2 = 3;
int motorR1 = 6;
int motorR2 = 7; 


void setup() {
  // initialize serial communication:
  Serial.begin(9600);

  // initialize the LED pin as an output:
  pinMode(builtInLED, OUTPUT);

  //Initializes motor pins as output
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT);
  pinMode(motorR1, OUTPUT);
  pinMode(motorR2, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();


    //FORWARDS
    if (incomingByte == 'w') {
      digitalWrite(builtInLED, HIGH);
      digitalWrite(motorL1, HIGH);
      digitalWrite(motorL2, LOW);
      digitalWrite(motorR1, LOW);
      digitalWrite(motorR2, HIGH);
    }

    //BACKWARDS
    else if (incomingByte == 's') {
      digitalWrite(builtInLED, HIGH);
      digitalWrite(motorL1, LOW);
      digitalWrite(motorL2, HIGH);
      digitalWrite(motorR1, HIGH);
      digitalWrite(motorR2, LOW);
    }

    //RIGHT
    else if (incomingByte == 'a') {
      digitalWrite(builtInLED, HIGH);
      digitalWrite(motorL1, HIGH);
      digitalWrite(motorL2, LOW);
      digitalWrite(motorR1, HIGH);
      digitalWrite(motorR2, LOW);
    }

    //LEFT
    else if (incomingByte == 'd') {
      digitalWrite(builtInLED, HIGH);
      digitalWrite(motorL1, LOW);
      digitalWrite(motorL2, HIGH);
      digitalWrite(motorR1, LOW);
      digitalWrite(motorR2, HIGH);
    }
  }
  else{
      digitalWrite(builtInLED, LOW);
      digitalWrite(motorL1, LOW);
      digitalWrite(motorL2, LOW);
      digitalWrite(motorR1, LOW);
      digitalWrite(motorR2, LOW);
    }
    //Delays the readtime for next command by 50ms 
    delay(50);
    
}
