%matplotlib inline

import random
import numpy as np
import matplotlib.pyplot as plt

A = [2,40,40]
B = [2,3,4]
C = [50,45,40,35,30,25,20]
D = [50,45,40,35,30,25,20]
A_count =[]
B_count =[]
results = []

for n in range(0,len(B)):
    for m in range(0,len(C)):
        temp = []
        for i in range(1,1001):
            while A[1]>0 and C[m]>0:
                A_roll = random.randint(1,12)
                B_roll = random.randint(1,12)
                if A_roll>B_roll:
                    C[m] = C[m]-(A_roll-B_roll)*A[0]
                else:
                    A[1] = A[1]-(B_roll-A_roll)*B[n]
            if A[1]<=0:
                temp.append('B')
            elif C[m]<=0:
                temp.append('A')
            A[1] = A[2]
            C[m] = D[m]
        results.append(temp)   

for l in results:
    A_count.append(l.count('A'))
    B_count.append(l.count('B'))

#print (results)
print (A_count)
print (B_count)

n_groups = 21
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.2

opacity = 0.4

rects1 = plt.bar(index, A_count, bar_width,
                 alpha=opacity,
                 color='b',
                 label='A')

rects2 = plt.bar(index + bar_width, B_count, bar_width,
                 alpha=opacity,
                 color='r',
                 label='B')

plt.xlabel('# of Wins')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3',
                               'Av4', 'Av4', 'Av4', 'Av4', 'Av4', 'Av4', 'Av4'))
plt.legend()

plt.tight_layout()
plt.show()