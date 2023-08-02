#Program to generate a random number

import random
mu = 100
sigma = 50

print(random.gauss(mu,sigma))
#Gaussian distribution

import random
import matplotlib.pyplot as plt

nums=[]
mu=100
sigma=50

for i in range(100):
	temp = random.gauss(mu,sigma)
	nums.append(temp)

plt.plot(nums)
plt.show()