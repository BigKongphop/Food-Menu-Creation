menu_list = []
amt_list = []
price_list = []
def add() :
  print("~"*50)
  print("%27s"%("Menu"))
  print("%34s"%("Add bread in order"))
  print("~"*50)
  print("%8s %18s %21s"%("Menu ID", "Menu", "Baht"))
  print("%5s %24s %18s"%("1", "Cherry Pie", "150"))
  print("%5s %18s %24s"%("2", "Tart", "120"))
  print("%5s %22s %20s"%("3", "Baguette", "80"))
  print("%5s %23s %19s"%("4", "Croissant", "60"))
  print("%5s %21s %21s"%("5", "Challah", "40"))
  print("%5s %24s %18s"%("6", "Cheese Bun", "40"))
  print("%5s %21s %21s"%("7", "Pretzel", "35"))
  print("%5s %25s %17s"%("8", "Fancy Bread", "25"))
  print("%5s %20s %22s"%("9", "Bagels", "15"))
  print("~"*50)
  print("['ENTER 0 TO EXIT']")
  a = 1
  while a > 0 :
    menu = int(input("Enter Menu ID(0-9) : "))
    if menu == 1 :
      menu_list.append("Cherry Pie")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 150
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Cherry Pie %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 2 :
      menu_list.append("Tart")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 120
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Tart %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 3 :
      menu_list.append("Baguette")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 80
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Beguette %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 4 :
      menu_list.append("Croissant")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 60
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Croissant %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 5 :
      menu_list.append("Challah")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 40
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Challah %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 6 :
      menu_list.append("Cheese Bun")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 40
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Cheese Bun %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 7 :
      menu_list.append("Pretzel")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 35
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Pretzel %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 8 :
      menu_list.append("Fancy Bread")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 25
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Bread %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 9 :
      menu_list.append("Bagels")
      amt = int(input("Enter Amount(NO.Only) : "))
      if amt > 0 :
        amt_list.append(amt)
        price = 15
        sum_price = price * amt
        price_list.append(sum_price)
        print("Add Bagels %s Slice"%(amt))
        print("          V          ")
      else :
        print(['PLEASE ENTER ONLY POSITIVE NUMBER'])
        print()
    elif menu == 0 :
      a = a - 2
    else:
      print("['PLEASE TRY AGAIN']")
      print()
def dele() :
  print("~"*50)
  print("%35s"%("Cancel bread in order"))
  print("~"*50)
  print("%5s %22s %20s"%("Menu", "Amount", "Baht"))
  c = 0
  while c < len(amt_list):
    print("%s.%-11s %14d %20d"%(c+1,menu_list[c], amt_list[c], price_list[c]))
    c = c + 1
  print("~"*50)
  print("['ENTER 0 TO EXIT']")
  d = 1
  while d > 0 :
    dl = int(input("Enter Number of Line to Cancel(NO.Only) : "))
    if dl > len(menu_list) :
      print("['NOT FOUND']")
      print()
    elif dl > 0 :
      menu_list.remove(menu_list[dl-1])
      amt_list.remove(amt_list[dl-1])
      price_list.remove(price_list[dl-1])
      print("Cancel bread in order successful")
      d = d - 1
    elif dl == 0 :
      d = d - 1
    else :
      print("['NOT FOUND']")
      print()
def receipt() :
  print("~"*50)
  print("%29s"%("Receipt"))
  print("~"*50)
  print("%5s %22s %20s"%("Menu", "Amount", "Baht"))
  b = 0
  while b < len(menu_list) :
    print(" %-11s %15d %20d"%(menu_list[b], amt_list[b], price_list[b]))
    b = b + 1
  print("~"*50)
  print(" %-20s %27.2f"%("Total",sum(price_list)))
def print_receipt() : 
  with open("receipt.txt","w") as receipt :
    receipt.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    receipt.write("%29s\n"%("Receipt"))
    receipt.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    receipt.write("%5s %22s %20s\n"%("Menu", "Amount", "Baht"))
    for b in range(len(menu_list)) :
      receipt.write(" %-11s %15d %20d\n"%(menu_list[b], amt_list[b], price_list[b]))
    receipt.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    receipt.write(" %-20s %27.2f\n"%("Total",sum(price_list)))
    receipt.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("~"*50)
print("%35s"%("Welcome to M-Bakery"))
print("%27s"%("Menu"))
print("~"*50)
print("%8s %18s %21s"%("Menu ID", "Menu", "Baht"))
print("%5s %24s %18s"%("1", "Cherry Pie", "150"))
print("%5s %18s %24s"%("2", "Tart", "120"))
print("%5s %22s %20s"%("3", "Baguette", "80"))
print("%5s %23s %19s"%("4", "Croissant", "60"))
print("%5s %21s %21s"%("5", "Challah", "40"))
print("%5s %24s %18s"%("6", "Cheese Bun", "40"))
print("%5s %21s %21s"%("7", "Pretzel", "35"))
print("%5s %25s %17s"%("8", "Fancy Bread", "25"))
print("%5s %20s %22s"%("9", "Bagels", "15"))
z = 1
while z > 0 :
  print("~"*50)
  print("%34s"%("Number of program"))
  print(" 1.Add order")
  print(" 2.Cancel order")
  print(" 3.Check receipt")
  print(" 4.Print receipt")
  print(" 5.Leave a program")
  print("~"*50)
  command = int(input("Select a number(1-5) : "))
  if command == 1 :
    add()
  elif command == 2 :
    if menu_list != [] :
      dele()
    else :
      print("['PLEASE RETURN TO ADD ORDER FIRST']")
  elif command == 3 :
    receipt()
  elif command == 4 :
    if menu_list != [] :
      print_receipt()
      print("~"*50)
      print("%37s"%("Print Receipt Successful"))
      print("%29s"%("Thank you"))
      print("~"*50)
      z = z - 1
    else :
      print("['PLEASE RETURN TO ADD ORDER FIRST']")
  elif command == 5 :
    print("~"*50)
    print("%29s"%("Thank you"))
    print("~"*50)
    z = z - 1
  else :
    print("['PLEASE ENTER A NUMBER 1-5 ONLY']")