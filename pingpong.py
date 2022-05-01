from pygame import *

w=600
h=5000
fps=60
clock=time.Clock()

window= display.set_mode((w,h))
window.fill((255,255,255))
class GameSprite(sprite.Sprite):
   #class constructor
    def __init__(self, player_image, player_x, player_y,size_x,size_y):
       super().__init__()
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.x > 5:
           self.rect.x -= 20
       if keys[K_s] and self.rect.x < w - 80:
           self.rect.x += 20
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= 20
       if keys[K_RIGHT] and self.rect.x < w - 80:
           self.rect.x += 20
bat1=Player("ball.png",0,0,100,1000)
bat2=Player("ball.png",500,0,100,1000)
bon=GameSprite("mai.png",300,200,100,100)
game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    window.fill((255,255,255))
    bat1.update()
    bat1.reset()
    bat2.update()
    bat2.reset()
    bon.update()
    bon.reset()

    display.update()
    clock.tick(fps)