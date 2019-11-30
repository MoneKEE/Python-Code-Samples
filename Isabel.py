#Isabel - virtual assistant

#! python2
# coding: utf-8

import speech
import sound
import dialogs
import linguistictagger as lt
import time
import sqlite3
import csv
import sys

'''
In physics we are told stories about a fundamental building that comprises all things.  I believe that, given the proper bounds in context, a base vocabulary can be created in order to convey rudimentary meaning to a machine.

PRIMARY BEHAVIOR

Virtual assistant needs to perform three actions:
	
	* Interpret
		This is the brain of the virtual agent which gives meaning
		to the phrases the agent hears.
		
		Using LinguisticTagger tag each term in the phrase with its
		corresponding parts of speech.  The agent will use the original term, 
		its associated tag and its position in the phrase to reduce the response space,
		thereby simplifying response selection.
		
	* Listen
		Covert voice data from m4a to text accomplished by recording voice
		data through standard input.  Speech to text provided by the Sound module.
	
	* Speak
		Voice the agent's response.  Text to speech conversion provided by the 
		Speech module.
'''

def interpret_new(taggedtext):
	#unzip tags, substrings and ranges into separate lists
	tags, substrings, ranges = zip(*taggedtext)
	
		
def interpret(text):
	# Response Handlers
	# determines what and how the assistant responds to inquiries
	
	# acknowledgement handlers
	if text[0:5] == 'hello':
		speak('Hello, Michael.')
		
	elif text[0:3] == 'hey':
		speak('Yes, Michael?')
		
	elif 'thanks' in text or 'thank you' in text:
		speak('Your welcome')
		
	# the who handler
	elif 'who' in text:	
		speak('you are asking a who question')
		
	# the what handler
	elif text[0:4] == 'what':
		if 'time' in text:
			if 'what time is it' in text:
				gettime = time.strftime('%I:%M',time.localtime())
				speak(gettime)
			else:
				speak('you are asking a time question.')
		elif 'is' in text:
			speak('you are asking a what is question')
		else:
			speak('you are asking a what question.')
	
	# Inquiry handlers
	# categorizes inbound inquiries based on the first term
	# in the string in an effort to manage the response problem
	# space.
		
	# the when handler
	elif text[0:4] == 'when':
		speak('you are asking a when question.')
		
	# the where handler
	elif text[0:5] == 'where':
		speak('You are asking a where question.')
		
	# the why handler
	elif text[0:3] == 'why':
		speak('You are asking a why question.')
	
	# the how handler
	elif text[0:3] == 'how':
		speak('You are asking a how question.')
	
	# exit
	elif 'goodbye' in text:
		pass
		
	# exception
	else:
		speak('I did not get that.')
		

def listen():
	# Record an audio file using sound.Recorder:
	recorder = sound.Recorder('speech.m4a')
	
	sound.play_effect('rpg:MetalClick',1.0)
	
	recorder.record()
	# Continue recording until the 'Finish' button is tapped:
	time.sleep(2.5)
	recorder.stop()

	try:
		result = speech.recognize('speech.m4a')
		
		sound.play_effect('game:Ding_3',1.0)
		time.sleep(0.5)
		
		print('=== Details ===')
		print(result)
		print('=== Transcription ===')
		print(result[0][0])
		print('')
		
		return result
		
	except RuntimeError as e:
		print('%s' % (e,))
		print ('')


def speak(text):
	speech.say(text,'en_US')
	while speech.is_speaking():
		time.sleep(0.1)

'''
TEXT PROCESSING
'''
def tagtext(text):
	scheme = lt.SCHEME_NAME_TYPE_OR_LEXICAL_CLASS
	results = lt.tag_string(text, scheme)
	
	print('===Tagging===')
	
	for tag, substring, range in results:
		if tag != 'Whitespace':
			print(substring + ": " + tag)
			
	print('===Details===')
	print(results)		
	print('')
	
	return results

def cleantext(text):
	# change all characters to lower case
	text = text.lower()
	
	text = text.replace("'s", ' is')
	
	return text

'''
MAIN
'''
def main():
	
	#create the database and cursor
	conn = sqlite3.connect('isabel.db')
	c = conn.cursor()
	
	c.execute('''DROP TABLE phrasematrix''')
	
	#
	c.execute('''CREATE TABLE phrasematrix(term, speech, position INTEGER, phrase, tagline)''')
	
	time.sleep(2)
	
	wake()	

	while True:
		try:
			results = raw_input('Enter text: ')
			
			clntext = cleantext(results)
			
			taggedtext = tagtext(clntext)
			
			taglin = ' '.join([tag for tag, wrd, pos in taggedtext if tag != 'Whitespace'])
			
			# Write to table
			# Each pr
			for tag, wrd, pos in taggedtext:
				pnt = str(pos[0])
				if tag != 'Whitespace':				
					command = "INSERT INTO phrasematrix(term, speech, position, phrase, tagline) VALUES ('" + wrd + "','" + tag + "'," + pnt + ",'" + clntext + "','" + taglin + "')"
					c.execute(command)
			
			if clntext == 'goodbye' or clntext == 'Goodbye':
				break
				
		except TypeError as e:
			print(e.message)
			print('')
			
			
	print('===Phrasematrix Contents===')
	
	for row in c.execute('SELECT * FROM phrasematrix'):	
		print(row)
				
	conn.close()
	shutdown()
						
if __name__ == '__main__':
	main()
