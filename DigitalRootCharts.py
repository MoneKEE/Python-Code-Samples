import numpy as np
from matplotlib.patches import RegularPolygon, Circle, Shadow
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def Isa():
	fig, ax = plt.subplots()
	
	#Month
	pentagon = RegularPolygon([0.5,0.5], 5,0.5,facecolor='none',linewidth=3)
	ax.add_artist(pentagon)
	
	#Day
	triangle = RegularPolygon([0.5,0.5], 3,0.5,facecolor='none',linewidth=1)
	ax.add_artist(triangle)
	
	#Year
	circle = Circle([0.5,0.5],0.5,facecolor='none',linewidth=5)
	ax.add_artist(circle)
	
	plt.show()


def Buba():	
	fig, ax = plt.subplots()
	
	#Month
	heptagon = RegularPolygon([0.5,0.5], 7,0.5,facecolor='none',linewidth=3)
	#shadow = Shadow(heptagon,0.5,0.5, props=dict(lw="10"))
	ax.add_artist(heptagon)
	#ax.add_artist(shadow)
	
	#Day
	octagon = RegularPolygon([0.5,0.5], 8,0.5,facecolor='none',linewidth=1)
	ax.add_artist(octagon)
	
	#Year
	pentagon = RegularPolygon([0.5,0.5], 5, 0.5, facecolor='none',linewidth=5)
	ax.add_artist(pentagon)
	
	plt.show()
	
	
def Moi():	
	fig, ax = plt.subplots()
	
	#Month
	hexagon = RegularPolygon([0.5,0.5],6,0.5,facecolor='none',linewidth=3)
	ax.add_artist(hexagon)
	 
	#Day
	rectangle = RegularPolygon([0.5,0.5],4,0.5,facecolor='none',linewidth=1)
	ax.add_artist(rectangle)
	
	#year
	octagon = RegularPolygon([0.5,0.5],8,0.5,facecolor='none',linewidth=5)
	ax.add_artist(octagon)
	
	plt.show()
	
Isa()

Buba()

Moi()
	
	







