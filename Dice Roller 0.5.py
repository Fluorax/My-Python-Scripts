#!/usr/bin/env python3
import random
my_dice=[2,4,6,8,10,12,20,100]
times_rolled=0

print('Thanks for trying DnD dice roller')
print('The supported dice formats in this version are the following:')
print('d2, d4, d6, d8, d10, d12, d20 and d100.')
print('Please note that during dice format selection it is', 'not necessary to include the d- prefix.', sep='\n')

def valid_dice():
    local_dice_format=random.choice(my_dice)
    while True:  
        try:
            local_dice_format = int(input('Please select a dice format:'))
            if local_dice_format in my_dice:
                global dice_format
                dice_format = local_dice_format
                print('Thank you. Please select # of rolls:',end =" ")
                break
            else:
                print('Format not supported.')
        except ValueError:
            print('Format not supported.')
            
def valid_roll():
    local_roll_number=random.randint(1,10000000)
    while True:
        try:
            local_roll_number = int(input())
            if local_roll_number > 0:
                global roll_number
                roll_number = local_roll_number
                break
            else:
                print('Input not valid, please select a positive number:',end='')
                continue
        except:
            print('Format not supported, please enter a valid input:',end =" ")
        
def random_numbers():                         
    local_numbers = [random.randint(1,dice_format) for i in range(roll_number)]
    print('You rolled:',','.join(str(n) for n in local_numbers))
    global numbers
    numbers = local_numbers

while True:
    if times_rolled >= 1:
        print('Total rolls:', str(times_rolled))
    valid_dice()
    valid_roll()
    random_numbers()
    times_rolled=times_rolled+1
    if dice_format == 20 and 20 in numbers:
        print('Critical, nice!')
    

