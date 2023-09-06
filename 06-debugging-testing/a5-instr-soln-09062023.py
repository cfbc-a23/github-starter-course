import random

def run_trial(target, head_probability):
    total_flips = 0
    consecutive_heads = 0
    while consecutive_heads < target:
        flip = random.random()
        if flip < head_probability:
            consecutive_heads += 1
        else:
            consecutive_heads = 0
        total_flips += 1
    return total_flips

def compute_list_average(lst):
    avg = sum(lst) / len(lst)
    return avg

def compute_simulated_average(target=5, n_trials=1000,
                              seed=0, head_probability=0.5):
    sim_results = []
    random.seed(seed)

    for i in range(n_trials):
        total_flips = run_trial(target, head_probability)
        sim_results.append(total_flips)

    avg = compute_list_average(sim_results)
    return avg

if __name__ == '__main__':
    target = int(input("Target number of heads"))
    n_trials = int(input("Number of trials to perform"))
    head_probability = float(input("Probability of observing heads"))
    print(target, n_trials, head_probability)
    print(compute_simulated_average(target=target,
                                    n_trials=n_trials,
                                    seed=0,
                                    head_probability=head_probability),
            " for target ", target)