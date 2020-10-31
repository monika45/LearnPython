# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:14:08 2020

@author: zhy
"""

# %% save()
import numpy as np

a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
np.save('array_save', a)

#%% savez()

a1 = np.array([1, 2, 3, 4, 5, 6, 7])
a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
np.savez('array_savez', array_a=a1, array_b=a2)

#%% savez_compressed()

np.savez_compressed('array_savez_commpressed', array_a=a1, array_b=a2)

# %% load读取
r = np.load('array_save.npy')
print(r)

npz_data = np.load('array_savez.npz')
print(npz_data['array_a'])
print(npz_data['array_b'])

npz_data_2 = np.load('array_savez_commpressed.npz')
print(npz_data_2['array_a'])
print(npz_data_2['array_b'])


