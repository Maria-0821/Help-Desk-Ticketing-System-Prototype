class Ticket:
    # assigned static ticket number
    ticket_number = 2000
    # total number of tickets stored in list for display
    total_tickets = []

    # List of status
    ticket_status_list = ["OPEN", "CLOSED", "REOPENED"]
    # assigned array to reduce redundancy for typing OPEN CLOSED and REOPENED

    # initial assignment of tickets statistics
    tickets_created = 0
    tickets_to_solve = 0
    tickets_resolved = 0

    # class constructor with default values.
    def __init__(self,
                 staff_id=None,
                 ticket_creator_name=None,
                 contact_email=None,
                 description_issue=None,
                 ticket_response="NOT YET PROVIDED",
                 ticket_status="OPEN"):

        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.description_issue = description_issue
        self.ticket_status = ticket_status
        self.ticket_response = ticket_response

        # if condition to check all the given params are not null then increment in statistics.
        if staff_id is not None and ticket_creator_name is not None and description_issue is not None and contact_email is not None:
            Ticket.ticket_number += 1
            Ticket.tickets_created += 1
            Ticket.tickets_to_solve += 1
        # increment the value at starting from 2001
        self.ticket_number = Ticket.ticket_number

    # function for submitting the ticket
    def submit_ticket(self, ticket):
        # if description issue lies related to password generator.
        is_pass = ticket.description_issue
        if "password" in is_pass.lower():
            successful_password_change = self.password_generator(ticket)
            # if password is successfully generated.

            if successful_password_change:
                ticket.ticket_status = Ticket.ticket_status_list[1] # index 1 represents CLOSED
                Ticket.tickets_to_solve -= 1
                Ticket.tickets_resolved += 1
        # append the value in ticket objects list assigned above.
        Ticket.total_tickets.append(ticket)

    # print the ticket
    def print_ticket(self):
        if len(Ticket.total_tickets) == 0:
            return False
        print("Printing Tickets:\n")
        for tickets in Ticket.total_tickets:
            print("Ticket Number: ", tickets.ticket_number,
                  "\nTicket Creator: ", tickets.ticket_creator_name,
                  "\nStaff ID: ", tickets.staff_id,
                  "\nEmail Address: ", tickets.contact_email,
                  "\nDescription: ", tickets.description_issue,
                  "\nResponse: ", tickets.ticket_response,
                  "\nTicket Status: ", tickets.ticket_status, "\n"
                  )

        return True



    # print the ticket statistics
    def print_ticket_statistics(self):
        print("Displaying Ticket Statistics:\n")
        print("Tickets Created:  ", Ticket.tickets_created)
        print("Tickets Resolved: ", Ticket.tickets_resolved)
        print("Tickets To Solve: ", Ticket.tickets_to_solve, "\n")

    # generate a new password
    def password_generator(self, ticket):
        # slice the first two characters from staff_id
        two_char_staff_id = ticket.staff_id[0:2]
        # slice the first 3 characters from creator name
        three_char_creator_name = ticket.ticket_creator_name[0:3]

        # append both the characters using string operator
        generate_password = two_char_staff_id + three_char_creator_name

        # update the response
        ticket.ticket_response = "New Password Generated: " + generate_password
        return two_char_staff_id is not None

    # it is invoked to search for available ticket.
    def search_ticket(self, ticket_number):
        for ticket in Ticket.total_tickets:
            if ticket.ticket_number == ticket_number:
                return ticket
        return None

    # it is invoked to print only opened tickets
    def print_open_tickets(self):
        count_ticket = 0
        if len(Ticket.total_tickets) == 0:
            return False
        for tickets in Ticket.total_tickets:
            if tickets.ticket_status != Ticket.ticket_status_list[1]:
                count_ticket += 1
                print("Ticket Number: ", tickets.ticket_number,
                      "\nTicket Creator: ", tickets.ticket_creator_name,
                      "\nStaff ID: ", tickets.staff_id,
                      "\nEmail Address: ", tickets.contact_email,
                      "\nDescription: ", tickets.description_issue,
                      "\nResponse: ", tickets.ticket_response,
                      "\nTicket Status: ", tickets.ticket_status, "\n"
                      )
        return count_ticket > 0

    # it is invoked to print only closed tickets, it is used later for reopening closed tickets
    def print_closed_tickets(self):
        count_ticket = 0
        if len(Ticket.total_tickets) == 0:
            return False
        for tickets in Ticket.total_tickets:
            if tickets.ticket_status == Ticket.ticket_status_list[1]:
                count_ticket += 1
                print("Ticket Number: ", tickets.ticket_number,
                      "\nTicket Creator: ", tickets.ticket_creator_name,
                      "\nStaff ID: ", tickets.staff_id,
                      "\nEmail Address: ", tickets.contact_email,
                      "\nDescription: ", tickets.description_issue,
                      "\nResponse: ", tickets.ticket_response,
                      "\nTicket Status: ", tickets.ticket_status, "\n"
                      )
        return count_ticket > 0

    # reopen the closed tickets
    def reopen_ticket(self, ticket_number):
        searched_ticket = self.search_ticket(ticket_number)
        if searched_ticket is not None and searched_ticket.ticket_status != Ticket.ticket_status_list[0]: # 0 represents OPEN
            if searched_ticket.ticket_status == Ticket.ticket_status_list[1]:
                searched_ticket.ticket_status = Ticket.ticket_status_list[2]
                Ticket.tickets_to_solve += 1
                Ticket.tickets_resolved -= 1
                return True
        return False

    # setters
    def set_ticket_status(self, ticket, ticket_status):
        ticket.ticket_status = ticket_status

    def set_ticket_response(self, ticket, ticket_response):
        ticket.ticket_response = ticket_response

    # respond to tickets
    def respond_to_tickets(self, ticket, ticket_response, ticket_status):

        self.set_ticket_response(ticket, ticket_response) # update the response
        # to check if the client wants to change the status of ticket
        if ticket_status == Ticket.ticket_status_list[2] or ticket_status == "No Change":
            return False
        elif ticket.ticket_status == ticket_status:
            return False

        self.set_ticket_status(ticket, ticket_status)
        Ticket.tickets_resolved += 1
        Ticket.tickets_to_solve -= 1

        return True
