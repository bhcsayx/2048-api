from agents import ExpectiMaxAgent
from game import Game
from multiprocessing import Pool
import os

data_amount = 8
workers = 4
scores = [128,512,2048]
filenames = []

def generate(times,filename):
    print(filename)
    train_game = Game(score_to_win=128,enable_rewrite_board=True)
    guide_agent = ExpectiMaxAgent(game=train_game)
    cur_times = 0
    while cur_times < times:
        guide_agent.play(record=True,record_file=filename)
        cur_times = cur_times+1;print(cur_times)

p = Pool(workers)
for i in range(workers):
    filename = 'data'+'_'+str(scores[0])+'_'+str(i)+'.txt'
    filenames.append(filename)
    p.apply_async(generate,args=(int(data_amount/workers)+1,filename,))
p.close()
p.join()

merge = 'data_128.txt'
for file in filenames:
    f=open(merge,'a')
    for line in open(file):
        file.writelines(line)
    f.close()

