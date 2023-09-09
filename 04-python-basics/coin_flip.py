# How many times do I need to flip a coin to get 5 heads in a row?
import random

sim_results = []
n_trials = 100

for i in range(n_trials):
    total_flips = 0
    consecutive_heads = 0
    target = 5

    while consecutive_heads < target:
        # 1. Flip a coin
        flip = random.random()

        # 2a. If it's heads: increment consecutive_heads
        if flip < 0.5:
            consecutive_heads += 1

        # 2b. If it's tails: reset consecutive_heads to 0
        else:
            consecutive_heads = 0

        # 3. Increment the total_flips after coin is flipped
        total_flips += 1

    sim_results.append(total_flips)

avg = sum(sim_results) / len(sim_results)

print(avg, "average total number of coin flips in order to get", target, "heads in a row.")
