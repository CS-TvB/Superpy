# Zippie market manual

In this manual we will go trough the main menu of the system and the functions within it and how to correctly use it.

Running the program and the functions within:  

to enter the main menu you can type -h or –help. Some operating systems requires you to also type python or python3 in front of the function, see the examples below. Also make sure you are in the folder of the program while executing it (this is also the location where exports will be saved)
-	python .\main.py -h
-	python .\main.py -help
-	python3 .\main.py -h
-	python3 .\main.py -help

Main menu:  

Welcome to the zippiemarket zippie system!  

options:

|Argument|Second option for argument|Description|
|--------|--------------------------|-----------|
|-h|--help|show this help message and exit|
|--st|X|Set todays date in Date.txt|
|--sat|X|Set the date to any desired date|
|--rd|X|Reads the set date from Date.txt|
|--pp|X|purchase a product|
|--sp|X|sell a product|
|--rr|X|report revenue|
|--rp|X|report profit|
|--ebp|X|exports bought products|
|--sf1|X|displays the revenue of a giving day|
|--sf2|X|displays the profit of a giving day|

# explanation functions

    --st, Set todays date :  
 	-	this function sets the date to today.   


    --sat, Set the date to a desired date :  
	-	this function lets you set any desired date.  


    --rd, Reads the set date :  
    -	this function lets you check what date is written in the program, handy to check If you need to set todays date, rather then still having it on older date from –sat.  


    --pp, purchase a product :  
    -	this function lets you purchase products provided with a couple valid inputs. The function in the program will tell you the requirements for the inputs displayed below.  
	 	1.	product name.
		2.	bought price.
		3.	buy date.
		4.	expiry date.  


    --sp, sell a product :  
    -	this function lets you sell products provided with a couple valid inputs. The function in the program will tell you the requirements for the inputs displayed below.  
	    1.	product name.
	    2.	sold price.


    --rr, report revenue :  
	-	this function reports the made revenue from a giving date.  


    --rp, report profit :  
	-	this function reports the made profit from a giving date.  


    --ebp, exports bought products :  
    -	this function creates a exported CSV file with al the information of bought product from a provided date.


    --sf1, displays the revenue of a giving day :  
    -	this function displays how much revenue the company made in one day, provided the desired date.


    --sf2, displays the profit of a giving day :  
    -	this function displays how much profit the company made in one day, provided the desired date.

# report

For the last two special functions I wrote a somewhat similar functions, because I wanted to work with Matplot library. But lets dive deeper in the function. 

1)  First we create a empty list called renvenue. then we open the csv file where the sold item info is stored.

2)  Then we wil loop trough the file in search of lists from items we have sold on the input date.

3)  Afther we found a list with a matching sold date we check the quantitys sold and times that the sold price per piece, if the quantity 1 we just add the sold price only once.

4)	When we have the revenue, we create a figure and axis object that we can use to add elements to the graph.

5)	In the bar graph, with [0] being our x-coordinate and revenue being our height. We set the label for the x-axis to “Day” because we only need to measure revenue of 1 single day.  

6)	We set the label for the y-axis to “revenue (in euro’s)” because want to see how high the revenue goes on the giving date. 

7)	And then we give the graph a title, I made it a f-string so if they decide to save it for a presentation later they have a indication of what day it was about.

8)	At the end we show the graph or print a string to say that the revenue was 0.

```python
def special_function_1(today):
   revenue = []
   with open('sold.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[2] == str(today):
            if int(row[-1]) > 1:
               revenue.append(float(row[3]) * float(row[-1]))
            else:
               revenue.append(float(row[3]))

   revenue = sum(map(int, revenue))
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

``` 

The csv library solves alot in my program, it basically functions as follow:

1)	We open the file sold.csv, in read mode. And we call that complete action csv_file.

2)	Then we give a name, csv_reader to an action that returns a reader object wich wil iterate over the lines in the csv_file. You could say that the delimiter (‘,’) here acts like a border and will put its returned list of strings into a few elements.

3)	After this we can use the elements to loop though.

```python
def report_revenue(the_day):
   revenue = 0
   with open('sold.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         if row[2] == the_day:
            if int(row[-1]) > 1:
               revenue += float(row[3]) * float(row[-1])
            else:
               revenue += float(row[3])
   sys.stdout.write("\nin therms of revenue we made: " + str(revenue))
   return revenue
```

The export_data_to_csv function:  
In this function we take a date as input and try to make it a valid date, afther we confirmed it is valid we send the input as argument to the function that exports the matching lists with the input date.

```python
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
```



