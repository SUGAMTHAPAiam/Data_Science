# Personal Spending Tracker
# Tracks spending over 3 days and checks it against a daily and overall budget.
 
name = input("Enter your Name: ")
total_spent = 0
 
for day in range(1, 4):
    spent = float(input("Enter money spent today ($): "))
    total_spent = total_spent + spent
 
    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")
 
print("Total money spent over 3 days: $" + str(total_spent))
 
if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")