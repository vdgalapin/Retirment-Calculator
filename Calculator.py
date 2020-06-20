import matplotlib.pyplot as plt
import numpy as np

# How much is in your current principal
current_principal = float(input("Current Principal: "))
# How much is the annual addition
annual_addition = float(input("Annual Addition: "))
# How many years to grow
years_growth = int(input("Years Growth: "))
# How much is the interest per year
annual_interest = float(input("Annual Interest: "))

# List for money growth
money_growth = []
# Years for the x-axis
years = []
# Calculation
MoneyEarnYearly = current_principal
for x in range(1, years_growth + 1):
    MoneyEarnYearly = MoneyEarnYearly + annual_addition + (
            (MoneyEarnYearly + annual_addition) * (annual_interest / 100))
    money_growth.append(MoneyEarnYearly)
    years.append(x)


# Open the file of how much you need to retire in each state
File = open('US.txt', 'r')

print("You can retire in: ")
# Iterate through the file
for y in File:
    # Split the list to configure
    y = y.split("\t")
    # Check the last of the list to check if it's lowered than
    if int(y[1]) <= MoneyEarnYearly:
        print(y[0], ' $', y[1], end=" ")
File.close()

# This will make a list of 0 to the years of growth
index = np.arange(years_growth)

# This will plot the graph
plt.bar(years, money_growth, color='green', label="$" + str(round(MoneyEarnYearly, 2)))

# Added a title in the bar graph
plt.title("Money Growth in " + str(years_growth) + " years")

# The size of the axis
plt.axis([0, years_growth + 1, 0, round(MoneyEarnYearly) + (round(MoneyEarnYearly) / years_growth)])

# The y axis will be the money growth
plt.ylabel("Dollars ($)")

# The x axis will be the years
plt.xlabel("Years")
# Add a legend
plt.legend(loc='best')
# Put ticks marks in each bar
plt.xticks(0.95 + index, years)
plt.show()
