ticket_msg = input("Enter the ticket message: ")

ticket_msg = ticket_msg.strip()          # remove extra spaces
ticket_msg = ticket_msg.lower()           # convert to lowercase
ticket_msg = ticket_msg.replace("error", "issue")

print(ticket_msg)
