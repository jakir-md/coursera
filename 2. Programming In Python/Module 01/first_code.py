print("Md Jakir Hossain")
x = 1 + 3 \
+ 5
print(x)

# variable writing conventions:
'''
1. myName => camel case
2. my_name => snake case
3. 

'''

a, b, c = 10, 11, 12
print(a);
print(b);
print(c);

d = 10
print(d);

del d; #deleting the variable
# print(d);

def printHello():
    print("Hey! Hello");
    print("Hey! Gello");

printHello();


'''
Datatype in Python:
1. Numeric:
    1. Integer
    2. float
    3. Complex

2. Sequence:
    1. Strings
    2. Lists
    3. Tuple => Immutable.

3. Dictionary: key value pair
4. Set: Unordered Collection
'''

p = 10 + 10j
print(p);

#Sequence
d21 = "Jakir"; #Strings
print(d21);

d22 = [10, 11, "JakirList", True] #Lists
print(type(d22))
d22[2] = "ChangedJakirList"
print(d22[2])

d23 = (10, 11, "JakirTupple", False) #Tupple
print(type(d23))
# d23[2] = "NoChangeInTupple"
print(d23[3])


#Dictionary
d3 = {'name': 'jakir', 'email':'mdjakir@gmail.com'}
print(type(d3))
print(d3["email"])

#Set
d4 = {1, 5, 'Set'} #not subscriptable
print(type(d4))
print(d4)


#Built in functions
def basicBuiltInFunction():
    print("This is print function")
    print("This is len functin", len("len"))
    print("This is int convert", int('75'))
    print("This is float convert", float(10.0))

basicBuiltInFunction()


#Taking Inputs => Takes input as strings
# num1 = input("Input number 1: ")
# num2 = input("Input number 2: ")
# print(num1+num2)
# print(int(num1) + int(num2))
# print('{0} {1}'.format(num1, num2))


#Math and logical operator
d5 = True
d6 = False
d6 = not d6
if(d5 or d6):
    print("At least one is True")
if(d5 and d6):
    print("All Are True")



#Conditional statements:
bill = 101
discount1 = 10
discount2 = 20

if(bill > 100 and bill < 200):
    print('You Pay: ', bill-discount1)
elif (bill > 200):
    print('You Pay: ', bill-discount2)
else :
    print('Your are not eligible for discount')



#Match Statement
http_status = 500
match http_status:
    case 200 | 201:
        print("Success")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")


#Looping in Python
favourites = ['banana', 'apple', 'papya']
for i in range(10):
    print("Loopping..", i)

for indx, item in enumerate(favourites):
    print(indx, item)

for item in favourites:
    print("I like this Fruit: ", item)

count = 0;
while(count < len(favourites)):
    print(favourites[count])
    count+=1


#Controll flow Statements
favorites2 = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for dessert in favorites2:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)


#nested loops
import time
start_time = time.time()
for i in range(2):
    for j in range(10):
        print(0, end = " ")
    print()

print(round(time.time() - start_time, 3))