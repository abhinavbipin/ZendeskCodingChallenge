# ZendeskCodingChallenge

This project connects to the Zendesk API, make http requests to retrieve all the tickets, and displays them in a command line interface.



## Instructions
To run the program, you only need run.py, Options.py, and Helpers.py.
Once you have these three programs in the same folder, all you need to do is run run.py in your IDE, or 
manuver to the folder with these files and enter 'python run.py' in your command line. 
You will need to have the requests library installed (use pip install requests). 

### Files
- run.py starts the ticket viewer and the menu.
- Options.py contains methods that display th users options to manuver through the ticket viewer.
- Helpers.py contains methods that are used in run.py and Options.py.
- test_ticketviewer.py contains tests methods for the ticket viewer.
- constants.py contains constants used by the test method.
- tickets.json contains ticket objects used to PUSH to the API (not used for ticket viewer).

### Features
- Displays all tickets in the Zendesk API for the given user (me), 25 at a time. 
- Displays total tickets, the number of tickets currently displayed, the current page and total pages.
- User has ability to travel between pages by going forward one, backward one, or to a page of their choice.
- User can choose to view any ticket, and get furthr details than shown in the inital display.
- User can quit when desired. 
- Simple, straightforward instructions and options for the user to view tickets that handles improper user input. 


