import matplotlib.pyplot as plt
import os
from datetime import datetime

now = datetime.now()
nameoff = "ddpg_10u25e4lKAISTt12_04_47"
current_time = now.strftime("%H_%M_%S")
dir_name = 'output_episodes/' + nameoff
ep_reward = {}
ep_throughput = {}
episode_edge_capabilities = {}
n_episodes = 0

for filename in os.listdir(dir_name):
    f = os.path.join(dir_name, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        print(f.split("_")[5].split(".")[0])
        episode = int(f.split(".")[0].split("_")[5])
        n_episodes += 1
        with open(f, 'r') as fi:
            content = fi.read()

        reward = float(content.split("reward :")[1].split("throughput")[0])
        throughput = float(content.split("throughput :")[1].split("edge capability")[0])
        edge_capability_sum = float(content.split("edge capability :")[1])

        ep_reward[episode] = reward
        episode_edge_capabilities[episode] = edge_capability_sum
        ep_throughput[episode] = throughput

# Plot episode vs rewards
fig_reward = plt.figure()
plt.plot([i + 1 for i in range(n_episodes)], [ep_reward[i] for i in range(n_episodes)])
plt.xlabel("episode")
plt.ylabel("rewards")
fig_reward.savefig(dir_name + '/plot_rewards.png')

# Plot episode vs throughput
fig_throughput = plt.figure()
plt.plot([i + 1 for i in range(n_episodes)], [ep_throughput[i] for i in range(n_episodes)])
plt.xlabel("episode")
plt.ylabel("throughput")
fig_throughput.savefig(dir_name + '/plot_throughput.png')

# Plot episode vs edge capabilities
fig_edge_capabilities = plt.figure()
plt.plot([i + 1 for i in range(n_episodes)], [episode_edge_capabilities[i] for i in range(n_episodes)])
plt.xlabel("episode")
plt.ylabel("edge capabilities")
fig_edge_capabilities.savefig(dir_name + '/plot_edge_capabilities.png')
