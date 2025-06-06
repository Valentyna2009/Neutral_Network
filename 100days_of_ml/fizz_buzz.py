# Task: print numbers from 1 to 100
# For multiples of 3, print “Fizz” instead of the number.

# For multiples of 5, print “Buzz” instead of the number.

# For numbers which are multiples of both 3 and 5, print “FizzBuzz”.

def print_num(num):
    for i in range(1, num):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        
        elif i % 3 == 0:
            print('Fizz')
        
        elif i % 5 == 0:
            print('Buzz')

        else:
            print(i)

num1 = 100
print_num(num1)