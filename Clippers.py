#Carly's clippers
#Hope I can make it

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
  #to test: print total_price (was successful)
  #print(total_price)

average_price = total_price / len(prices)
#to test print average_price (255/8 should give 31.875)
#print(average_price)
print("Average Haircut Price: " + str(average_price))

new_price = [price -5 for price in prices]
#to test: print new_prices (first one should be 25 and not 30)
print(new_price)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
#test
print("Total Revenue: " + str(total_revenue))
total_daily_revenue = total_revenue / 7
print(total_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_price[i] < 30]
print(cuts_under_30)