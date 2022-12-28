print("Welcome to the Gemstones Shop!")
gemstone_prompt = print('Which gemstone would you like to collect?\n'
                "1. diamond\n"
                "2. ruby\n"
                "3. emerald\n"
                "4. sapphire\n"
                "5. Exit\n\n"
                "Please enter your choice (1-5):",str(input()))
total_diamonds=0
total_rubies=0
total_emeralds=0
total_sapphires=0

def convert_new_total(gem_amount):
    total=gem_amount
    return total

while gemstone_prompt=='1' or gemstone_prompt=='2' or gemstone_prompt=='3'or gemstone_prompt=='4' or gemstone_prompt=='5': 
    if gemstone_prompt == '1':
        print(f'How many diamonds would you like to collect?')
        diamond_amount=int(input())
        total_rubies=convert_new_total(diamond_amount)
        gemstone_prompt
    elif gemstone_prompt == '2':
        print(f'How many rubies would you like to collect?')
        ruby_amount=int(input())
        total_rubies=convert_new_total(ruby_amount)
        gemstone_prompt
    elif gemstone_prompt == '3':
        print(f'How many emeralds would you like to collect?')
        emerald_amount=int(input())
        total_emeralds=convert_new_total(emerald_amount)
        gemstone_prompt
    elif gemstone_prompt == '4':
        print(f'How many sapphires would you like to collect?')
        sapphire_amount=int(input())
        total_sapphires=convert_new_total(sapphire_amount)
        gemstone_prompt
    elif gemstone_prompt=='5':
        print('Invalid input.\n')
        gemstone_prompt
    else:
        ending_menu=print(f'1. diamond {total_diamonds} \n'
                f'2. ruby {total_rubies} \n'
                f'3. emerald {total_emeralds} \n'
                f'4. sapphire {total_sapphires} \n')
        exit()





