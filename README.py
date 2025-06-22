# Daily-practices
# Daily practices


text = "data science is amazing"
vowels = 'aeiou'
count = 0
for i in text:
    if i in vowels:
        count += 1    # this will use to add the count if the vowels words in vowels
print(count)

#######################################

A = ('Bosco')

B = ''.join(reversed(A)) #this is use to reverse the words from (A)

if A==B:
    print(f'this is palindome {B}') #if it is palindome it will print palidome
else:
    print(f'this is not a palindome {B}\nthe original word is {A}') #if it is not palindome it will print not palidome also the original word


######################################

A = ('kcart ecneics atad eht tuoba lla si siht iH')

B = A.split()                     #this is split the variable and make them as list

C = [word[::-1] for word in B]      #this code is used to reverse the words

D = ' '.join(reversed(C))         #this code is use to add the word that was reversed already.

print(D)


######################################

#Print the first N prime numbers 

A = int(input('Kindly enter the number of prime numbers we need to find : '))

def prime(X):                                #This function is used to find that if the number divisable by iterate number then it throws false 
    if X<2:
        return False                     
    for i in range(2,X):
        if X%i ==0:
            return False
    return True                            # if its not divisable by iterate number then its throws true 

score = 0 
start = 2

while (score<A):                            #This line is used to run the loop till its greater then A
    if prime(start):
        print(start,end=' ')
        score +=1                            #Then after the loop run it will increase the score value 
    start +=1                                #Then after the loop run it will increase the start value 

########################################################


# Combine file handling and classes
# Modify your student manager project to use a `Student` class
# Add methods to save/load student data to/from a file

class student():

    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
    
    def display(self):
        print(f'{self.name},{self.age},{self.roll}')
    
data = {}

def A():
    N = int(input('Kindly enter the number of students your going to enter :').strip())
    for i in range(N):
        name, age, roll = input('Enter the details of the students (name,age,roll_no):').split()
        data[roll] = student(name,age,roll)
    print('uploaded')

def displays():
    for i , j in data.items():
        j.display()

def upload():
    A = input('do you want to upload this details into files (yes/no)').strip().lower()
    if A == 'yes':
        with open (r'Bosco.txt','w') as file:
            for i,j in data.items():
                file.write(f'{j.name},{j.age},{j.roll}\n')
        print('uploaded')
    else:
        print('Notes thanks')

A()
displays()
upload()
displays()
        
