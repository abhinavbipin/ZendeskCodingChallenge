import os
import unittest
from Helpers import *
from Options import *
import requests
import json
import ticketListModel as model
from io import StringIO
from unittest import mock
from unittest.mock import patch



class Test_Ticket_Viewer(unittest.TestCase):

    def test_get_tickets(self): # tests whether local ticket list has right amount

        url = 'https://zccabipin.zendesk.com/api/v2/tickets.json'
        user = os.environ.get('user')
        password = os.environ.get('password')

        response = requests.get(url, auth=(user, password))

        if response.status_code != 200: # HTTP code has to be 200, otherwise stop
            print('Status:', response.status_code, ':(\nProblem with the request. API may be unavailable. Exiting.')
            exit()

        data = response.json()

        self.assertEqual(len(getTickets(url, user, password)), data['count'])

    def run_pageview_test(self, given_answer, expected_out, tickets, page): #from StackOverflow
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            pageViewer(tickets, page, '')
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_page_view_basic(self):
        tickets1 = model.TICKETLISTMODEL.copy()
        self.run_pageview_test('q', 'Press F to go forward one page\nPress C to choose a specific page to go to\nPress S to view a single ticket\nPress Q to quit', tickets1, 0)
        self.run_pageview_test('q', 'Press B to go backward one page\nPress C to choose a specific page to go to\nPress S to view a single ticket\nPress Q to quit', tickets1, 1)

    def test_page_view_one_page(self):
        tickets2 = model.TICKETLISTMODEL.copy()
        tickets2.pop()
        
        self.run_pageview_test('q', 'Press S to view a single ticket\nPress Q to quit', tickets2, 0)

    def test_page_view_101tickets(self):
        tickets3 = model.TICKETLISTMODEL.copy()
        spare = tickets3.pop()
        tickets3 += tickets3
        tickets3 += tickets3
        tickets3.append(spare)

        self.run_pageview_test('q', 'Press F to go forward one page\nPress B to go backward one page\nPress C to choose a specific page to go to\nPress S to view a single ticket\nPress Q to quit', tickets3, 3)
        self.run_pageview_test('q', 'Press F to go forward one page\nPress C to choose a specific page to go to\nPress S to view a single ticket\nPress Q to quit', tickets3, 0)
        self.run_pageview_test('q', 'Press B to go backward one page\nPress C to choose a specific page to go to\nPress S to view a single ticket\nPress Q to quit', tickets3, 4)

    def run_displaytickets_test(self, given_answer, expected_out, tickets, page, num_chars): #from StackOverflow
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            display_tickets(tickets, page)
            self.assertEqual(fake_out.getvalue().strip()[:num_chars], expected_out)
    
    def test_displaytickets_displayed(self):
        tickets4 = model.TICKETLISTMODEL.copy()
        spare = tickets4.pop()
        tickets4 += tickets4
        tickets4 += tickets4
        tickets4.append(spare)

        self.run_displaytickets_test('', model.DISPLAYALL1, tickets4, 0, len(model.DISPLAYALL1))
        self.run_displaytickets_test('', model.DISPLAYALL2, tickets4, 1, len(model.DISPLAYALL2))
        self.run_displaytickets_test('', model.DISPLAYALL3, tickets4, 4, len(model.DISPLAYALL3))


    def test_displaytickets_pages(self):

        tickets5 = model.TICKETLISTMODEL.copy()
        spare = tickets5.pop()
        tickets5 += tickets5
        tickets5 += tickets5
        tickets5.append(spare)

        self.run_displaytickets_test('', model.DISPLAYSUMMARY1, tickets5, 4, len(model.DISPLAYSUMMARY1))

        tickets5.pop()
        self.run_displaytickets_test('', model.DISPLAYSUMMARY2, tickets5, 3, len(model.DISPLAYSUMMARY2))

        tickets5.pop()

        self.run_displaytickets_test('', model.DISPLAYSUMMARY3, tickets5, 3, len(model.DISPLAYSUMMARY3))

        tickets5+= tickets5

        self.run_displaytickets_test('', model.DISPLAYSUMMARY4, tickets5, 7, len(model.DISPLAYSUMMARY4))
        self.run_displaytickets_test('', model.DISPLAYSUMMARY5, tickets5, 6, len(model.DISPLAYSUMMARY5))
        
        tickets5.append(spare)
        tickets5.append(spare)
        tickets5.append(spare)

        self.run_displaytickets_test('', model.DISPLAYSUMMARY6, tickets5, 7, len(model.DISPLAYSUMMARY6))
        self.run_displaytickets_test('', model.DISPLAYSUMMARY7, tickets5, 8, len(model.DISPLAYSUMMARY7))


    # def run_singleticket_test(self, given_answer1, given_answer2, expected_out, tickets, page, num_chars): #from StackOverflow
    #     result = ''
    #     with patch('builtins.input', return_value=given_answer2), patch('sys.stdout', new=StringIO()) as fake_out2:
    #         with patch('builtins.input', return_value=given_answer1), patch('sys.stdout', new=StringIO()) as fake_out1:
    #             singleTicket(tickets, page)
    #             result += fake_out1.getvalue().strip()
    #         result += fake_out2.getvalue().strip()
    #         self.assertEqual(result, expected_out)

    def test_singleTicket_display(self):
        tickets6 = model.TICKETLISTMODEL.copy()
        with mock.patch()
        #self.run_singleticket_test('1', 'q', model.DISPLAYSINGLE1, tickets6, 0, len(model.DISPLAYSINGLE1))


    def test_singleTickets_back(self):


        
        
if __name__ =='__main__':
    unittest.main()
    #display_tickets()


