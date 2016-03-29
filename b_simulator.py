%matplotlib inline

import random
import numpy as np
import matplotlib.pyplot as plt

# 1 Data initialization
A = []
B = [2,3,4]
C = [50,45,40,35,30,25,20]
D = [50,45,40,35,30,25,20]
A_count =[]
B_count =[]
results = []

# 1.1 Error checking on user input
while True:
    try:
        atk = int(input("Attack: "))
        break # Breaks out of while loop
    except ValueError:
        print("Not an integer. Please try again.")
        
while True:      
    try:
        hp = int(input("Health: "))
        break # Breaks out of while loop
    except ValueError:
        print("Not an integer. Please try again.")

# 1.2 Creating the User's hero
name = input("What is your name, champion?: ")
A.append(atk)
A.append(hp)
A.append(A[1])
print(name, "(",atk,"/",hp,")")

# 2 Starts a battle simulation iterating over test attack values
for n in range(0,len(B)):
    # 2.1 For each attack, iterate over each possible health value
    for m in range(0,len(C)):
        temp = []
        # 2.2 Define test size (neutral at 1000 runs per health)
        for i in range(1,1001):
            # 2.3 Battle function ends when one health becomes < 1
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
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, A_count, bar_width,
                 alpha=opacity,
                 color='b',
                 label='A')

rects2 = plt.bar(index + bar_width, B_count, bar_width,
                 alpha=opacity,
                 color='r',
                 label='B')

plt.xlabel('Stat line')
plt.ylabel('# of Wins')
plt.title('# of Wins of %s V Stat line'%(name))
plt.xticks(index + bar_width, ('Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av2', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3', 'Av3',
                               'Av4', 'Av4', 'Av4', 'Av4', 'Av4', 'Av4', 'Av4'))
plt.legend()

plt.tight_layout()
plt.show()