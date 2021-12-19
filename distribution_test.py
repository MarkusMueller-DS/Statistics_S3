import numpy as np

mu, sigma = 180, 8.511

muf, sigmaf = 170, 8.357


m = np.random.normal(mu, sigma, 1000000)
f = np.random.normal(muf, sigmaf, 1000000)


count_f_larger = 0
for m, f in zip(m,f):
    if f > m:
        count_f_larger += 1


print(np.mean(m))
print(np.mean(f))
print(count_f_larger / 1000000)
