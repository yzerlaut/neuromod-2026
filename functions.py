import numpy as np

# stimulus
def build_pattern(ntwk, 
                  n_targets=50, 
                  window=50,
                  quantal_per_event=5,
                  seed=0):
    """ we force the pattern to always target the first neuron so that we can easily see evoked activity"""
    np.random.seed(seed+20)
    target_nrns = [0]+list(np.random.choice(np.arange(ntwk['N_PYR']), n_targets-1))
    stim_times = np.random.uniform(0, window, n_targets)
    return np.concatenate([t+np.arange(quantal_per_event)*0.5 for t in stim_times]),\
            np.concatenate([n*np.ones(quantal_per_event, dtype=int) for n in target_nrns], dtype=int)

def enforce_min_isi(times, dt):
    """Snap spike times to the simulation grid and enforce a minimum
    spacing of one dt between consecutive spikes (per neuron)."""
    times = np.sort(np.round(np.asarray(times) / dt) * dt)
    for k in range(1, len(times)):
        if times[k] <= times[k - 1]:
            times[k] = times[k - 1] + dt
    return times