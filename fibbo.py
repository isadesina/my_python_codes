import random
random.seed(1)
a, b = 1, 2
while a :  # while a is true
    print(a)
    a, b = b, a + b
    if a > 10:
        a = 0  # set a to be false
#

bool_test = False
counter = 0
while bool_test:
    print("True!")
    counter += 1
    if counter == 4:
        bool_test = False

#

# write a while loop where the loop prints the value of i 6 times and then prints it is finished after the iterations
# after every iteration it increases the value of i

i = 1

while i < 7:
    print(i)
    i += 1  # counter = counter + 1

print("it is finished")


j = 0
while 1 == 1:
    print(j)
    j += 1
    if j >= 10:
        print("Breaking")
        break

print("It is finished!")
k = 1
while k < 100:
    print(k)
    k += 1
    if k == 50:
        break


name ="stella"
if name == "stella":
    print("y")

else:
    print("n")

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
allp = ['a','s','i','o','f','z','l','d']
randallp = random.choice(allp)
for item in allp:
    if item == randallp:
        print(item)
        break

# modularity

