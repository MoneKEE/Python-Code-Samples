# coding: utf-8

"""
4 layer neural network

This module simulates a four-layer neural network.  
It accepts a 4x4 matrix of binary values as input and a 4x1 matrix of binary values
as output.  The neural network is trained by Back Propagation in an attempt to predict the function that
produces the supplied output given the supplied input.

Backpropagation - Looks to minimize the error function in weight space using the method of 
	gradient descent.  The combination of weights that acheive minimization are considered to be
	a solution to the learning problem.  With each iteration of the algorithm the gradient of the
	error function is found then used to "correct" the randomly initialized synaptic weights.
	
	The learning problem consists of identifying the proper combination of weights which allow the 
	network function Fn(x) to approximate a given function F(x) as closely as possible.
	
Activation Function - The sigmoid s(x) is used as the approximation of the nonlinear step function which 	    	guarantees continuity and differentialbility of the error function.
	
									s(x) = 1 / (1 + e^-cx), 0 < s(x) < 1
									s(x)' = (e^-x)/(1+e^-x)^2 = s(x)*(1-s(x))
			
	The constant c can be chosen arbitrarily and determines the shape of the sigmoid curve.  The reciprocal  (1/c) is called the Temperature parameter of the neural network.  Higher values of c bring the shape closer to that of the step function.
	
VARIABLE DEFINITIONS
X -> Input dataset, an m by n matrix of binary data points
y -> Output dataset and expected values for each training data point 

?? Hypothesis: Adding more layers should make the system more resilient.  But does there exist a threshold where adding a layer begins to degrade performance

l0 -> First layer of the network and the input layer of n x 1
l1 -> Second layer of the network, otherwise known as the first hidden layer
l2 -> Third layer of the network, otherwise known as the second hidden layer
l3 -> Final layer of the network and the output layer, which is our hypothesis, and should
			approximate the correct answer as we train

syn0 -> First layer of weights, synapse0, connecting l0 and l1
syn1 -> Second layer of weights, synapse1, connecting l1 to l2
syn2 -> Third layer of weights, synapse2, connecting l2 to l3

l3_error ->
l3_delta ->

l2_error -> This is the amount that the neural network missed
l2_delta -> This is the error of the network scaled by the confidence.  It's almost identical to the error except that extremely confident 						errors are muted

l1_error -> Weighting l2_delta by the weights of syn1, we can calculate the error in the first 
						middle/hidden layer
l1_delta -> This is the l1 error of the network scaled by the confidence.  Almost identical
		with the l1_error except that confident errors are muted
"""



import numpy as np
from six.moves import range

class nnet4(object):
	#Initialize input/output datasets and synaptic weights
	def __init__(self):	
		#seed random numbers to make calculation derterministic
		np.random.seed(1)
		
		#intialize weights randomoly with mean 0
		self.syn0 = 2*np.random.random((4,4)) - 1
		self.syn1 = 2*np.random.random((4,4)) - 1
		self.syn2 = 2*np.random.random((4,1)) - 1 
	
		# input datasets
		#X0 -> Training set
		#X1 -> Testing set
		self.X0 = np.array([[0,1,0,0],[0,1,1,0],[1,0,0,0],[1,1,1,1],[1,0,1,0]])

		#output dataset
		self.y = np.array([[0],[1],[1],[0],[1]])
		
	def run(self):
		self.train()
		self.testSweep()
		
	#the sigmoid function simulates the nonlinear step function. The derivative of the sigmoid is used
	#to determine weight adjustment vectors at the end of each iteration.
	def nonlin(self,x,c=1,deriv=False,fcn="sigmoid"):
		
		#sigmoid nonlinear
		if fcn=="sigmoid":
			if(deriv==True):
				return x*(1-x)
			return 1/(1+np.exp(-x*c))
			
		#step function
		if fcn=="step":
			if x*c > 0:
				return 1
			else:
				return 0
				
	#test the current synaptic weight settings with 
	#input set X1 comprised of input combinations
	#not encountered in the training set
	def test(self,inp=[0,0,0,0]):
		self.l0 = inp
		self.l1 = self.nonlin(np.dot(self.l0,self.syn0))
		self.l2 = self.nonlin(np.dot(self.l1,self.syn1))
		self.l3 = self.nonlin(np.dot(self.l2,self.syn2))
	
		print("-----------------------------")
		print(inp, '|', self.l3)
	
	#test the current synaptic weight settings by passing	to self.test a list if tuples
	#representing the complete set of possible inputs
	def testSweep(self):
		swp = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
		
		print(" input       | output")
		
		for itr in swp:
			self.test(itr)
	
	#Set the randomly intialized synaptic weights
	#by backpropagation training program.
	def train(self,iter=80000):
		for iter in range(iter):
			#Forward propagation - Each successive layer is formed by calculating the sigmoid of the dot
			#product of the previous layer and it's corresponding set of synaptic weights.  Notice the
			#correspodence between the column count of the neuronal layer and the row count of the 
			#associated synaptic layer.
			#l0(4x4)
			#l1(4x4)=l0(4x4)*syn0(4x4)
			#l2(4x4)=l1(4x4)*syn1(4x4)
			#l3(4x1)=l2(4x4)*syn2(4x1)
			self.l0 = self.X0
			self.l1 = self.nonlin(np.dot(self.l0,self.syn0))
			self.l2 = self.nonlin(np.dot(self.l1,self.syn1))
			self.l3 = self.nonlin(np.dot(self.l2,self.syn2))
		
			#Determine the difference between the current output and the expected output. This will be
			#used in the next expression.
			#        Dy = Ye - Yc
			self.l3_error = self.y - self.l3
		
			#in what direction is the target value?  were we really sure?  if so dont change too much.
			#The "Delta Function" is the error minus the derivative of the expected output's sigmoid 
			#function.  Establishes in which direction the #target value lies
			#
			self.l3_delta = self.l3_error * self.nonlin(self.l3,deriv=True)
			
			#The layer 1/2 error function is determined somewhat differently, as the dot product of the 
			#layer 3 delta function and the transpose of synaptic layer 2
			#
			self.l2_error = np.dot(self.l3_delta,self.syn2.T)
			self.l2_delta = self.l2_error * self.nonlin(self.l2,deriv=True)

			self.l1_error = np.dot(self.l2_delta,self.syn1.T)
			self.l1_delta = self.l1_error * self.nonlin(self.l1,deriv=True)
		
			#Weight adjustment vectors determining magnitude and direction of change for each element in
			#the synaptic layers:
			#			Wn = Ln dot Δ(Ln+1)
			self.syn2 += np.dot(self.l2.T,self.l3_delta)
			self.syn1 += np.dot(self.l1.T,self.l2_delta)
			self.syn0 += np.dot(self.l0.T,self.l1_delta)
			
			#Commit current values to table
			
		
			#Display the current values of layer1/2,layer1/2 error, layer1/2 delta every 10000 steps
			if (iter % 10000) == 0:
				plist = ["ERROR: " + str(np.mean(np.abs(self.l3_error))),"",
						"syn0:  ","----------",self.syn0,"",
						"syn1: ","----------",self.syn1,"","syn2: ","----------",self.syn2,"",
						"l1: ","----------",self.l1,"","l2: ","----------",self.l2,"","l3: ",
						"----------",self.l3,"","l1_error: ",self.l1_error,"",
						"l2_error: ","----------",self.l2_error,"","l3_error: ",
						"----------",self.l3_error,"","l1_delta: ","----------",self.l1_delta,"",
						"l2_delta: ","----------",self.l2_delta,"","l3_delta: ","----------",
						self.l3_delta,""]
									
				plist1 = ["ERROR: " + str(np.mean(np.abs(self.l3_error))),"",
						"syn0:  ","----------",self.syn0,"",
						"syn1: ","----------",self.syn1,"",
						"l1: ","----------",self.l1,"l1_delta: ","----------",self.l1_delta,"","l1_error: ",self.l1_error,"","syn2: ","----------",self.syn2,"","l2: ","----------",self.l2,"l2_delta: ","----------",self.l2_delta,"","l2_error: ","----------",self.l2_error,"","l3: ",
						"----------",self.l3,"","l3_error: ",
						"----------",self.l3_error,"","l3_delta: ","----------",
						self.l3_delta,""]
						
				for p in plist1:
					print(p)

if __name__ == "__main__":	
		import sys

		
