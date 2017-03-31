
def total_melons_sold(text_file):

    the_file = open(text_file)

    melon_tallies = {"Musk":0, 
                    "Hybrid":0, 
                    "Watermelon":0, 
                    "Winter": 0}

    for line in the_file:
        line = line.rstrip()
        line = line.split("|")
        melon_type = line [1]
        melon_count = line [2]
        melon_tallies[melon_type] = melon_tallies[melon_type] + int(melon_count)


    return melon_tallies

tallies = total_melons_sold("orders-by-type.txt")
# print tallies

def total_melon_revenue(melon_tallies):
    total_revenue = 0

    melon_prices = { "Musk": 1.15, 
                    "Hybrid": 1.30, 
                    "Watermelon": 1.75, 
                    "Winter": 4.00 }
   

    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue =  total_revenue + revenue

        print "We sold {} {} melons at ${:.2f} each for a total of ${:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)


total_melon_revenue(tallies)

def separate_sales(text_file):
    the_file= open(text_file)
    online_revenue = 0
    salespeople_revenue = 0

    for line in the_file:
        line = line.split("|")
        # print line
        if line[2] == "ONLINE":
            online_revenue = online_revenue+ float(line[3])
        else:
            salespeople_revenue = salespeople_revenue + float(line[3])

    print "SALES DATA"
    print "Salespeople generated ${:.2f} in revenue.".format(salespeople_revenue)
    print "Internet sales generated ${:.2f} in revenue.".format(online_revenue)

    if salespeople_revenue > online_revenue:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"



separate_sales("orders-with-sales.txt")



























