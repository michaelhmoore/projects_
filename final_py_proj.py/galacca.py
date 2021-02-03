# Import needed packages
import pygame
import random
import sys

# Set width, height, and frames per second for game sceen.
WIDTH = 1000
HEIGHT = 800
FPS = 60

# Setting game variables for the entire game
player_vel = 20
player_width = 150
player_health = 3
kamikaze_width = 100
kamikaze_kill_count = 0
scroll_speed = 5
kamikazes = []
kamikazes_2 = []
kamikaze_2_health = 2
bullet_width = 50
bullet_height = 80
bullet_vel = 20
enemy_bullet_width = 10
enemy_bullet_height = 70
bullet_delay = 10
enemies = []
bullets = []
bullet_count = 0
enemy_width = 200
enemy_health = 5
enemy_vel = 4
boss_width = 700
boss_height = 250
bosses = []
boss_vel = 3
boss_health = 150
boss_spawned = False
boss_death_count = 0

# Setting count
count = 0
enemy_frame_count = 0

# Defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Loading sprites or images
background = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/Untitled-2.jpg"), (WIDTH, HEIGHT))
player = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/B-17.png"), (player_width, player_width))
kamikaze = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/Biploar_type4_1.png"), (kamikaze_width, kamikaze_width))
kamikaze_2 = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/type_3.png"), (kamikaze_width, kamikaze_width))
bullet = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/Untitled.png"), (bullet_width, bullet_height))

enemy_1 = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Downloads/Without Source files -Game Assets/JU-87B2/Type_1/JU87B2 -progress_4.png"), (enemy_width, enemy_width))
enemy_2 = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/JU87B2 -progress_5.png"), (enemy_width, enemy_width))
enemy_sprites = [enemy_1, enemy_2]

boss_image = pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/Type2_2.png"), (boss_width, boss_height))

# Initialize game and create fonts for ingame.
pygame.init()
my_font = pygame.font.SysFont("Arial", 70)
game_over_font = pygame.font.SysFont("bell", 120, bold = True)
win_font = pygame.font.SysFont("cambrian", 120, bold = True)

# Created screen with caption and clock.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Battle")
clock = pygame.time.Clock()

# Background classes
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scroll_speed

class Background1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, -HEIGHT/2)

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scroll_speed

# Created player class.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/1.1)

    def update(self):
        global player_health, count, bullet_delay, counts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - player_width:
            self.rect.x += player_vel
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= player_vel

        count += 1
        if keys[pygame.K_SPACE] and count % bullet_delay == 0:
            all_sprites.add(Bullet())

        for kamikaze in kamikazes:
            if pygame.sprite.collide_rect(self, kamikaze):
                kamikazes.remove(kamikaze)
                all_sprites.remove(kamikaze)
                player_health -= 1

        for kamikaze in kamikazes_2:
            if pygame.sprite.collide_rect(self, kamikaze):
                kamikazes_2.remove(kamikaze)
                all_sprites.remove(kamikaze)
                player_health -= 1

        for bullet in bullets:
            if pygame.sprite.collide_rect(self, bullet):
                bullets.remove(bullet)
                all_sprites.remove(bullet)
                player_health -= 1

# Created Kamikaze class(plane that just crashes)
class Kamikaze(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = kamikaze
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, WIDTH - kamikaze_width), 0)
        self.kamikaze_vel = [random.randrange(-1, 2), random.randrange(2, 8)]

    def update(self):
        self.rect.y += self.kamikaze_vel[1]
        self.rect.x += self.kamikaze_vel[0]
        if self.rect.y > HEIGHT:
            kamikazes.remove(self)
            all_sprites.remove(self)

# Created a 2 shot kamikaze class.
class Kamikaze_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = kamikaze_2
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, WIDTH - kamikaze_width), 0)
        self.kamikaze_vel = [random.randrange(-1, 2), random.randrange(2, 8)]
        self.kamikaze_2_health = kamikaze_2_health

    def update(self):
        self.rect.y += self.kamikaze_vel[1]
        self.rect.x += self.kamikaze_vel[0]
        if self.rect.y > HEIGHT:
            kamikazes_2.remove(self)
            all_sprites.remove(self)

# Created a boss.
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, - boss_height/2)
        self.boss_health = boss_health

    def update(self):
        global boss_vel
        if self.rect.y < HEIGHT/20:
            self.rect.y += boss_vel
        else:
            self.rect.x += boss_vel
            if self.rect.x + boss_width > WIDTH:
                boss_vel *= -1
            elif self.rect.x < 0:
                boss_vel *= -1

def add_kamikaze():
    if random.random() < 0.1 and len(kamikazes) < 8:
        kamikazes.append(Kamikaze())
        for kamikaze in kamikazes:
            all_sprites.add(kamikaze)

def add_kamikaze_2():
    if random.random() < 0.05 and len(kamikazes_2) < 3:
        kamikazes_2.append(Kamikaze_2())
        for kamikaze in kamikazes_2:
            all_sprites.add(kamikaze)

def add_enemy():
    if random.random() < 0.01 and len(enemies) < 1:
        enemies.append(Enemy())
        for enemy in enemies:
            all_sprites.add(enemy)

def add_boss():
    global boss_spawned
    if len(bosses) < 1 and random.random() < 0.005:
        bosses.append(Boss())
        boss_spawned = True
        for boss in bosses:
            all_sprites.add(boss)

def add_bullet():
    global bullet_count
    bullet_count += 1
    if len(bullets) < 10 and bullet_count + 1 >= 60:
        bullet_count = 0
        bullets.append(EnemyBullet())
        for bullet in bullets:
            all_sprites.add(bullet)

def draw_text():
    health = str(player_health)
    killed = str(kamikaze_kill_count)
    health_label = my_font.render("Health: " + health, 1, WHITE)
    screen.blit(health_label, (0, 0))
    killed_label = my_font.render("Points: " + killed, 1, WHITE)
    screen.blit(killed_label, (0, HEIGHT/18))

# Created bullet class.
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center

    def update(self):
        global kamikaze_kill_count
        self.rect.y -= bullet_vel

        for kamikaze in kamikazes:
            if pygame.sprite.collide_rect(self, kamikaze):
                kamikazes.remove(kamikaze)
                all_sprites.remove(kamikaze)
                all_sprites.remove(self)
                kamikaze_kill_count += 1

        for kamikaze in kamikazes_2:
            if pygame.sprite.collide_rect(self, kamikaze):
                kamikaze.kamikaze_2_health -= 1
                all_sprites.remove(self)
                if kamikaze.kamikaze_2_health < 1:
                    kamikazes_2.remove(kamikaze)
                    all_sprites.remove(kamikaze)
                    kamikaze_kill_count += 3
                else:
                    pass

        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                enemy.enemy_health -= 1
                all_sprites.remove(self)
                if enemy.enemy_health < 1:
                    enemies.remove(enemy)
                    all_sprites.remove(enemy)
                    kamikaze_kill_count += 10
                else:
                    pass

        for boss in bosses:
            if pygame.sprite.collide_rect(self, boss):
                boss.boss_health -= 1
                all_sprites.remove(self)
                if boss.boss_health < 1:
                    bosses.remove(boss)
                    all_sprites.remove(boss)
                    kamikaze_kill_count += 1000
                else:
                    pass

        if self.rect.y < 0:
            all_sprites.remove(self)

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((enemy_bullet_width, enemy_bullet_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        if len(enemies) > 0:
            self.rect.center = enemies[0].rect.center

    def update(self):
        self.rect.y += bullet_vel

        if self.rect.y > HEIGHT:
            bullets.remove(self)
            all_sprites.remove(self)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_sprites[0]
        self.rect = self.image.get_rect()
        if random.random() < 0.5:
            self.rect.center = (0, HEIGHT/4)
            self.enemy_vel = enemy_vel
        else:
            self.rect.center = (WIDTH, HEIGHT/4)
            self.enemy_vel = enemy_vel * -1
        self.enemy_health = enemy_health

    def update(self):
        global enemy_frame_count
        self.rect.x += self.enemy_vel
        if self.rect.x > WIDTH or self.rect.x < -enemy_width:
            enemies.remove(self)
            all_sprites.remove(self)

        enemy_frame_count += 1
        if enemy_frame_count + 1 >= 60:
            enemy_frame_count = 0
        self.image = enemy_sprites[enemy_frame_count//30]

def game_over():
    global player_health
    game_over = True
    
    while game_over:
        screen.fill(WHITE)
        label = game_over_font.render("GAME OVER", 1, BLACK)
        screen.blit(label, (WIDTH/3.7, HEIGHT/3))
        score_label = game_over_font.render("Your Score: " + str(kamikaze_kill_count), 1, BLACK)
        screen.blit(score_label, (WIDTH/4, HEIGHT/2.5))
        screen.blit(pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/Type2_2.png"), (600, 300)), (WIDTH/2 - 300, HEIGHT/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def win():
    global boss_death_count
    boss_death_count +=1 
    if boss_death_count + 1 >= 150:
        boss_death_count = 0

        win = True
        while win:
            screen.fill(WHITE)
            label = win_font.render("YOU WON!", 1, BLACK)
            score_label = win_font.render("Your Score: " + str(kamikaze_kill_count), 1, BLACK)
            screen.blit(label, (WIDTH/2.9, HEIGHT/2.5))
            screen.blit(score_label, (WIDTH/4, HEIGHT/2.5))
            screen.blit(pygame.transform.scale(pygame.image.load("/Users/andrewcochran/Desktop/B-17.png"), (300, 300)), (WIDTH/2 - 150, HEIGHT/2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

def title_screen():
    intro = True
    while intro:
        screen.fill(WHITE)
        text = "Press Enter To Start"
        label = my_font.render(text, 1, BLACK)
        screen.blit(label, (WIDTH/4.2, HEIGHT/3))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            intro = False
        pygame.display.update()

title_screen()

all_sprites = pygame.sprite.Group()
all_sprites.add(Background())
all_sprites.add(Background1())
player = Player()
all_sprites.add(player)

def main():
    global bosses
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    all_sprites.add(Bullet())

        all_sprites.update()
        add_kamikaze()

        if kamikaze_kill_count > 49:
            add_kamikaze_2()

        if kamikaze_kill_count > 99:
            add_enemy()
            if len(enemies) > 0:
                add_bullet()

        if kamikaze_kill_count > 119 and not boss_spawned:
            add_boss()
            if len(bosses) == 0:
                add_bullet()

        if boss_spawned and len(bosses) < 1:
            win()

        if player_health < 1:
            game_over()

        all_sprites.draw(screen)
        draw_text()
        pygame.display.update()

    pygame.quit()

main()