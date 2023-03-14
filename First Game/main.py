import pygame
import random 

# เริ่มต้นโปรเจ็ค pygame
pygame.init()

# FPS Frame per second # ตัวใหญ่ Confix 
FPS = 30


# ปรับความกว้าง-สูงของเกม # ตัวใหญ่ Confix
WIDTH = 800
HEIGHT = 700

# สร้างสี # ตัวใหญ่ Confix
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

# คะแนนเมื่อยิ่งโดน
SCORE = 0
LIVES = 3


#  สร้างสกรีนหรือกล่องสำหรับใส่เกม
screen = pygame.display.set_mode((WIDTH,HEIGHT))


# สร้างชื่อเกม
pygame.display.set_caption('Solarizer by Samurai Spicy')

# สร้างพาธ background
bg =  'C:\\Users\\Peche\\Desktop\\Akechikara\\PyGame\\First Game\\background.png'
# โหลด background มาไว้
background = pygame.image.load(bg).convert_alpha()
background_rect = background.get_rect()


# สร้างนาฬิกาของเกม
clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		#  ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อมีการเรียกใช้
		pygame.sprite.Sprite.__init__(self) 
		
		img = 'C:\\Users\\Peche\\Desktop\\Akechikara\\PyGame\\First Game\\aircraft.png'
		self.image = pygame.image.load(img).convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()

		# สุ่มตำแหน่งแนวแกน x
		rand_x = random.randint(self.rect.width ,WIDTH - self.rect.width)

		# ตำแหน่งจากจุดศูนย์กลางของตัวละคร
		self.rect.center = (rand_x, 0)

		# speed y
		self.speed_y = random.randint(1,10)


	def update(self):
		self.rect.y += self.speed_y

		if self.rect.bottom > HEIGHT:
			self.rect.y = 0
			# สุ่มตำแหน่ง x อีกครั้ง
			rand_x = random.randint(self.rect.width ,WIDTH - self.rect.width)
			self.rect.x = rand_x
			self.speed_y = random.randint(1,10)


class Player(pygame.sprite.Sprite):

	def __init__(self):
		#  ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อมีการเรียกใช้
		pygame.sprite.Sprite.__init__(self) 
		
		img = 'C:\\Users\\Peche\\Desktop\\Akechikara\\PyGame\\First Game\\bomber.png'
		self.image = pygame.image.load(img).convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT - self.rect.height)

		# speed x
		self.speed_x = 0


	def update(self):
		# self.rect.y += 5 

		self.speed_x = 0

		# เช็คว่ามีการกดปุ่มหรือไม่? ปุ่มอะไร?
		keystate = pygame.key.get_pressed()

		if keystate[pygame.K_LEFT]:
			self.speed_x = -5

		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5

		self.rect.x += self.speed_x

		if self.rect.bottom > HEIGHT:
			self.rect.y = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		group_bullet.add(bullet)


class Bullet(pygame.sprite.Sprite):

	def __init__(self,x,y):
		# x = center ของเครื่องบิน
		# y = top ของเครื่องบิน

		#  ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อมีการเรียกใช้
		pygame.sprite.Sprite.__init__(self) 
		

		self.image = pygame.Surface((10,10))
		self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y

		# speed x
		self.speed_y = -10

	def update(self):
		self.rect.y += self.speed_y


		#  ลบกระสุนเมื่อแกน y < 0 
		if self.rect.y < 0:
			self.kill()

font_name = pygame.font.match_font('arial')
def draw_text(screen,text,size,x,y):
	font = pygame.font.Font(font_name,size)
	text_surface = font.render(text,True,WHITE)
	text_rect = text_surface.get_rect()
	text_rect.topleft = (x,y)
	screen.blit(text_surface,text_rect)


# draw_text(screen, 'SCORE: 100', 30, WIDTH-100, 10)

# สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() #กล่องสำหรับเก็บตัวละคร
group_enemy = pygame.sprite.Group() #กล่องสำหรับเก็บศัตรู
group_bullet = pygame.sprite.Group() #กล่องสำหรับใส่กระสุน


player = Player() # สร้างตัวละคร
all_sprites.add(player) # เพิ่มตัวละครเข้าไปในกลุ่ม

# enemy
for i in range(5):
	enemy = Enemy()
	all_sprites.add(enemy)
	group_enemy.add(enemy)


# สถานะของเกม
running = True # True = YES , False = No

while running:
	# สั่งให้เกมรันตามเฟรมเรต
	clock.tick(FPS)

	# ตรวจสอบว่าเราปิดเกมแล้วยัง?
	# ถ้าหากเรากดกากบาท จะสั่งให้ตัวแปร running = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()

	all_sprites.update()

	# ตรวจสอบการชนกันของ Sprite ด้วยฟังก์ชั่น collide
	collide = pygame.sprite.spritecollide(player,group_enemy, True)
	# print(collide) 

	# if collide:
	# 	LIVES -= 1

	if collide # and LIVES == 0:
		# หากมีการชนกัน จะปิดโปรแกรมทันที
		running = False


	# bullet collission
	hits = pygame.sprite.groupcollide(group_bullet, group_enemy, True, True)
	print('Bullet:',hits)
	for h in hits:
		enemy = Enemy()
		all_sprites.add(enemy)
		group_enemy.add(enemy)
		# add score
		SCORE += 10 # SCORE = SCORE + 1


	# ใส่สีแบคกราวของเกม
	screen.fill(BLACK)

	screen.blit(background,background_rect)

	# update score
	draw_text(screen, 'SCORE: {}'.format(SCORE) , 30, WIDTH-300, 10)
	draw_text(screen, 'Lives: {}'.format(LIVES) , 20, 100, 10)

	# นำตัวละครทั้งหมดมาวาดใส่เกม
	all_sprites.draw(screen)

	# ทำให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกม
pygame.quit()

