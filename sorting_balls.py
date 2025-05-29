
numbers_list=[]
print('This program will sort the balls in the winners rack.')
for i in range(0,60):
    user_input=input('enter balls to be selected in the winners rack between 0 and 59 (for stopping the value enter -1):')
    if user_input == '-1':
        sorted_list = sorted(numbers_list)
        print('sorted list of balls:', sorted_list)
        break
    try:
        number=int(user_input)
    except ValueError:
        print('Invalid input, please enter a valid integer between 0 and 59 .')

    if number >59 or number < 0:
        print('Invalid input, please enter a number between 0 and 59.')
        continue 
    else:
        numbers_list.append(number)


    
