import pygame

# เริม่ต้นโปรเจ็ค pygame
pygame.init()

# FPS Frame per second # ตัวใหญ่ Confix 
FPS = 30


# ปรับความกว้าง-สูงของเกม # ตัวใหญ่ Confix
WIDTH = 800
HEIGHT = 700

# สร้างสี # ตัวใหญ่ Confix
BLACK = (0,0,0)
GREEN = (0,255,0)


#  สร้างสกรีนหรือกล่องสำหรับใส่เกม
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# สร้างชื่อเกม
pygame.display.set_caption('Solarizer by Samurai Spicy')

# สร้างนาฬิกาของเกม
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

	def __init__(self):
		#  ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อมีการเรียกใช้
		pygame.sprite.Sprite.__init__(self) 
		
		img = 'C:\\Users\\Peche\\Desktop\\Akechikara\\PyGame\\First Game\\aircraft.png'
		self.image = pygame.image.load(img).convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)


	def update(self):
		self.rect.y += 5
		if self.rect.bottom > HEIGHT:
			self.rect.y = 0



# สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() #กล่องสำหรับเก็บตัวละคร
player = Player() # สร้างตัวละคร
all_sprites.add(player) # เพิ่มตัวละครเข้าไปในกลุ่ม


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


	all_sprites.update()


	# ใส่สีแบคกราวของเกม
	screen.fill(BLACK)

	# นำตัวละครทั้งหมดมาวาดใส่เกม
	all_sprites.draw(screen)

	# ทำให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกม
pygame.quit()

