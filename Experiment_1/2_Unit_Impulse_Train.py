import numpy as np
import matplotlib.pyplot as plt

def simulate_unit_impulse_train(Signal_length,period):
    impulse_train=np.zeros(Signal_length)
    for n in range(Signal_length):
        if n%period==0:
            impulse_train[n]=1
    return impulse_train

Signal_length=100
period =10
impulse_train=simulate_unit_impulse_train(Signal_length,period)

plt.stem(impulse_train)
plt.title('Impulse Train')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

