int time;
int wait = 1000;

void setup(){
  time = millis();
  
  
}

void draw(){
  if(millis() -  time >= wait){
    //println("tick");
    time = millis();
      for (int colour = 1; colour <= 255; colour++){
        background(colour);
  }
  }
  
  
  
}
