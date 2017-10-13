from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pygame

class moon():
	def __init__(self, size, dist, color, speed):
		self.size = size
		self.dist = dist
		self.color = color
		self.speed = speed
		self.rotY = 35
		return

	def render(self):
		glPushMatrix()
		glColor3f(self.color[0], self.color[1], self.color[2])
		#glRotatef(90.0, 1, 0, 0)  
		glRotatef(self.rotY, 0, 1, 0) 
		#glRotatef(35.0, 0, 0, 1) 
		glTranslatef(0.0, 0.0, self.dist) 
		glutWireSphere(self.size,20,20)
		self.rotY += self.speed
		glPopMatrix()
		return

class planet():
	def __init__(self, size, dist, color, speed, hasMoon):
		self.moons = []
		self.size = size
		self.dist = dist
		self.color = color
		self.speed = speed/2
		self.rotY = 35
		self.hasMoon = hasMoon
		if self.hasMoon:
			self.moons.append(moon(self.size/3, self.size + .2, (1, 1, 1), 1.2))
		return

	def render(self):
		# glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glColor3f(self.color[0], self.color[1], self.color[2])
		glRotatef(90.0, 1, 0, 0)  
		glRotatef(self.rotY, 0, 1, 0) 
		glRotatef(35.0, 0, 0, 1) 
		glTranslatef(0.0, 0.0, self.dist) 
		glutWireSphere(self.size,20,20) 
		self.rotY += self.speed
		for m in self.moons:
			m.render();
		glPopMatrix()	
		
		return

class GLContext():
	def __init__(self, screen):
		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LEQUAL)
		self.screen = screen
		self.aspect = screen.get_width()/screen.get_height()
		self.planets = []
		gluPerspective(45.0, self.aspect, 0.1, 200.0)
		self.rot = 0
		self.rot2 = 45
		self.planets.append(planet(.2, 4, (1.0, 0.0, 0.0), 5, False))
		self.planets.append(planet(.3, 5, (1, 0.647059, 0), 4, False))
		self.planets.append(planet(.3, 6.2, (0, 0, 0.8), 3.5, True))
		self.planets.append(planet(.25, 7.5, (0.545098, 0.0, 0.0), 2.5, False))
		self.planets.append(planet(.8, 10, (0.823529, 0.705882, 0.54902), 1.5, False))
		self.planets.append(planet(.5, 12, (.85, 0.643137, 0.12549), 1.3, False))
		self.planets.append(planet(.4, 14, (0, 0.807843, 0.819608), 1.2, False))
		self.planets.append(planet(.4, 16, (0, 0, 0.501961), 1.15, False))
		self.planets.append(planet(.08, 19, (0, 1, 1), 1.1, False))
		return

	def check_events(self):
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				exit()
 				if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
 					exit()
 		return


	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		#glBegin(GL_QUADS)

		glColor3f(1.0, 1.0, 0.0)
		glTranslatef(0.0, 0.0, -30.0) #trasnlates scene -1.0 units in depth (away from the camera)
		glRotatef(-70.0, 1, 0, 0)  
		glRotatef(20.0, 0, 1, 0) 
		glRotatef(self.rot, 0, 0, 1) 

		glutWireSphere(2,20,20) 
		self.rot -= .5
		for p in self.planets:
			p.render()
		#glEnd()
		glPopMatrix()

		return
def main():
	pygame.init() #initializes PyGame
	glutInit()
	screen = pygame.display.set_mode((600,600), pygame.OPENGL|pygame.DOUBLEBUF) #makes screen context for our application
	context=GLContext(screen) #makes OpenGL context for your application

	#Your display loop!
	while True:
		context.check_events() #checks for user events
		context.display() #calls display function
		pygame.display.flip() #swaps buffers and sends rendered image to screen

#ensures that main() gets called when the program runs
if __name__ == '__main__':
	try:
		main()
	finally:
		pygame.quit()

