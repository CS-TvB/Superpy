# Imports
import argparse
import csv
import sys
from datetime import timedelta, datetime, date
import matplotlib.pyplot as plt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

#this function sets todays date in the txt file called "Date.txt" and returns it.
def set_today():
   atm = str(date.today())
   with open("Date.txt", "w") as f:
      f.write(atm)
      sys.stdout.write(atm)
   return atm

#this function increases the time by a positive or negative number and saves the date in "Date.txt".
def set_advance_time(increase):
   Today = str(date.today())
   Todays_format = datetime.strptime(Today, '%Y-%m-%d')
   increased_day = Todays_format + timedelta(days = increase)
   Today = increased_day.strftime('%Y-%m-%d')
   file = open("Date.txt", "w")
   file.write(Today)
   file.close()
   sys.stdout.write("""
   =====================================================
   (ᵔᴥᵔ) Time has succsesfully advanced to {}
   =====================================================\n""".format(Today))

#this function reads the date stored inside the Date.txt file.
def read_today():
   date = open("Date.txt", "r").read()
   print ("""
   ============================
   ༼ つ  ͡° ͜ʖ ͡° ༽つ {}
   ============================""".format(date))
   return date

#this function (if all the arguments are correct in main) adds a product to bought.csv.
def purchase_product(id, product_name, price, buy_date, expiry_date):
   with open('bought.csv', mode='a', newline='') as file:
      writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writerow([id, product_name, price, buy_date, expiry_date])
   sys.stdout.write("""
   =====================================================
   (• ε •) Purchase has succesfully been placed!(• ε •)
   =====================================================\n""")

#checks if we ever bought product, and adds it to the sold list if it is there.
def sell_product(id, name, price, atm):
   with open('bought.csv', 'r') as read_file:
      reader = csv.reader(read_file, delimiter=',')
      items = [row for row in reader]
      product = next((item for item in items if item[1] == name), None)
   if not product:
      sys.stdout.write("""
   =======================================================================================================
   1.. 2.. 3.. 4.. How manny thiefs are in the store? we dont have this on the shelves anymore. ¯\_(ツ)_/¯
   =======================================================================================================\n""")
   else:
      with open('sold.csv', 'a', newline='') as file:
         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         writer.writerow([id, product[0], atm, price])
         sys.stdout.write("""
   ============================================
   The item has succesfully been sold ٩(◕‿◕)۶
   ============================================\n""")

#reports the revenue of a day.
def report_revenue(the_day):
   revenue = 0
   with open('sold.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[2] == the_day:
            revenue += float(row[3])
   sys.stdout.write("\nin therms of revenue we made: " + str(revenue))
   return revenue

#reports the proft made on a day.
def report_profit(gifted_date):
   cost = 0
   revenue = 0
   with open('bought.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[3] == str(gifted_date):
            cost += float(row[2])
   with open('sold.csv', mode='r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      for row in csvreader:
         if row[2] == str(gifted_date):
            revenue += float(row[3])
   profit = revenue - cost
   print ("\nthe profit was", profit)
   return profit

#exports data to csv.
def export_data_to_CSV(search_string):
   with open("bought.csv", "r") as original_file:
      with open("filtered_bought.csv", "w", newline='') as filtered_file:
         reader = csv.reader(original_file)
         writer = csv.writer(filtered_file)
         for row in reader:
            if row[0] == search_string:
               writer.writerow(row)
   print("the file can be found in the software folder called, filtered_bought.csv")
   return "filtered_bought.csv"

#vizualize revenue.
def special_function_1(today):
   revenue = []
   with open('sold.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[2] == str(today):
            revenue.append(float(row[3]))
   if revenue:  
      fig, ax = plt.subplots()
      ax.bar([0], revenue)
      ax.set_xlabel("Day")
      ax.set_ylabel("Revenue (in euro's)")
      ax.set_title(f"Revenue for a single day, {today}")
      plt.show()
   else:
      print ("sry no revenue build up today :(")
      return ()

#visualize buying costs.
def special_function_2(today):
   buying_costs = []
   with open('bought.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[3] == str(today):
            buying_costs.append(float(row[2]))
   if buying_costs:  
      fig, ax = plt.subplots()
      ax.bar([0], buying_costs)
      ax.set_xlabel("Day")
      ax.set_ylabel("cost (in euro's)")
      ax.set_title(f"bought costs for a single day, {today}")
      plt.show()
   else:
      print ("sry nothing has been bought on this date.")
      return ()

def main():
   parser = argparse.ArgumentParser(description='Welcome to the zippiemarket zippie system!')
   
   group = parser.add_mutually_exclusive_group()
   
   group.add_argument('--st', help='Set todays date', action='store_true')
   group.add_argument('--sat', help='Increase todays date by the giving number of days', type=int)
   group.add_argument('--rd', help='Reads the set date', action='store_true')
   group.add_argument('--pp', help='purchase a product', action='store_true')
   group.add_argument('--sp', help ='sell a product', action='store_true')
   group.add_argument('--rr', help='report revenue', action='store_true')
   group.add_argument('--rp', help='report profit', action='store_true')
   group.add_argument('--ebp', help='exports bought products', action='store_true')
   group.add_argument('--sf1', help='displays the revenue of a giving day', action='store_true')
   group.add_argument('--sf2', help='displays the profit of a giving day', action='store_true')

   args = parser.parse_args()

   if args.st:
      set_today()

   if args.sat:
      set_advance_time(args.sat)

   if args.rd:
      read_today()

   while args.pp:
      id = input("Please enter the product id (must be a 4-digit number): ")
      if id.isdigit() and len(id) == 4:
         print("Input accepted.")
      else:
         print("Invalid input")
         break
      product_name = input("Please enter the product name: ")
      if isinstance(product_name, str):
         print("Input accepted.")
      else:
         print("Invalid input")
         break         
      price = input("Please enter the product price: ")
      try:
         price = float(price)
         print("Input accepted.")
      except ValueError:
         print("Invalid input")
         break
      buy_date = input("Please enter the product bought date in this format, %Y-%m-%d: ")
      try:
         buy_date = datetime.strptime(buy_date, '%Y-%m-%d')
         buy_date = datetime.date(buy_date)
         print("Valid date")
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break
      expiry_date = input("Please enter the product expiry date in this format, %Y-%m-%d: ")
      try:
         expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
         expiry_date = datetime.date(expiry_date)
         print("Valid date")
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break
      purchase_product(id, product_name, price, buy_date, expiry_date)
      break

   while args.sp:
      id = input("Please enter the product id (must be a 4-digit number): ")
      if id.isdigit() and len(id) == 4:
         print("Input accepted.")
      else:
         print("Invalid input")
         break
      name = input("Please enter the product name: ")
      if isinstance(name, str):
         print("Input accepted.")
      else:
         print("Invalid input")
         break
      price = input("Please enter the product price: ")
      try:
         price = float(price)
         print("Input accepted.")
      except ValueError:
         print("Invalid input")
         break
      sell_product(id, name, price, set_today())
      break

   while args.rr:
      gifted_date = input("Please enter the date you would like to see the revenue from in this format, %Y-%m-%d: ")
      try:
         gifted_date = datetime.strptime(gifted_date, '%Y-%m-%d')
         gifted_date = datetime.date(gifted_date)
         print("Valid date")
         report_revenue(str(gifted_date))
         break
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break

   while args.rp:
      gifted_date = input("Please enter the date you would like to see the profit from in this format, %Y-%m-%d: ")
      try:
         gifted_date = datetime.strptime(gifted_date, '%Y-%m-%d')
         gifted_date = datetime.date(gifted_date)
         print("Valid date")
         report_profit(gifted_date)
         break
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break

   while args.ebp:
      ebp = input("Please enter the product id (must be a 4-digit number): ")
      if ebp.isdigit() and len(ebp) == 4:
         print("Input accepted.")
         export_data_to_CSV(ebp)
         break
      else:
         print("Invalid input")
         break

   while args.sf1:
      gifted_date = input("Please enter the date you would like to see the revenue from in this format, %Y-%m-%d: ")
      try:
         gifted_date = datetime.strptime(gifted_date, '%Y-%m-%d')
         gifted_date = datetime.date(gifted_date)
         print("Valid date")
         special_function_1(gifted_date)
         break
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break

   while args.sf2:
      gifted_date = input("Please enter the date you would like to see the profit from in this format, %Y-%m-%d: ")
      try:
         gifted_date = datetime.strptime(gifted_date, '%Y-%m-%d')
         gifted_date = datetime.date(gifted_date)
         print("Valid date")
         special_function_2(gifted_date)
         break
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
         break

if __name__ == '__main__':
   main()