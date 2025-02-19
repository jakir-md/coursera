'''
#Scope of a variable in python
1. Local = Access only inside the function
2. Enclosed = Enclosed inside the function
3. Global = Global
4. Built in = all built in functions
'''
print()
print('Variable Scope: ')
global_var = 10
def fn1():
    enclosed_var = 20
    def fn2():
        print(enclosed_var)
        print(global_var)
    fn2()
fn1()



#List Data Structure
print()
print('List Data Structure: ')
list1 = [10, [11, 13, 15, 'Jakir'], True]
print(*list1) #all the items are printed seperately
print(list1, sep = " ")

list1.insert(len(list1), 'Inserted New Item') #insert at a specific index
print(list1)

list1.append(10) #appending the end of the list
print(list1)

list1.extend(['extended list', 15, 33, 17]) #extending the list
print(list1)

list1.pop(1) #popping items form the list
print(list1)

del list1[1] #same popping 
print(list1)

for i in list1: #iterating over list
    print(i)




#Tupples in Python:
print()
print('Tupples In Python: ')
tupples = (1, 3, 10, 1, 1, 3.55, False, {13, 18, 19})
print(tupples.count(1))
print(tupples.index(3))
for i in tupples:
    print(i)


#Set In Python
print()
print('Set Data Structure: No Duplicates ')
set_a = {1, 2, 3, 4, 5, 7}
set_a.add(6)
set_a.remove(6)
set_a.discard(7)

set_b = {1, 2, 6, 7, 8, 9, 10}
final_union_set = set_a | set_b #union => set_a.union(set_b) can be done
final_intersection_set = set_a & set_b #insection
final_difference_set = set_a - set_b #items only in the set_a not in the set_b
final_symetry_set = set_a ^ set_b #symetrical items => union - commons
print(set_a)
print(final_union_set)
print(final_intersection_set)
print(final_difference_set)
print(final_symetry_set)



#Dictionary in python
print()
print('Dictionary Data Structure: No Duplicates ')
dictionary_item = {1:'Jakir', 2:'Hossain Mia', 2:'Mosrakul'} #doesn't support duplicate keys. so it'll update the key's value
dictionary_item[3] = 'Noytik' #adding new key value
dictionary_item[2] = 'Md Mosrakul Mia' #reassigning new values
print(dictionary_item)

for key, value in dictionary_item.items():
    print(key, value) #only keys can be printed without the items() function