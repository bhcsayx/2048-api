from keras.models import Sequential
from keras.layers import Dense,Conv2D,Dropout,Activation,LSTM,BatchNormalization,Flatten
import keras.backend as K

model = Sequential()


model.add(Conv2D(512,kernel_size=(2,1),padding='valid',use_bias=False,input_shape=(4,4,16)))
model.add(Conv2D(512,kernel_size=(1,2),padding='valid',use_bias=False))
model.add(Conv2D(4096,kernel_size=(2,1),padding='valid',use_bias=True))
model.add(Conv2D(4096,kernel_size=(1,2),padding='valid',use_bias=True))
model.add(Conv2D(4096,kernel_size=(2,1),padding='valid',use_bias=True))
model.add(Conv2D(4096,kernel_size=(1,2),padding='valid',use_bias=True))
model.add(Flatten())
model.add(Dense(512,activation='relu'))


'''model.add(Dropout(0.05))'''
model.add(Dense(128,activation='relu'))
'''model.add(Dropout(0.1))'''

model.add(Dense(4,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#model.save('cnn_2048.h5')

