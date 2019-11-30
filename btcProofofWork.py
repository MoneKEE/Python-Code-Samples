# coding: utf-8
import string
import hashlib
import random
import time

example_challenge = "fgrt354ksnrte398kfjghqa42"

def generation(challenge = example_challenge,size = 24):
		answer = ''.join(random.choice(string.ascii_lowercase +
																	 string.ascii_uppercase +
																	 string.digits) for x in xrange(size))
		attempt = challenge + answer
		return attempt, answer
		
shaHash = hashlib.sha256()

def testAttempt():
		Found = False
		start = time.time()
		
		while Found == False:
				attempt, answer = generation()
				shaHash.update(attempt)
				solution = shaHash.hexdigest()
				
				if solution.startswith('00000'):
						finish = time.time() - start
						print solution
						print "timeTook: ", finish
						Found = True
						
		print answer	

testAttempt()