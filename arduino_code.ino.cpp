#include <Servo.h>


String command;
int val;
Servo myservo;


void setup() {
  myservo.attach(10);
  Serial.begin(9600);
  pinMode(A5,OUTPUT);
  digitalWrite(A5, HIGH);

}

void loop() {
  while (Serial.available()) {
    if (Serial.available() > 0) {
      command = Serial.readStringUntil('\n');
    }

    int servo = command.toInt();
    val = map(servo,640, 0, 0, 180);
    myservo.write(val);
    //Serial.println(c);
    // Serial.println(val);

   
  }
}
