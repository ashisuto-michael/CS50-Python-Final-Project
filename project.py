# Declare global variables
global totalRoom, availableRoom, gameStarted

# Function to order food
def orderFood(food):
    if food == "1":
        print("\nMa ma mia!")
    elif food == "2":
        print("\nSlurp!")
    else:
        print("Invalid")

# Function to book room
def bookRoom(avRoom, room):
    if room <= avRoom:
        return avRoom - room
    elif room > avRoom:
        print("Not enough rooms!")
        return avRoom

# Function to call room service
def hotelService(tot,av):
    tot = int(tot)
    av = int(av)
    result = av/tot
    testBusy = 1 - result
    if testBusy <= 0.5:
        print("On my way! Meow!")
    else:
        print("Too busy!")

# Function to terminate program
def terminateHotel(inp):
    inp = 0
    print("Thank you for playing!")
    return inp

# Function if option is not valid
def invalidOption():
    print("That was not among the options...")

# The main function
def main():
    startOrNot = input("\nLaunch Hotel Management System? (y/n): ")

    if startOrNot == "y":
        gameStarted = 1
        totalRoom = input("Initialise starting number of rooms: ")
        availableRoom = int(totalRoom)
        while gameStarted == 1:
            print("\n/ᐠ｡ꞈ｡ᐟ\ Welcome to Nyanko Hotel! What would you like to do?\n")
            options = input("1. Order food    2. Book Room    3. Room Service    4. Terminate\n")
            if options == "1":
                whatFood = input("\nWhat food would you like?\n 1. Pizza    2. Tequila\n")
                orderFood(whatFood)
            elif options == "2":
                roomQuantity = int(input("\nHow many rooms to book?\n"))
                availableRoom = bookRoom(availableRoom,roomQuantity)
                print(f'Rooms left: {availableRoom}')
            elif options == "3":
                hotelService(totalRoom,availableRoom)
            elif options == "4":
                gameStarted = terminateHotel(gameStarted)
            else:
                invalidOption()
    elif startOrNot == "n":
        print("Game was not launched... party pooper!!")
    else:
        print("Invalid input, try again.")

# Start program
if __name__ == "__main__":
    main()
