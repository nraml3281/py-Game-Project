
from gamelib import*

game = Game(800,600,"Game",2)

bk = Image("scaryImages\\background.png",game)
bk.resizeTo(game.width,game.height)

sonicfly = Animation("scaryImages\\sonic fly.png",3,game,126/3,46,1)
sonicfly.moveTo(100,550)

ground = Image("scaryImages\\ground.png",game)

sonicstand = Image("scaryImages\\sonic stand.png",game)
sonicstand.moveTo(100,550)

sonicwalk2 = Animation("scaryImages\\sonic walk2.png",4,game,152/4,50,1)
sonicwalk2.moveTo(100,550)

ending = Image("scaryImages\\ending.fw.png",game)
ending.resizeTo(game.width,game.height)

sonicwalk = Animation("scaryImages\\sonic walk.png",4,game,152/4,50,1)
sonicwalk.moveTo(100,555)

redwalk2 = Animation("scaryImages\\red walk2.fw.png",4,game,378/4,91,1) 
redwalk2.moveTo(900,555)
redwalk2.setSpeed(10,90)

screaming = Sound("scaryImages\\screaming.wav",1)

flyingdragon = Animation("scaryImages\\flying dragon1.fw.png",4,game,384/4,94,2)
#flyingdragon.rotatTowards(sonicwalk)
#flyingdragon.moveTowards(sonicwalk,2)
#flying dragon.rotatTowards(sonicwalk2)
#flying dragon.rotatTowards(
#flying dragon.rotatTowards
#ring = Animation("scaryImages\\rings.png",10,game,512/10,

#Rfly = Animation("scaryImages\\rodan fly.png",6,game,223/2,202/3)

#platform = Image("scaryImages\\platform.png",game)
#platform.resizeTo(150,34)
#platform.moveTo(300,525)
title = Image("scaryImages\\title.fw.png",game)
title.draw()
game.drawText("Press [SPACE] to play",320,400)
game.update(1)
game.wait(K_SPACE)
jeffwalk = Animation("scaryImages\\jeff walk.fw.PNG",4,game,119/4,50,1)
jeffwalk.moveTo(-15,555)
jumping = False 
landed = False 
factor = 1.0
while not game.over:                                                                 
    game.processInput()
    #title.draw()
    bk.draw()
    jeffwalk.setSpeed(10,270)
    jeffwalk.move()
    #platform.draw()
    redwalk2.move()
    sonicwalk.draw()
    sonicstand.draw()
    sonicstand.moveTo(sonicwalk.x,sonicwalk.y)
    sonicwalk.visible = False 
    sonicstand.visible = True
    sonicfly.move()
    sonicfly.visible = False
    sonicfly.moveTo(sonicwalk.x,sonicwalk.y)
    sonicwalk2.visible = False
    sonicwalk2.move()
    sonicwalk2.moveTo(sonicwalk.x,sonicwalk.y)
    ground.draw()
    ground.moveTo(400,590)
    flyingdragon.move()
    flyingdragon.rotateTowards(sonicwalk)
    flyingdragon.moveTowards(sonicwalk,2)
    #jeffwalk.rotateTowards(sonicwalk)
    #jeffwalk.moveTowards(sonicwalk,2)
    #Rfly.draw()
    
    if sonicfly.collidedWith(jeffwalk):
        sonicwalk.health-=5

    if sonicwalk2.collidedWith(jeffwalk):
        sonicwalk.health-=5

    if sonicwalk.collidedWith(jeffwalk):
        sonicwalk.health-=5

    if sonicstand.collidedWith(jeffwalk):
        sonicwalk.health-=5


    if sonicfly.collidedWith(redwalk2):
        sonicwalk.health-=5

    if sonicwalk2.collidedWith(redwalk2):
        sonicwalk.health-=5

    if sonicwalk.collidedWith(redwalk2):
        sonicwalk.health-=5

    if sonicstand.collidedWith(redwalk2):
        sonicwalk.health-=1

    if sonicfly.collidedWith(flyingdragon):
        sonicwalk.health-=1

    if sonicwalk2.collidedWith(flyingdragon):
        sonicwalk.health-=1

    if sonicwalk.collidedWith(flyingdragon):
        sonicwalk.health-=1

    if sonicstand.collidedWith(flyingdragon):
        sonicwalk.health-=1
        
    if sonicwalk2.health<1:
        game.drawText("You lose!",game.width/4 ,game.height/4,Font(yellow,90,red))
        game.over=True

    if sonicwalk.health<1:
        game.drawText("You lose!",game.width/4 ,game.height/4,Font(yellow,90,red))
        game.over=True

    if sonicstand.health<1:
        game.drawText("You lose!",game.width/4 ,game.height/4,Font(yellow,90,red))
        game.over=True
        


    if redwalk2.isOffScreen("left"):
        redwalk2.moveTo(900,555)
        
    if jeffwalk.isOffScreen("right"):
        jeffwalk.moveTo(-15,555)
        
    if sonicwalk.isOffScreen("right"):
        sonicwalk.moveTo(30,550)
        sonicwalk2.moveTo(30,550)
        sonicstand.moveTo(30,550)
        
    if sonicwalk.isOffScreen("left"):
        sonicwalk.moveTo(900,555)
        sonicwalk2.moveTo(900,555)
        sonicstand.moveTo(900,555)

    if keys.Pressed[K_LEFT]:
        
        sonicwalk.x-=20
        sonicfly.visible = False
        sonicwalk2.visible = True
        sonicstand.visible = False
        sonicwalk.visible = False
        sonicwalk2.move()
    if keys.Pressed[K_RIGHT]:
        sonicwalk.visible =True
        sonicwalk2.visible = False
        sonicstand.visible = False
        sonicfly.visible = False
        sonicwalk.x+=20
        
       
    if not keys.Pressed:
        sonicstand.visible = True
        sonicwalk2.visible = False
        sonicfly.visible = False
        sonicwalk.visible = False
        
        
    if sonicwalk.y < 300:
        landed = False
        #if sonicfly.collidedWith(platform,"rectangle"):
            #landed = True
        #if sonicwalk.collidedWith(platform,"rectangle"):
            #landed = True
        #if sonicwalk2.collidedWith(platform,"rectangle"):
            #landed = True
        #if sonicstand.collidedWith(platform,"rectangle"):
            #landed = True

    else:
        landed = True
    if jumping:
        sonicwalk.y -= 22.5* factor
        factor *= .95
        landed = False
        if factor < .18:
             
            jumping = False
            factor = 1
    if keys.Pressed[K_UP] and landed and not jumping:
        sonicfly.visible = True
        sonicstand.visible = False
        
        sonicwalk.visible = False
        sonicwalk2.visible = False
        
        jumping = True
        
    if not landed:
        sonicwalk.y += 10.905
        sonicfly.visible = True
        sonicstand.visible = False
        
        sonicwalk.visible = False
        sonicwalk2.visible = False

    #if keys.Pressed[K_DOWN]:
        #sonicwalk.y+=5
    if sonicwalk.collidedWith(ground,"rectangle"):
            landed = True
    if game.time <1:
        ending.draw()
        screaming.play()
    game.drawText("Health =  " + str(sonicwalk.health),500,0)
    game.drawText("Time: " + str(int(game.time)),200,0)
    game.update(30)

game.wait(K_SPACE)#space bar click
game.quit()
   
