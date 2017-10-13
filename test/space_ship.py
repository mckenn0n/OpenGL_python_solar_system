from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pygame
import random

def ranNum():
 	return random.uniform(0, 1)
class Cube():
	def __init__(self, size, translate, speed_list_XYZ):
		self.size = size
		self.translate = translate
		self.rotX = 0
		self.rotY = 0
		self.rotZ = 0
		self.speed_list_XYZ = speed_list_XYZ
		return

	def render(self):
		glPushMatrix()

		glColor3f(ranNum(), ranNum(), ranNum())
		glTranslatef(self.translate[0], self.translate[1], self.translate[2]) 
		glRotatef(self.rotX, 1, 0, 0)  
		glRotatef(self.rotY, 0, 1, 0) 
		glRotatef(self.rotZ, 0, 0, 1) 
		# glutWireSphere(self.size,self.s1,self.s2)
		glutWireCube(self.size) 
		self.rotX += self.speed_list_XYZ[0] #3
		self.rotY += self.speed_list_XYZ[1] #2
		self.rotZ += self.speed_list_XYZ[2] #1.5
		glPopMatrix()
		return

class Sphere():
	def __init__(self, size, translate, s1, s2, speed_list_XYZ):
		self.size = size
		self.translate = translate
		self.s1 = s1
		self.s2 = s2
		self.rotX = 0
		self.rotY = 0
		self.rotZ = 0
		self.speed_list_XYZ = speed_list_XYZ
		return

	def render(self):
		glPushMatrix()

		glColor3f(ranNum(), ranNum(), ranNum())
		glTranslatef(self.translate[0], self.translate[1], self.translate[2]) 
		glRotatef(self.rotX, 1, 0, 0)  
		glRotatef(self.rotY, 0, 1, 0) 
		glRotatef(self.rotZ, 0, 0, 1) 
		glutWireSphere(self.size,self.s1,self.s2)
		# glutWireCube(self.size) 
		self.rotX += self.speed_list_XYZ[0] #3
		self.rotY += self.speed_list_XYZ[1] #2
		self.rotZ += self.speed_list_XYZ[2] #1.5
		glPopMatrix()
		return

class GLContext():
	def __init__(self, screen):
		self.cubes = []
		self.spheres = []
		self.screen = screen
		self.aspect = screen.get_width()/screen.get_height()
		self.rotX = 20
		self.rotY = 30
		self.rotZ = 35
		gluPerspective(45.0, self.aspect, 0.1, 200.0)
		self.cubes.append(Cube(.5, (0, 0, 0), (3, 2, 1.5)))
		self.spheres.append(Sphere(.25, (0, 0, 0), 20, 20, (3, 2, 1.5)));
		self.spheres.append(Sphere(.75, (0, 0, 0), 20, 2, (2, 3, 10)));
		self.spheres.append(Sphere(1.75, (0, 0, 0), 3, 3, (1, 1, 1)));
		self.spheres.append(Sphere(1, (0, 0, 0), 20, 20, (0, 1, 0)));
		self.cubes.append(Cube(1.5, (0, 0, 0), (1, 0, 0)))
		return

	def check_events(self):
		#Code goes here...
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				exit()
 				if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
 					exit()
 		return

	# def ranNum(self):
 # 		return random.uniform(0, 1)



	def display(self):
	#Code goes here...
		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		#glBegin(GL_QUADS)

		# glColor3f(self.ranNum(), self.ranNum(), self.ranNum())
		glTranslatef(0.0, 0.0, -6.0) #trasnlates scene -1.0 units in depth (away from the camera)
		# # glRotatef(self.rotX, 1, 0, 0) #20deg rotation around the x-axis 
		# # glRotatef(self.rotY, 0, 1, 0) #30deg rotation around the y-axis
		# # glRotatef(self.rotZ, 0, 0, 1) 
		# glutWireSphere(0.25,20,20)
		# glutWireCube(0.5) 
		# self.rotX += 3
		# self.rotY += 2
		# self.rotZ += 1.5
		# #glEnd()
		for c in self.cubes:
			c.render()
		for s in self.spheres:
			s.render()
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

