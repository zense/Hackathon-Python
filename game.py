import pygame
import sys
import client
import time


def load_imgs():
	img = pygame.image.load("space.jpg")
	#player_img = pygame.image.load("space_ship.jpeg")

	return [img]


class Screen:
	def __init__(self):
		self.screen = pygame.display.set_mode((700,700))
		self.screen.fill((255,255,255))




class Bullet:
	def __init__(self,x,y):
		self.x = x
		self.y = y


	def move_b(self):
		self.y = self.y-15


	def draw_bullet(self,screen):
		bullet = pygame.image.load("bullet.png")
		screen.blit(bullet,(self.x,self.y))
		



class Player:
	def __init__(self,x,y,ide):
		self.x = x
		self.y = y
		self.ide = ide
		self.health = 100
		self.is_shooting = 0


	def draw_player(self,screen):
		screen.blit(pygame.image.load("space_ship.png"),(self.x,self.y))


	def update_health(self):
		self.health = self.health-3


	def shoot(self):
		self.is_shooting = 1

		

	def move_up(self):
		self.y = self.y-15

	def move_down(self):
		self.y = self.y+15

	def move_right(self):
		self.x = self.x+15

	def move_left(self):
		self.x = self.x-15



class Main:
	def __init__(self):
		self.s = Screen()
		self.s.screen.fill((0,0,0))
		self.background1 = load_imgs()[0]
		self.bullets_list = []
		pygame.font.init()
		self.welcome_text = pygame.font.Font('freesansbold.ttf',50)
		self.welcome_blit = self.welcome_text.render("press any key to start",True,"red")

		self.wait = pygame.font.Font('freesansbold.ttf',30)
		self.wait_font = self.wait.render("waiting for other players to join",True,"green")

		self.health_font = pygame.font.Font('freesansbold.ttf',30)

		
		
	def welcome_screen(self):
		code = 0
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if e.type == pygame.KEYDOWN:
					code = 1
					
			if(code == 1):
				break

			self.s.screen.blit(self.background1,(0,0))
			self.s.screen.blit(self.welcome_blit,(20,300))				

			pygame.display.update()

		self.wait_screen()


	def wait_screen(self):
		value = 0
		self.client = client.Client()
		self.client.make_threads()
		self.s.screen.fill((255,255,255))
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


			if(self.client.can_start == True):
				print("entered")
				break

			self.s.screen.blit(self.wait_font,(20,300))

			pygame.display.update()

		self.main_screen()

				
	def main_screen(self):
		self.client.recv_id()
		self.client.recv_start_coordinates()
		self.client.poss_ids.remove(self.client.ide)
		bullet_code = 0


		count = 1       
		for i in self.client.start_cordinates:
			if count == self.client.ide:
				self.player1 = Player(i[0],i[1],count)

			elif count == self.client.poss_ids[0]:
				self.player2 = Player(i[0],i[1],count)

			elif count == self.client.poss_ids[1]:
				self.player3 = Player(i[0],i[1],count)

			elif count == self.client.poss_ids[2]:
				self.player4 = Player(i[0],i[1],count)

			count = count+1

		self.client.make_thread2()

		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_UP:
						self.player1.move_up()

					elif e.key == pygame.K_DOWN:
						self.player1.move_down()


					elif e.key == pygame.K_RIGHT:
						self.player1.move_right()


					elif e.key == pygame.K_LEFT:
						self.player1.move_left()


					if(e.key == pygame.K_SPACE):
						self.player1.shoot()

			self.health_display = self.health_font.render(f'health:{self.player1.health}',True,"red")



			self.client.send_cor([self.client.ide,self.player1.x,self.player1.y,self.player1.is_shooting])

			if(self.player1.is_shooting == 1):
				b1 = Bullet(self.player1.x,self.player1.y)
				self.bullets_list.append(b1)
				self.player1.is_shooting = 0
 

		   
			l = [self.client.one,self.client.two,self.client.three]
			for i in l:
				if i[0] == self.client.poss_ids[0]:
					self.player2.x = i[1]
					self.player2.y = i[2]
					if(i[3] == 1):
						b = Bullet(self.player2.x,self.player2.y)
						self.bullets_list.append(b)


				elif i[0] == self.client.poss_ids[1]:
					self.player3.x = i[1]
					self.player3.y = i[2]
					if(i[3] == 1):
						b = Bullet(self.player3.x,self.player3.y)
						self.bullets_list.append(b)

				elif i[0] == self.client.poss_ids[2]:
					self.player4.x = i[1]
					self.player4.y = i[2]
					if(i[3] == 1):
						b = Bullet(self.player4.x,self.player4.y)
						self.bullets_list.append(b)



			self.s.screen.blit(self.background1,(0,0))
			self.player4.draw_player(self.s.screen)
			self.player1.draw_player(self.s.screen)
			self.player2.draw_player(self.s.screen)
			self.player3.draw_player(self.s.screen)
			self.s.screen.blit(self.health_display,(540,20))


			for i in self.bullets_list:
				i.draw_bullet(self.s.screen)
				print("drawing png")
				i.move_b()
				if((abs(i.x -self.player1.x) == 5) and (abs(i.y - self.player1.y)) == 5):
					self.player1.update_health()


			if(self.player1.health == 0):
				print("you lost man")

			print(self.player1.health)


			pygame.display.update()

m = Main()
m.welcome_screen()