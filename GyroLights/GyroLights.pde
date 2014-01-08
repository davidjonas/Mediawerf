import ketai.sensors.*;
//Multipliers
int multiplier = 25;
int minusmultiplier = -25;

//Floats for teh rectangle filling
float leftspeed;
float rightspeed;
float topspeed;
float botspeed;


//Sensors
KetaiSensor sensor;
float accelerometerX, accelerometerY, accelerometerZ;

void setup()
{
  sensor = new KetaiSensor(this);
  sensor.start();
  orientation(PORTRAIT);
  textAlign(CENTER, CENTER);
  textSize(36);
  //background(165, 143, 12);
}

void draw()
{
  background(0);
  if (accelerometerX >= 1.5)
  {
    leftspeed = accelerometerX * multiplier;
    
    fill(leftspeed, 0, 0);
    rect(0, 0, width, height);
    println(leftspeed);
  }
  if (accelerometerX <= -1.5)
  {
    rightspeed = accelerometerX * minusmultiplier;
    
    fill(0, rightspeed, 0);
    rect(0, 0, width, height);
    println(rightspeed);
  }
  if (accelerometerY >= 1.5)
  {
    topspeed = accelerometerY * multiplier;
    fill(0, 0, topspeed);
    rect(0, 0, width, height);
    println(topspeed);
  }
  if (accelerometerY <= -1.5)
  {
    botspeed = accelerometerY * minusmultiplier;
    fill(0, botspeed, botspeed);
    rect(0, 0, width, height);
    println(botspeed);
  }
  
}

void onAccelerometerEvent(float x, float y, float z)
{
  accelerometerX = x;
  accelerometerY = y;
  accelerometerZ = z;
}

void mousePressed()
{
  
  
  
}



