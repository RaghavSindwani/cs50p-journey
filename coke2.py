amount_due = 50
while amount_due > 0:
  print("amount mode:", amount_due)
  coin = int(input("Insert Coin: " ))
  if coin in [25,5,10]:
    amount_due = amount_due - coin
print("Change owed:", abs(amount_due))
