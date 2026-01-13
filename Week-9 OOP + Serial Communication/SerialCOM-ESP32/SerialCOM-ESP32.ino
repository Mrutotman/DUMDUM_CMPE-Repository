void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');
    msg.trim();
    Serial.println(msg);
  }
}

