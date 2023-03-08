# Imports
import argparse
import csv
import sys
import os
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

#this function sets the date to a new one that is givin and saves the date in "Date.txt".
def set_advance_time(increase):
   increase = datetime.strptime(increase, '%Y-%m-%d')
   increase = increase.strftime('%Y-%m-%d')
   with open("Date.txt", "w") as f:
      f.write(increase)
      print(f"date updated with date: {increase}")
   return increase

#this function reads the date stored inside the Date.txt file.
def read_today():
   date = open("Date.txt", "r").read()
   print ("""
   ============================
   ༼ つ  ͡° ͜ʖ ͡° ༽つ {}
   ============================""".format(date))
   return date

#this function (if all the arguments are correct in main) adds a product to bought.csv.
def purchase_product(product_name, price, buy_date, expiry_date):
   if not os.path.exists("bought.csv"):
      open("bought.csv", "w").close()

   with open('bought.csv', "r", encoding="utf-8", errors="ignore") as file:
      lines = file.readlines()
      last_id = 0
      if lines:
         final_line = lines[-1]
         last_id = str(int(final_line.split(",")[0]) + 1)

   with open('bought.csv', mode='a', newline='') as file:   
      writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writerow([last_id, product_name, price, buy_date, expiry_date])
   sys.stdout.write("""
   =====================================
   Purchase has succesfully been placed!
   =====================================\n""")

#checks if we ever bought product, and adds it to the sold list if it is there.
def sell_product(name, price, atm):
   #if the sold file does not exist, create it.
   if not os.path.exists("sold.csv"):
      open("sold.csv", "w").close()

#checks if the product is in the bought list.
   with open('bought.csv', 'r') as read_file:
      reader = csv.reader(read_file, delimiter=',')
      products = []
      for row in reader:
         if row[1] == name:
            products.append(row)

#checks if the product is in the sold list.
   with open('sold.csv', 'r') as file:
      file_reader = csv.reader(file, delimiter=',')
      product = []
      for rows in file_reader:
         if rows[1] == name:
            product.append(rows)

#checks if the product is in the bought list, and if it is in the sold list, if its not, it adds it to the sold list.
   if products:
      if product:
         print("product already sold")
      else:
         with open('sold.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([products[0][0], products[0][1], atm, price])
         print("product succesfully sold")

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

   with open('sold.csv', mode='r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      for row in csvreader:
         if row[2] == str(gifted_date):
            revenue += float(row[3])

   with open('bought.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row_2 in csv_reader:
         if row_2[0] == row[0]:
            cost += float(row_2[2])

   profit = revenue - cost
   print ("\nthe profit was", profit)
   return profit

#exports data to csv.
def export_data_to_CSV(date_of_export):
   with open("bought.csv", "r") as original_file:
      with open("filtered_bought.csv", "w", newline='') as filtered_file:
         reader = csv.reader(original_file)
         writer = csv.writer(filtered_file)
         for row in reader:
            if str(row[3]) == str(date_of_export):
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
      ax.bar(today.strftime('%Y-%m-%d'), revenue)
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
      ax.bar(today.strftime('%Y-%m-%d'), buying_costs)
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
   group.add_argument('--sat', help='Set the date to a desired date', action='store_true')
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

   while args.sat:
      increase = input("Please enter the desired date in this format, %Y-%m-%d: ")
      set_advance_time(increase)
      break

   if args.rd:
      read_today()

   while args.pp:
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
      purchase_product(product_name, price, buy_date, expiry_date)
      break

   while args.sp:
      name = input("Please enter the product name: ")
      date_of_today = str(date.today())
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
      sell_product(name, price, date_of_today)
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
      date_of_export = input("Please enter the date you would like to export the bought info from, %Y-%m-%d: ")
      try:
         date_of_export = datetime.strptime(date_of_export, '%Y-%m-%d')
         date_of_export = datetime.date(date_of_export)
         print("Valid date")
         export_data_to_CSV(date_of_export)
         break
      except ValueError:
         print("Invalid date format. Please enter date in the format of YYYY-MM-DD.")
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
