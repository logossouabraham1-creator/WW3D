username = "admin"
password = "secret123"
balance = 1000
user_name = input('Username : ')
if user_name == username : 
    user_passcode = input('Password : ')
    if user_passcode == password :
        print('Welcome Admin!')
        print('1. Check Balance ')
        print('2. Withdraw Money ')
        print('3. Deposit Money ')
        user_option = int(input('Choose an option(1-3) :'))
        if user_option == 1 :
            print('Current Balance :',balance) 
        elif user_option == 2 :
            user_amount = int(input('Amount : '))
            if user_amount > 0 and user_amount <= balance:
                balance -= user_amount 
                print('Withdrawal successful ')
                print('Current Balance:',balance)
            else :
                print('Insufficient funds ')
        elif user_option == 3 :
            user_deposit = int(input('Amount : '))
            if user_deposit > 0 :   
                balance += user_deposit
                print('Deposit succuessful ')
                print('Current Balance:',balance)
        else :
            print('Invalid option ')
    else :
        print('Incorrect password')
else :
    print('Unknown User ')