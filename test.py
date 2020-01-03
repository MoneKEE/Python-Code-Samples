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


Isa()