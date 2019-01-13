from .guides import Guides
from .game import Game
import numpy as np
from .model import model
from keras.models import load_model
class ModelWrapper:

	def __init__(self,capacity=3000):
		self.model=load_model('cnn_2048.h5')
		self.memory=Guides(capacity)
		self.training_step=0
		self.game=None

	def predict(self,board):
		tmp_board = np.array(board)
		tmp = tmp_board[None,0:4,0:16]
		result = model.predict(tmp)
		tmp_direction = list(result[0])
		return tmp_direction.index(max(tmp_direction))
	
	'''def move(self,game):
		ohe_board=game.ohe_board
		suggest = board_to_move(game,board)
		direction=self.predict(ohe.board).argmax()
		game.move(direction)
		self.memory.push(ohe_board,suggest)

	def train_online(self,batch):
		if self.memory.ready(batch):
			guides=self.memory.sample(batch)
			X=[];Y=[]
			for guide in guides:
				X.append(guide,state)
				ohe_action = [0]*4
				ohe_action[guide.action]=1
				Y.append(ohe_action)
			loss,acc = self.model.train_on_batch(np.array(X),np.array(Y))
			self.writer.add_scalar('loss',float(loss),self.training_step)
			self.writer.add_scalar('acc',float(acc),self.training_step)
			self.training_step+=1
'''
	def train_offline(self):
		raw_data=open('game2048/data_2048.txt','r')
		X=[];Y=[]
		for line in raw_data.readlines():
			data = list(line.strip('\n').replace("[",'').replace("]",'').replace(' ','').replace(',',''))
			ohe_board = np.zeros((4,4,16));m=0
			for i in range(4):
				for j in range(4):
					for k in range(16):
						ohe_board[i][j][k]=(int(data[m]));m=m+1
			ohe_action = [0]*4
			ohe_action[int(data[256])] = 1
			X.append(ohe_board)
			Y.append(ohe_action)
		loss,acc = self.model.train_on_batch(np.array(X),np.array(Y))
		print (loss,acc)
		self.training_step+=1
