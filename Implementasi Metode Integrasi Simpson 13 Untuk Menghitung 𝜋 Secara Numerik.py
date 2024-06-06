import numpy as np
import time

i = 95
j = i %3

print ("jumlah nim terakhir", i, "=", j) 
print ( "Jadi, menggunakan Metode 3 (Integrasi Simpson 1/3)")
print ()

def f(x):
    return 4 / (1 + x**2)

def simpson_13(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N harus genap untuk metode Simpson 1/3")
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    fx = f(x)
    result = h/3 * (fx[0] + 2 * sum(fx[2:N:2]) + 4 * sum(fx[1:N:2]) + fx[N])
    return result

def rms_error(estimated, reference):
    return np.sqrt((estimated - reference)**2)

pi_ref = 3.14159265358979323846
N_values = [10, 100, 1000, 10000]
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = simpson_13(f, 0, 1, N)
    elapsed_time = time.time() - start_time
    error = rms_error(pi_approx, pi_ref)
    results.append((N, pi_approx, error, elapsed_time))

for result in results:
    N, pi_approx, error, elapsed_time = result    
    print(f"N = {N} | Pi Approximation: {pi_approx} | RMS Error: {error} | Execution Time: {elapsed_time} seconds")
