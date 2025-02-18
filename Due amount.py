def due(b,g):
    return g-b
bill = int(input("Enter the Bill amount: "))
given = int(input("Enter the given amount: "))
dueAmount = due(bill, given)
print(f"Due Amount : {dueAmount}")