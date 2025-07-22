import numpy as np
import pandas as pd

b_x = 0.015       
b_y = 0.015
del_k_x = 0.0366
del_k_y = 0.0168
rms = 15e-6 # 25% imperfection       
t0 = 0.0001       
n_x = 96
n_y = 96


nodes_df = pd.read_csv("Nodal_Coordinates.csv")  


nodes_df = nodes_df.sort_values(by='NodeLabel').reset_index(drop=True)


x = nodes_df['X'].values
y = nodes_df['Y'].values


k_x = np.arange(n_x) * del_k_x
k_y = np.arange(n_y) * del_k_y


phi = 2 * np.pi * np.random.rand(n_x, n_y)

f_xy = np.zeros_like(x)
const = ((rms**2)/(4 * np.pi)) * b_x * b_y

for i in range(n_x):
    for j in range(n_y):
        kxi = k_x[i]
        kyj = k_y[j]
        phi_ij = phi[i, j]  
        Sff_ij = const * np.exp(-0.25 * (b_x**2 * kxi**2 + b_y**2 * kyj**2))
        A_ij = np.sqrt(2 * Sff_ij * del_k_x * del_k_y)
        f_xy += A_ij * np.cos(kxi * x + kyj * y + phi_ij)
        

f_xy -= np.mean(f_xy)
t_xy = t0 + f_xy


# Assign ElementID as NodeLabel
nodes_df['ElementID'] = nodes_df['NodeLabel']
nodes_df['Thickness'] = t_xy

# OUTPUT CSV
nodes_df[['ElementID', 'Thickness']].to_csv("element_thickness_15_0.1mm.csv", index=False)
print("CSV file written with 1:1 mapped ElementID and Thickness.")
