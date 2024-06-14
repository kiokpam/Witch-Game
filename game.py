import pygame,random

pygame.init()
game_font=pygame.font.Font('source/Swiss.ttf',40)
def make_bg():
    screen.blit(bg, (bg_pos, 0))
    screen.blit(bg, (bg_pos + 900, 0))

def move_ball(balls):
    for ball in balls:
        ball.rect.centerx -=4
    return balls
def draw_ball(balls):
    for ball in balls:
        screen.blit(ball_sur,ball.rect)
        alpha_surface=game_font.render(str(ball.key),True, (255,0,0))
        screen.blit(alpha_surface,(ball.rect.centerx-15,ball.rect.centery-30))
screen = pygame.display.set_mode((900, 353))
def check_collision(balls):
    for ball in balls:
        if witch_rect.colliderect(ball.rect):
            return False
    return True
#Backrgound
bg = pygame.image.load("source/bg.png")
bg_pos = 0
#witch
witch = pygame.image.load("source/witch.png")
witch = pygame.transform.scale(witch, (witch.get_width() // 2, witch.get_height() // 2))
witch_rect = witch.get_rect(center=(100, 100))

#ball
ball_sur=pygame.image.load('source/ball.png')
ball_sur=pygame.transform.scale(ball_sur,(100,100))
ball_list=[]
spawnball=pygame.USEREVENT
pygame.time.set_timer(spawnball,600)
class Ball():
    def __init__(self, key):
        self.key=key
        self.pos=random.choice([50,60,70,80])
        self.rect=ball_sur.get_rect(center=(900,self.pos))

Active=True

pygame.display.set_caption("The Witch Game")
clock = pygame.time.Clock()
score=0
high_score=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Active:
                pass
            if event.key == pygame.K_SPACE and not Active:
                Active=True
                ball_list.clear()                           #Xóa list ống cũ
                
        if event.type== spawnball:
            ball=Ball(random.choice([i for i in range(10)]))
            ball_list.append(ball)
    bg_pos -= 1
    if bg_pos <= -900:
        bg_pos = 0
    make_bg()
    if Active:
        Active=check_collision(ball_list)
        ball_list=move_ball(ball_list)
        draw_ball(ball_list)
        keys=pygame.key.get_pressed()

        for ball in ball_list:
            if keys[pygame.K_0 + int(ball.key)]:
                
                pygame.draw.line(screen,(0,0,255),(100,100),(ball.rect.centerx,ball.rect.centery),10)
                ball_list.remove(ball)
                draw_ball(ball_list)
                score+=1
        score_surface=game_font.render(str(score),True, (255,0,0))
        screen.blit(score_surface,(450,150))
    else:
        if score>high_score:
            high_score=score
        score=0
        lose=game_font.render(f'Press Space to play again',True, (255,0,0))
        lose_rect=lose.get_rect(center=(450,250))
        screen.blit(lose,lose_rect)
        score_surface=game_font.render(f'High score: {high_score}',True, (255,0,0))
        screen.blit(score_surface,(250,150))
    
    screen.blit(witch, witch_rect)
    pygame.display.update()
    clock.tick(60)