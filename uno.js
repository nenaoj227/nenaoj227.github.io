/* This is a tutorial on how to make a ball bounce */
// Author : Nena Ojukwu

int x; int y; int r; int Vx; int Vy;
void setup(){
  size(600,700);
  x=100;
  y=200;
  r=30;
  Vx = 6;
  Vy = 5;
}

void draw(){
  background(0); //starts each loop with a fresh slate
  circle(x,y,r);
  updatePosition();
  bounce();
}

void bounce(){
  if (y + Vy <0){
    Vy = -Vy;
  }
  if (x + Vx < 0 ){
    Vx = -Vx;
  }
  if (x< width - r/2){
    Vx *= -1;
  }
  if (y> height - r/2){
    Vy *= -1;
  }
  
}
    
    
    
void updatePosition(){
  x += Vx;
  y += Vy;
}
  