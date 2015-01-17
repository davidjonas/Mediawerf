
Wind windSensor;
String statusStr = "";
int windSpeed = 0;
String windDirection = "";
boolean isConnected = false;

// the setup is only executed once at the startup 
void setup() {
  
  size(displayWidth, displayHeight);

  //initialize windSensor
  windSensor = new Wind(true);
  
  //initializing graphics
  textSize(18);
  smooth(); 
}


void draw()
{
  //we clean the screen with a background color
  background(60);
  //we choose the text color 
  fill(200);
  //we print the wind direction and screen on the screen
  statusStr = (isConnected) ? "connected, wind direction="+windDirection + ", speed="+windSpeed : "not connected";
  text(statusStr, 20,40);
}

 

