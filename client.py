import socket
import pickle
import threading
import sys
import time


class Client:
	def __init__(self):
		self.soc = socket.socket()
		self.can_start = False
		self.poss_ids = [1,2,3,4]
		self.one = [0,0,0]
		self.two = [0,0,0]
		self.three = [0,0,0]
		try:
			self.soc.connect(("127.0.0.1",9845))

			
			print("port lstest")
		except Exception as e:
			print("server unavailable")


	def recv_id(self):
		try:
			self.ide = pickle.loads(self.soc.recv(1024))
			print("id",self.ide)
		except Exception as e:
			print(e)

	def send_cor(self,co_ordinates):
		self.soc.send(pickle.dumps(co_ordinates))



	def recv_is_alljoined(self):
		joined = 0
		try:
			joined = pickle.loads(self.soc.recv(1024))
			print(joined)
			if(joined == "1"):
				self.can_start = True
		except Exception as e:
			joined = 0


	def recv_start_coordinates(self):
		try:
			self.start_cordinates = pickle.loads(self.soc.recv(1024))
			print("coordinates recved")
			print(self.start_cordinates)
		except Exception as e:
			print(e)


	def recv_coorinates(self):
		while True:
			try:
				self.one = pickle.loads(self.soc.recv(1024))
				self.two = pickle.loads(self.soc.recv(1024))
				self.three = pickle.loads(self.soc.recv(1024))

			except Exception as e:
				print(e)

			#print("recved_cor",self.one,self.two,self.three)

	
		

	def make_threads(self):
		Thread = threading.Thread(target = self.recv_is_alljoined)
		Thread.start()

	def make_thread2(self):
		t = threading.Thread(target = self.recv_coorinates)
		t.start()