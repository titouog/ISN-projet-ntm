def setup():
    size(640, 360)
    noSmooth()
    fill(126)
    background(102)
    




def draw():
    if (mouseButton == LEFT):
        stroke(255, 0, 0) 
    elif (mouseButton == RIGHT):
        stroke(0)
    else:
        noStroke()
    s = second()
    
  
    line(mouseX-15, mouseY, mouseX+15, mouseY)
    line(mouseX, mouseY-25, mouseX, mouseY+15) 
    line(s, 0, s, 1)