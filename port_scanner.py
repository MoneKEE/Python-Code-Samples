from socket import *
import time

start_time = time.time()

if __name__ == '__main__':
	target = input('Enter the host to be scanned: ')
	t_IP = gethostbyname(target)
	print('Starting scan on host: ',t_IP)
	
	for i in range(50, 9000):
		s = socket(AF_INET6, SOCK_STREAM)
		
		conn = s.connect_ex((t_IP, i))
		if(conn == 0):
			print('Port %d: OPEN' % (i,))
			
		s.close()
print('Time taken: ', time.time() - start_time)
