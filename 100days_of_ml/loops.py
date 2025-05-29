import random

def prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i != 0:
                return True
            else:
                return False      
    else:
        print('Write the num greater than 1')

number1 = -5
if prime_num(number1):
    print(f"{number1} is a prime number.")
else:
    print(f"{number1} is not a prime number.")




num_of_questions = 3
right_answers = 0
operation_list = ['+', '-', '*', '/']

print('Welcome to quiz. Answer at 3 questions and find out your score!!!')

for i in range(0, num_of_questions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 7)

    operation = random.choice(['+', '-', '*', '/'])

    correct_answer = 0

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        correct_answer = num1 / num2
        if num1 % num2 != 0:
            correct_answer = round(correct_answer)

    
    user_answer = int(input(f'Solve the {i + 1}: {num1} {operation} {num2} = '))

    if user_answer == correct_answer:
        print('Right.')
        right_answers += 1
    else:
        print('Wrong.')
    
print(f'Your score is: {right_answers}/{num_of_questions}')