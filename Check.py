TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(num):
    return (num * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("Please type your name: ")
    print("Hello, {}!!".format(name))
    num_tickets = input("How many tickets would you like? ")
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Uh oh... we ran into an issue :( \n{}\nPlease try again!".format(err))
    else:
        final_price = calculate_price(num_tickets)
        print("Your price of {} tickets will be: {}".format(num_tickets, final_price))

        answer = input("Would you like to proceed, {}? \nY/N ".format(name))
        if answer.lower() == "y":
            print("S O L D !")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))

print("Sorry, the tickets are all sold out!")