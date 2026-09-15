# Modelling Neuromodulation in Cortical Circuits

## Setup

### 1. Install a `python` distribution

Download and install the miniforge installer:
see https://github.com/conda-forge/miniforge

### 2. Install the scientific computing packages

```
pip install numpy scipy scikit-learn matplotlib 
```

### 3. Install `brian2` 

```
pip install brian2
```

### 4. Clone this repository

```
git clone https://github.com/yzerlaut/neuromod-2026
```

## Project

> *Modelling the VIP-mediated Effedt of Arousal Modulation on Cortical Dynamics and Computation*


### Tasks

1. Implement another afferent excitatory drive targetting pyramidal and VIP interneurons

i.e. starting from this arcitecture:

![alt text](figs/basic-architecture.png)

Implement this architecture with the additional neuromodulatory drive:

![alt text](figs/new-architecture.png)


What is the impact and functional role of this VIP-mediated neuromodulatory drive ?
How does it affect the properties of ongoing cortical activity ?
How does it affect the processing of incoming stimuli ?