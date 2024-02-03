from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, color = None):
        ().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
        self.fill_color = (200, 200, 255)
        if color:
            self.fill_color = color
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fill(self):
        draw.rect(window, self.fill_color, self.rect)

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - sizey: #1235
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - sizey: #1235
            self.rect.y += self.speed
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

win_width = 700 #1280
win_height = 500 #700

sizey = 100
sizex = 20

dx = 3
dy = 3

window = display.set_mode((win_width, win_height))
window.fill((200, 200, 255))
display.set_caption("Пінг-понг")
# background = transform.scale(image.load("starry_sky.png"), (win_width, win_height))

# player1 = Player('platform.png', 10, 10, sizex, sizey, 10)
# player2 = Player('platform.png', 660, 10, sizex, sizey, 10)

ball = Player('ball.png', 100, 200, 50, 50, 10)

players = sprite.Group()
for i in range(1, 2):
    player = Player('platform.png', 10, 10, sizey, sizey, 10)
    players.add(player)
# players.add(player1)
# players.add(player2)

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += dx
    ball.rect.y += dy
    
    if sprite.spritecollide(players, ball, False): #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
        dx *= -1
    # if sprite.spritecollide(players, ball, False): #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
    #     dx *= -1
    if ball.y < 0 or ball.y > win_height - 50: #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
        dy *= -1

    # if ball.rect.colliderect(platform.rect):
    #     dy *= -1
    # if ball.rect.x < 0 or ball.rect.x > 450:
    #     dx *= -1

    # if ball.rect.y < 0:
    #     dy *= -1

    player.fill()
    player.fill()
    ball.fill()

    player.update2()
    player.update1()
    ball.update()

    player.reset()
    player.reset()
    ball.reset()

    player.draw()
    player.draw()
    ball.draw()

    display.update()
    time.delay(50)

#
# from pygame import *

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, color = None):
#         ().__init__()
#         self.image = transform.scale(image.load(player_image), (sizex, sizey))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#         self.size_x = size_x
#         self.size_y = size_y
#         self.fill_color = (200, 200, 255)
#         if color:
#             self.fill_color = color
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
#     def fill(self):
#         draw.rect(window, self.fill_color, self.rect)

# class Player(GameSprite):
#     def update1(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_UP] and self.rect.y > 0:
#             self.rect.y -= self.speed
#         if keys_pressed[K_DOWN] and self.rect.y < win_height - 100: #1235
#             self.rect.y += self.speed
#     def update2(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_w] and self.rect.y > 0:
#             self.rect.y -= self.speed
#         if keys_pressed[K_s] and self.rect.y < win_height - 100: #1235
#             self.rect.y += self.speed
#     def draw(self, shift_x=0, shift_y=0):
#         self.fill()
#         window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# win_width = 700 #1280
# win_height = 500 #700

# sizey = 100
# sizex = 20

# dx = 7
# dy = 7

# window = display.set_mode((win_width, win_height))
# window.fill((200, 200, 255))
# display.set_caption("Пінг-понг")
# # background = transform.scale(image.load("starry_sky.png"), (win_width, win_height))

# player1 = Player('platform.png', 10, 10, sizex, sizey, 10)
# player2 = Player('platform.png', 660, 10, sizex, sizey, 10)
# sizey = 50
# sizex = 50
# ball = Player('ball.png', 100, 200, sizex, sizey, 10)

# game = True
# finish = False

# clock = time.Clock()
# FPS = 60
# font.init()
# font2 = font.Font(None, 36)
# font3 = font.Font(None, 100)
# while game:
#     player1.fill()
#     player2.fill()
#     ball.fill()

#     for e in event.get():
#         if e.type == QUIT:
#             game = False

#     player1_win = font3.render("Гравець 2 програв", 1, (0, 0, 0))
#     player2_win = font3.render("Гравець 1 програв", 1, (0, 0, 0))

#     ball.rect.x += dx
#     ball.rect.y += dy
    
#     count = 0
#     if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
#         dx *= -1
#         count += 1
#     if ball.rect.y < 0 or ball.rect.y > win_height - 50:
#         dy *= -1
#     if ball.rect.x < 0:
#         window.blit(player2_win, (20, 200))
#         finish = True
#     if ball.rect.x > win_width - 50:
#         window.blit(player1_win, (20, 200))
#         finish = True
#     if count == 5 or count==10 or count ==15:
#         dx += 5
#         dy += 5
#         ball.rect.x += dx
#         ball.rect.y += dy
#     # if count % 5 == 0 and count > 1 and dx < 30 and dy < 30:
#     #     dx += 7
#     #     dy += 7

#     player1.update2()
#     player2.update1()
#     ball.update()

#     player1.reset()
#     player2.reset()
#     ball.reset()

#     player1.draw()
#     player2.draw()
#     ball.draw()

#     display.update()
#     time.delay(50)
