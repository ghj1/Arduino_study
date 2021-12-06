int x;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  
  if (x == 1){
  digitalWrite(22,0);
   }
  if (x == 2){
  digitalWrite(23,0);
   }
  if (x == 3){
  digitalWrite(24,0);
   }
  if (x == 4){
  digitalWrite(25,0);
   }
  if (x = 5){
  digitalWrite(22, 1);
  digitalWrite(23, 1);
  digitalWrite(24, 1);
  digitalWrite(25, 1);
   }
  }
