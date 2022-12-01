import HelpDeskTicketingSystem as HelpDesk


class Main(HelpDesk.Ticket):

    def main(self):
        print("...Welcome To Help Desk Ticketing System...")

        # run the program
        while True:
            # print the options i-e staff and it team
            choose_portal = self.print_option()

            match choose_portal:
                # staff is selected
                case "1":
                    staff_id = ""
                    while True:
                        staff_id = str(input("Enter Staff ID: "))
                        if len(staff_id) < 2:
                            print("Staff ID can't be less than 2 characters")
                            continue
                        else:
                            break
                    while True:
                        choose_staff_option = self.print_staff_main_menu()
                        match choose_staff_option:
                            case "1":
                                ticket_creator_name = ""
                                while True:
                                    ticket_creator_name = str(input("Enter Ticket Creator Name: "))
                                    if len(ticket_creator_name) < 3:
                                        print("Ticket creator name can't be less than 3 characters")
                                        continue
                                    else:
                                        break

                                ticket_contact_email = str(input("Enter Contact Email: "))
                                ticket_description_issue = str(input("Describe Your Issue: "))

                                create_ticket = HelpDesk.Ticket(staff_id, ticket_creator_name, ticket_contact_email,
                                                                ticket_description_issue)
                                self.submit_ticket(create_ticket)

                                print("Ticket Submitted Successfully")

                            case "2":
                                self.print_ticket_statistics()
                            case "3":
                                print_ticket = self.print_ticket()
                                if not print_ticket:
                                    print("Ticket not available at the moment")
                                    continue
                            case "4":
                                self.print_ticket_statistics()
                                print_ticket = self.print_ticket()
                                if not print_ticket:
                                    print("Ticket not available at the moment")
                                    continue

                            case "5":
                                break

                case "2":

                    while True:
                        choose_team_option = self.print_it_team_main_menu()

                        match choose_team_option:
                            case "1":
                                if not self.print_open_tickets():
                                    print("Ticket not available at the moment")
                                    continue

                                count = 0
                                is_available = None
                                while count != 3:
                                    try:
                                        ticket_number = int(input("Enter Ticket Number: "))
                                    except:
                                        print("Please Enter Numeric Value")
                                        continue
                                    is_available = self.search_ticket(ticket_number)
                                    if is_available is None:
                                        print("Ticket Not Found")

                                        count += 1
                                        continue
                                    break

                                ticket_response = str(input("Enter Ticket Response: "))

                                ticket_status = str(input("Change Ticket Status\n"
                                                          "1. CLOSE\n"
                                                          "2. No Change\n"
                                                          "Enter: "))
                                match ticket_status:
                                    case "1":
                                        ticket_status = "CLOSED"
                                    case "2":
                                        ticket_status = "No Change"

                                print(ticket_status)
                                response = self.respond_to_tickets(is_available, ticket_response, ticket_status)

                                if response:
                                    print("Ticket Successfully Responded")
                                else:
                                    print("Ticket Response Changed, Status Remained Same")

                            case "2":
                                self.print_ticket_statistics()

                            case "3":
                                print_ticket = self.print_ticket()
                                if not print_ticket:
                                    print("Ticket not available at the moment")
                                    continue
                            case "4":
                                self.print_ticket_statistics()
                                print_ticket = self.print_ticket()
                                if not print_ticket:
                                    print("Ticket not available at the moment")
                                    continue

                            case "5":
                                show_tickets = self.print_closed_tickets()

                                if not show_tickets:
                                    print("Ticket not available at the moment")
                                    continue

                                count = 0
                                is_available = None
                                ticket_number = 0
                                while count != 3:
                                    try:
                                        ticket_number = int(input("Enter Ticket Number: "))
                                    except:
                                        print("Please Enter Numeric Value")
                                        continue
                                    is_available = self.search_ticket(ticket_number)
                                    if is_available is None:
                                        print("Ticket Not Found")

                                        count += 1
                                        continue
                                    break
                                if self.reopen_ticket(ticket_number):
                                    print("Ticket Reopened Successfully.")
                                else:
                                    print("Ticket Can't be opened")

                            case "6":
                                break

    def print_option(self):
        return str(input("1. Staff Portal\n2. IT Team Portal\nEnter: "))

    def print_staff_main_menu(self):
        return str(input("1. Submit Ticket\n"
                         "2. Print Ticket Statistics\n"
                         "3. Print Ticket Information\n"
                         "4. Print Detailed Ticket Information\n"
                         "5. Go Back\n"
                         "Enter: "))

    def print_it_team_main_menu(self):
        return str(input("1. Respond Ticket\n"
                         "2. Print Ticket Statistics\n"
                         "3. Print Ticket Information\n"
                         "4. Print Detailed Ticket Information\n"
                         "5. Reopen Ticket\n"
                         "6. Go Back\n"
                         "Enter: "))


Main().main()
