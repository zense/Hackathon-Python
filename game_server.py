import socket
import threading
import pickle
import time

class Server:
	def __init__(self):
		self.soc = socket.socket()
		self.ip = "127.0.0.1"
		self.soc.bind((self.ip,9845))
		self.players_list = []
		self.can_start = False
		self.count = 0
		

	def send_joined(self,conn,ide,room):
		conn.send(pickle.dumps("1"))


	def send_id(self,conn,ide,room):
		conn.send(pickle.dumps(ide))	



	def send_start_co_ordinates(self,conn,ide,room):
		lst = [[350,600],[350,100],[100,350],[600,350]]
		conn.send(pickle.dumps(lst))		
		print("all_sent")



	def process_player(self,conn,ide,room):
		local_count = 0
		while True:
			if((self.can_start) and (local_count == 0)):
				self.send_joined(conn,ide,room)
				time.sleep(0.1)
				self.send_id(conn,ide,room)
				time.sleep(0.1)
				self.send_start_co_ordinates(conn,ide,room)
				local_count += 1
				self.count = self.count+1


			if(self.count == 4*room):
				self.can_start = False
				break

		while True:
			try:
				cor = conn.recv(1024)
				print("recved sucess")
				#k = pickle.loads(cor)
				for i in self.players_list:
					if((i[2] == room) and i[1] != ide):
						i[0].send(cor)

			except Exception as e:
				print(e)


	def main_server_loop(self):
		ide = 1
		room = 1
		self.soc.listen()
		while True:
			conn,addr = self.soc.accept()
			self.players_list.append([conn,ide,room])

			t = threading.Thread(target = self.process_player,args = (conn,ide,room))
			t.start()

			if(ide<4):
				ide = ide+1

			else:
				ide = 1
				self.can_start = True
				room = room+1



			

s = Server()
s.main_server_loop()