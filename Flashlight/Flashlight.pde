import ketai.camera.*;
KetaiCamera cam;

int alpha = 0;
int speed = 5;
boolean white = false;

void setup() {
  //size(1600, 900);
  noStroke();
  frameRate(30);
  background(0);
  cam = new KetaiCamera(this, 480, 800, 24);
  cam.start();
  orientation(PORTRAIT);
}

void draw() 
{
  background(0);
  fill(alpha);
  rect(0, 0, width, height);
  alpha+=speed;
  if (alpha >= 256 || alpha <= 0)
  {
    if (cam.isFlashEnabled())
      cam.disableFlash();
    else
      cam.enableFlash();
    speed*=-1;
  }
  //println(speed);
  //println(alpha);
  println(mouseY);
}

void mousePressed()
{
  if (mouseY > 400)
  {
    if (speed >= 0)
      {
        speed++;
      }
      else
      {
        speed--;
      }
  }
  if (mouseY < 400)
  {
    if (speed >= 0)
    {
      speed--;
    }
    else
    {
      speed++;
    }
  }
  
}


