# for taking integer as an input

n= int(input())

# for taking string as an input

s = input()

# Note -> No need to specify as str(input())

# taking array of integers as an input

arr = list(map(int,input().strip().split()))

# for above one.. it should be given that item of array are given with spaces

# another way

arr= list(map(int,input().split()))

# another way

arr=[]
a=input()
for i in a.split():
  arr.append(i)

# string as input but want to store as list

s = list(input())

# taking array of stirng as input

arr_string = list(map(str,input().string().split()))

# similary we can do for the touples and other data types

# taking limited no of integers as input

# method 1 -> take input in arr and use each element of list as the variable 

# use map function 

a,b=map(int,input().split())

# for three integers 
 
a,b,c=map(int,input().split())

# similar we can take many value if we already know the no of given to be given 

# method 3 -> directly take element from the list

a,b,c = list(map(int,input().strip().split()))

# above method can be used for any no of integers...

# some time we have to take input for multiple no of line eg-> for query type of question

query = int(input())
for item in range(query()):
  
  # we can take any no of input as mentain above
  
  a,b=map(int,input().split())
  
  # we can process it or store it

# for storing the values we can create an container like a array or dictionary or list

q = int(input())

container_aslist = []

for item in range(query()):
  
  a,b=map(int,input().split())
  container.append([a,b])

# if you don't know about the append and other method don't worry . I will write some post for you. 

--> the next topic will be on the for loop
