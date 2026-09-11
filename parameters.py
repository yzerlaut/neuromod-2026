from brian2 import pF, nS, ms, mV, pA # import units

# --- LIF parameters (conductance-based leak) ---
Cm  = 200*pF
gL  = 10*nS
El  = -70*mV
Vt  = -50*mV
Vr  = -70*mV
Tr  = 10*ms
# note: tau = Cm/gL = 20 ms

# --- recurrent excitatory synapse ---
Ee    = 0*mV
tau_e = 5*ms
we    = 2*nS

# --- recurrent inhibitory synapse ---
Ei    = -80*mV
tau_i = 5*ms
wi    = 10*nS

# --- external excitatory input ("ext"): same decay as recurrent exc, own weight ---
w_ext = 4*nS


