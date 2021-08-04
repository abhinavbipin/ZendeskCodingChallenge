import math
import requests

#methods used by the viewers or by main

# Displays the ticket of the page the user is currently on
def displayTickets(ticket_list, page):

    while(type(page) != int or page < 0 or page > math.ceil((len(ticket_list)/25)-1)):
        print('Please enter a valid page number')
        page = input()

    #prints logistics of all tickets and page
    print('\nTotal tickets: {}  Tickets displayed: {}  Page: {}/{}\n'.format(len(ticket_list), min((len(ticket_list)- page *25 ), 25), page+1, math.ceil(len(ticket_list)/25)))
    
    for i, ticket in enumerate(ticket_list):
        # display 25 tickets of the current page
        if (i >=page*25 and i  < (page+1)*25): 
            print('#{}. Ticket with id {} about "{}" is {} with priority {}.'.format(i+1, ticket['id'], ticket['subject'], ticket['status'], ticket['priority']))
    
    print()

    #gets tickets. 
def getTickets(url, user, password):

    #connect to API
    response = requests.get(url, auth=(user, password))

    if response.status_code != 200: # HTTP code has to be 200, otherwise stop
        print('Status:', response.status_code, ':(\nProblem with the request. API may be unavailable. Exiting.')
        exit()

    data = response.json()
    ticket_list = data['tickets'] #first page

    #Goes through any more pages of tickets from the API
    while (data['next_page'] != None):
        url = data['next_page']
        response = requests.get(url, auth=(user, password))

        if response.status_code != 200: # HTTP code has to be 200
            print('Status:', response.status_code, ':(\nProblem with the request. API may be unavailable. Exiting.')
            exit()

        data = response.json()
        ticket_list = ticket_list + data['tickets']

    return ticket_list