from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pygame

class GLContext():
	def __init__(self, screen):
		self.screen = screen
		self.aspect = screen.get_width()/screen.get_height()
		gluPerspective(45.0, self.aspect, 0.1, 200.0)
		return

	def check_events(self):
		#Code goes here...
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				exit()
 				if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
 					exit()
 		return


	def display(self):
	#Code goes here...
		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		#glBegin(GL_QUADS)


		glTranslatef(0.0, 0.0, -1.0) #trasnlates scene -1.0 units in depth (away from the camera)
		glRotatef(20.0, 1, 0, 0) #20deg rotation around the x-axis 
		glRotatef(30.0, 0, 1, 0) #30deg rotation around the y-axis
		glRotatef(40.0, 0, 0, 1) #49deg rotation around the z-axis

		glutWireCube(0.5) 

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

