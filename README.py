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
