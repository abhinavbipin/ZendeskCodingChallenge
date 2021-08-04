import math
from Helpers import *

#menus that set up what the user an choose and responds appropriately. One for the options on each page, one for a single ticket

def pageViewer(ticket_list, page, choice):
    #will keep going until user quits
    while(type(page) != int or page < 0 or page > math.ceil((len(ticket_list)/25)-1)):
        print('Please enter a valid page number')
        page = input()

    while (choice != 'Q'):

        #shows options. options will be limits baseed on which page user is on (EG cant go back from first page)
        if (math.ceil(len(ticket_list)/25) >page+1):
            print('Press F to go forward one page')

        if (page > 0): 
            print('Press B to go backward one page')

        if (len(ticket_list)>25): 
            print('Press C to choose a specific page to go to')


        print('Press S to view a single ticket')
        print('Press Q to quit')

        #user's input
        choice = str(input()).capitalize()

        if (choice == 'F'): 
            #if they choose forward and its a valid option, display tickets of next page
            if (len(ticket_list)>25 and math.ceil(len(ticket_list)/25) >page+1):
                page+=1
                displayTickets(ticket_list, page)

        elif(choice == 'B'):
            #if they choose backward and its a valid option, display tickets of previous page
            if (page > 0):
                page -=1
                displayTickets(ticket_list, page)


        elif(choice == 'C'):
            #if they choose a specific page, make sure they enter a valid page number
            num = 0
            while(type(num) != int or num < 1 or num > math.ceil((len(ticket_list)/25))):
                print('Which page number do you want to see?')
                try:
                    num = int(input())
                    if (num >math.ceil((len(ticket_list)/25)) or num < 1): print('Please enter the number a valid page number')
                except ValueError:
                    print('Please enter a number')
            
            #show that page
            page = num - 1
            displayTickets(ticket_list, page)

        #or if they wanna see a single ticket, new set up
        elif(choice == 'S'): choice = singleTicket(ticket_list, page)

#Displays more information about a single ticket
def singleTicket(ticket_list, page):

    num = '' #which ticket

    #making sure they enter a valid ticket number
    while (type(num) != int) or num >len(ticket_list) or num < 1:
        print('Which ticket number do you want to see?')
        try:
            num = int(input())
            if (num >len(ticket_list) or num < 1): print('Please enter the number of a valid ticket')
        except ValueError:
            print('Please enter a number')       

    #print detail about the ticket
    ticket = ticket_list[num-1]
    print('Ticket number:', ticket['id'])
    print('Created at:', ticket['created_at'])
    print('Last updated:', ticket['updated_at'])
    print('Priority:', ticket['priority'])
    print('Status:', ticket['status'])
    print('Description:', ticket['description'])
    print()

    # wait for user to go back
    choice = ''
    while (choice != 'B' and choice != 'Q'):
        print('Press B to go back to view the whole page of tickets')
        print('Press Q to quit')
        choice = str(input()).capitalize()

    if choice == 'B':
        #display ticket of the page we were on before setting up options again
        displayTickets(ticket_list, page)
        return 'B'
    else: return 'Q'