ticket_age = int(input("Ticket age (in hours): "))
impact_level = input("Ticket impact (low/medium/high): ").strip().lower()

if impact_level == "high" and ticket_age > 4:
    priority = "Critical"
elif impact_level == "medium" and ticket_age > 8:
    priority = "High"
else:
    priority = "Normal"

print(f"Ticket Impact: {impact_level}")
print(f"Ticket Age: {ticket_age} hours")
print(f"Priority: {priority}")
