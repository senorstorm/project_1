import random
import numpy as np
import matplotlib.pyplot as plt

A = [2,40]
B = [3,30]
results = []

for i in range(1,1001):
    while A[1]>0 and B[1]>0:
        A_roll = random.randint(1,12)
        B_roll = random.randint(1,12)
        if A_roll>B_roll:
            B[1] = B[1]-(A_roll-B_roll)*A[0]
        else:
            A[1] = A[1]-(B_roll-A_roll)*B[0]
    
    if A[1]<0:
        results.append('B')
    elif B[1]<0:
        results.append('A')
    A[1] = 40
    B[1] = 30

A_count = results.count('A')
B_count = results.count('B')

fig, ax = plt.subplots()
index = np.arange(1)
bar_width = 0.35

rects1 = plt.bar(index, A_count, bar_width,
                 alpha=0.4,
                 color='b',
                 label='A')

rects2 = plt.bar(index + bar_width, B_count, bar_width,
                 alpha=0.4,
                 color='r',
                 label='B')

plt.xlabel('Champion')
plt.ylabel('Win #')
plt.title('Win # by Champion')
plt.xticks(index + bar_width, ('AvB'))
plt.legend()

plt.tight_layout()
plt.show()