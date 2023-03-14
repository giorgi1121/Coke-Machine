#create variable due with value
due = 50

#loop which prints same before due will be 0 or less
while True:
    print("Amount due: " + str(due))
    coin = int(input("Insert coin: "))
    
    #check if inserted coins are 5, 10 or 25
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin
    
    #if due is equal to 0 or less break the loop
    if due <= 0:
        print("Change owed: " + str(abs(due)))
        break
