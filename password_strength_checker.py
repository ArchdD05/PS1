

satisfied_password=False
while satisfied_password==False:
    type=input('Are you a user or admin:').strip().lower()
    if type =='user':
        count_letter=0
        count_digit=0
        password=input('Enter your password:').strip()
        if len(password)<7:
            print('Password must be at least 7 characters long.')
        for letter in password:
            if letter>='a' and letter<='z' or letter>='A' and letter<='Z':
                count_letter+=1
                continue
            elif letter>='0' and letter<='9':
                count_digit+=1
                continue
        if count_letter == 0:
            print('Password must contain at least one letter.')
        elif count_digit == 0:
            print('Password must contain at least one digit.')
        if len(password)>7 and count_letter > 0 and count_digit > 0:
            print('Password is valid.')
            satisfied_password=True
    elif type=='admin':
        special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        
        count_letter=0
        count_digit=0
        special_char=0
        password=input('Enter your password:').strip()
        if len(password)<10:
            print('Password must be at least 10 characters long.')
        for letter in password:
            if letter>='a' and letter<='z' or letter>='A' and letter<='Z':
                count_letter+=1
                continue
            elif letter>='0' and letter<='9':
                count_digit+=1
                continue
            elif letter in special_characters:
                special_char+=1
                continue
            
        if count_letter == 0:
            print('Password must contain at least one letter.')
        elif count_digit == 0:
            print('Password must contain at least one digit.')
        elif special_char == 0:
            print('Password must contain at least one special character.')
        if len(password)>10 and count_letter > 0 and count_digit > 0 and special_char > 0:
            print('Password is valid.')
            satisfied_password=True
    else:
        print('Invalid input, please enter either "user" or "admin".')
