#!python3

'''
This widget script simply shows the current local IP address in a label.
'''

import appex, ui
import socket
import console

def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('google.com', 80))
		ip = s.getsockname()[0]
		s.close()
	except:
		ip = 'N/A'
	return ip

label = ui.Label(font=('Menlo', 24), alignment=ui.ALIGN_CENTER)
label.text = 'Local IP: ' + get_local_ip()
label.size_to_fit()

label.present('sheet')





