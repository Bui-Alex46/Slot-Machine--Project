import random       #importing modules
#GLOBAL CONST VALUES
MAX_LINES = 3       #ALL CAPS makes a global constant value
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {            #created a dictionary (kind of like an array)
    "A": 2,                 #Key, value
                            #"A" , 2
    "B": 4,
    "C": 6,
    "D": 8
}
#Dictionary to mulitply the winnings depending on the value
symbol_value = {            
    "A": 5,                               
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):       #iterates through the rows
                                    # almost same as saying i < lines.size()
        symbol = columns[0][line]      #checks the first item in each row
        for column in columns:      #
            symbol_to_check = column[line]  #checking the first value in the row
        #lose condition
            if symbol != symbol_to_check:   #Check if symbols are not the same, we breawk
                break  
        #win condition
        else:                               #All symbols are in the same row 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    #Randomly selecting values
    all_symbols = []                                            #creating a list
    for symbol, symbol_count in symbols.items():                #.items() gives you keys(index) and values
                                                                #for loop(A, 2, )
        for _ in range(symbol_count):                           #to loop through something wwithout caring about count or iteration value use underscore "_"
            all_symbols.append(symbol)                          #inserting values from the Dictionary into this new list

    columns = []                                                #Nested list, storing values of columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]            #slice operator, to copy the list [:]
        for _ in range(rows):
            value = random.choice(current_symbols)  #using the random.choice from imported module above in line 1    
                                                    #picks a random value in the copy list 
            current_symbols.remove(value)           #removing value from the list after being picked
            column.append(value)                    #inserting value into column

        columns.append(column)

    return columns                              #Returning list

#TRANSPOING: flips the matrix from horizontal to vertical
#[A B C
# A A A
# A C B]
#We want it to look like
#[A A A
# B A C
# C A B ]
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):                #enumerate() gives you index as well as item 
            if i != len(columns) - 1:                          #len(colums) - 1 is the last maximum index in the list
                print(column[row], end=" | ")               #end is the newline character
                                                            #setting end = | , because it wants to endl when we hit that value

            else:
                print(column[row], end ="")                 #end = "" doesn't print anything
        print()                                         #empty print statement prints a newline character to bring us down to next row

def deposit():
    while True: #While loop
        amount = input("What would you like to deposit? $")                              #is.idgit() chekcs that input is a valid whole number 
        if amount.isdigit():
            amount = int(amount)                 #Converts input into an integer
            if amount > 0:                       #Valid amount so break out of loop
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
     while True: #While loop
        lines = input(
            "Enter the number of lines to bet on (1-" +  str(MAX_LINES) + ")? ")        #str() turns value into a string 
                                                                                        #"+" concatenates string
                                                                                        #its gonna output (1-3) 
                                                    #is.idgit() chekcs that input is a valid whole number 
        if lines.isdigit():
            lines = int(lines)                     #Converts input into an integer
            if 1 <= lines <= MAX_LINES:             #Checks value is in between 2 different values 
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

     return lines

def get_bet():
     while True: #While loop
        amount = input("What would you like to bet on each line? $")                                          
        if amount.isdigit():
            amount = int(amount)                 
            if MIN_BET <= amount <= MAX_BET:                       
                break
            else:
                print(f"Amount must be between ${MIN_BET} -${MAX_BET}.")
        else:
            print("Please enter a number.")

     return amount
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
   
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)        #unpack operator, pass the 
    
    return winnings - total_bet

def main():     #Def is creating a function
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()  #calling main function

