import matplotlib.pyplot as plt
import os
import time
from datetime import datetime
 
now = datetime.now()
nameoff="ddpg_10u10e4lKAISTt12_35_42"
current_time = now.strftime("%H_%M_%S")
dir_name = 'output_episodes/' + nameoff
ep_reward={}
n_episodes=0
 
for filename in os.listdir(dir_name):
    f = os.path.join(dir_name, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        print(f.split("_")[5].split(".")[0])
        episode=int(f.split(".")[0].split("_")[5])
        n_episodes+=1
        fi = open(f,'r')
        reward=float(fi.read().split(":")[1])
        ep_reward[episode]=reward
        fi.close()

fig_reward = plt.figure()
plt.plot([i+1 for i in range(n_episodes)], [ ep_reward[i] for i in range(n_episodes)] )
plt.xlabel("episode")
plt.ylabel("rewards")
fig_reward.savefig(dir_name + '/rewards.png')