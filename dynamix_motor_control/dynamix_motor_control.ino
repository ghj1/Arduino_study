#include <DynamixelWorkbench.h>

DynamixelWorkbench dxl_wb;

void setup() {
  // put your setup code here, to run once:
  dxl_wb.begin("",1000000);
  
  dxl_wb.ping(1);
  dxl_wb.ping(2);
  
  dxl_wb.jointMode(1);
  dxl_wb.jointMode(2);

  Serial.begin(115200);
  
  
}

String control;
void loop() {
  // put your main code here, to run repeatedly:
  
  while(!Serial.available()){
    control = Serial.readString();
    
    if(control == "s"){
    dxl_wb.goalPosition(1,0);
    dxl_wb.goalPosition(2,0);
      Serial.println("stop");
      }
    else if(control == "f"){
    dxl_wb.goalPosition(1,2000);
    dxl_wb.goalPosition(2,2000);
      Serial.println("forward");
      }
    else if(control == "r"){
    dxl_wb.goalPosition(1,90);
    dxl_wb.goalPosition(2,90);
      Serial.println("right");
      }
    else{
    
      }
  }
//  
//  dxl_wb.goalPosition(1,0);
//  dxl_wb.goalPosition(2,0);
//  delay(2000);
//  dxl_wb.goalPosition(1,2000);
//  dxl_wb.goalPosition(2,2000);
//  delay(2000);
}
