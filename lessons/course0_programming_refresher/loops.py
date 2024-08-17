# Loop through a list of numbers and print each one
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"Number: {number}")

string = 'Python'

for s in string:
    print(s)

print('Thank you')

i=0
while i<5:
    print(f'before: {i}')
    i=i+1
    print(f'after: {i}')

obj = range(2,50,2)
print(obj)

print(list(obj))

for i in "hello string 3242cinthya":
    if i =="a":
        break
    print(i)