from Helpers import *
from Options import *
import os

#To start the ticket viewer, enter python3 run.py

def main():
    
    print('\nWelcome to Zendesk Ticket Viewer. You are viewing Abhinav Bipin\'s Tickets.\n')

    #setting up credentials to connect to API
    url = 'https://zccabipin.zendesk.com/api/v2/tickets.json'
    user = os.environ.get('user')
    password = os.environ.get('password')

    # tickets
    ticket_list = getTickets(url, user, password)

    # page = 0 # Will keep of which page user is currently on, each page is 25 tickets max
    # choice = '' # will keep track of user's choice
    displayTickets(ticket_list, 0) # show first 25 tickets
    pageViewer(ticket_list, 0, '') # method that allows user to navigate, will not return until user quits

    print ('\nThanks for using Zendesk! Have a great day.\n') # end statement


if __name__ == "__main__":
    main()