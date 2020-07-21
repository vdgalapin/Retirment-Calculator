# This allows to plot the table
import matplotlib.pyplot as plt
# This allow us to create a list automatically
import numpy as np
# Allow us to post an image and draw on it
from PIL import Image, ImageDraw, ImageFont
# Create a pretty table
from prettytable import PrettyTable

# How much is in your current principal
current_principal = float(input("Current Principal: "))
# How much is the annual addition
annual_addition = float(input("Annual Addition: "))
# How many years to grow
years_growth = int(input("Years Growth (Cannot be zero and below): "))
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
########################################################################################################################
# open method used to open different extension image file
im = Image.open(r"C:\Users\Vyron\Documents\GitHub\Retirment-Calculator\USA-MAP.png").convert('RGBA')
# Allow us to draw in the picture
draw = ImageDraw.Draw(im)
# Outline for dots in the picture
#######################################################################################################################
# # Washington
# draw.chord([(140,30), (160, 50)], 0,360, fill=50)
# # Oregon
# draw.chord([(120, 120), (140, 140)], 0,360, fill=50)
# # california
# draw.chord([(70,280), (90, 300)], 0,360, fill=50)
# # Alaska
# draw.chord([(120,550), (140, 570)], 0,360, fill=50)
# # Nevada
# draw.chord([(140,240), (160, 260)], 0,360, fill=50)
# # Idaho
# draw.chord([(210, 120), (230, 140)], 0,360, fill=50)
# # Arizona
# draw.chord([(210, 400), (230, 420)], 0,360, fill=50)
# # Utah
# draw.chord([(230,260), (250, 280)], 0,360, fill=0)
# # Montana
# draw.chord([(280,90), (300, 110)], 0,360, fill=50)
# # Wyoming
# draw.chord([(320,190), (340, 210)], 0,360, fill=50)
# # Colorado
# draw.chord([(340,280), (360, 300)], 0,360, fill=0)
# # New Mexico
# draw.chord([(340,400), (360, 420)], 0,360, fill=0)
# # North Dakota
# draw.chord([(480,80), (500, 100)], 0,360, fill=50)
# # South Dakota
# draw.chord([(480,150), (500, 170)], 0,360, fill=50)
# # Nebraska
# draw.chord([(480,240), (500, 260)], 0,360, fill=50)
# # Kansas
# draw.chord([(480,320), (500, 340)], 0,360, fill=50)
# # Texas
# draw.chord([(460,500), (480, 520)], 0,360, fill=50)
# # Minnesota
# draw.chord([(600,100), (620, 120)], 0,360, fill=50)
# # Iowa
# draw.chord([(600,220), (620, 240)], 0,360, fill=50)
# # Missouri
# draw.chord([(640,320), (660, 340)], 0,360, fill=50)
# # Arkansas
# draw.chord([(640,410), (660, 430)], 0,360, fill=50)
# # Oklahoma
# draw.chord([(520,400), (540, 420)], 0,360, fill=50)
# # Louisiana
# draw.chord([(660,520), (680, 540)], 0,360, fill=50)
# # Wisconsin
# draw.chord([(680,150), (700, 170)], 0,360, fill=50)
# # Illionois
# draw.chord([(720,260), (740, 280)], 0,360, fill=50)
# # Michigan
# draw.chord([(790,180), (810, 200)], 0,360, fill=50)
# # Indiana
# draw.chord([(770,260), (790, 280)], 0,360, fill=50)
# # Ohio
# draw.chord([(830,260), (850, 280)], 0,360, fill=50)
# # Kentucky
# draw.chord([(830,340), (850, 360)], 0,360, fill=50)
# # Tennessee
# draw.chord([(830,390), (850, 410)], 0,360, fill=50)
# # Mississippi
# draw.chord([(720,460), (740, 480)], 0,360, fill=50)
# # Alabama
# draw.chord([(790,450), (810, 470)], 0,360, fill=50)
# # Georgia
# draw.chord([(840,460), (860, 480)], 0,360, fill=50)
# # South Carolina
# draw.chord([(920,460), (940, 480)], 0,360, fill=50)
# # North Carolina
# draw.chord([(980,370), (1000, 390)], 0,360, fill=50)
# # Florida
# draw.chord([(920,580), (940, 600)], 0,360, fill=50)
# # West Virginia
# draw.chord([(900,320), (920, 340)], 0,360, fill=50)
# # Virginia
# draw.chord([(960,320), (980, 340)], 0,360, fill=50)
# # Pennsylvania
# draw.chord([(980,220), (1000, 240)], 0,360, fill=50)
# # New York
# draw.chord([(1000,160), (1020, 180)], 0,360, fill=50)
# # Maryland
# draw.chord([(980,280), (990, 290)], 0,360, fill=50)
# # Delaware
# draw.chord([(1010,280), (1020, 290)], 0,360, fill=50)
# # New Jersey
# draw.chord([(1020,250), (1030, 260)], 0,360, fill=50)
# # Connecticut
# draw.chord([(1050,200), (1060, 210)], 0,360, fill=50)
# # Rhode Island
# draw.chord([(1070,190), (1080, 200)], 0,360, fill=50)
# # Massachussets
# draw.chord([(1050,180), (1060, 190)], 0,360, fill=50)
# # New Hampshire
# draw.chord([(1050,140), (1060, 150)], 0,360, fill=50)
# # Vermont
# draw.chord([(1030,140), (1040, 150)], 0,360, fill=50)
# # Maine
# draw.chord([(1080,80), (1100, 100)], 0,360, fill=50)
# # Hawaii
# draw.chord([(400,680), (410, 690)], 0,360,  fill ="yellow")
########################################################################################################################


# This will put a grid  lines to the picture
########################################################################################################################
# for y in range(0, 720,20):
#     draw.line((0, y, im.size[0], y), fill=128)
# for x in range(0, 1200,20):
#     draw.line((x, 0, x, im.size[0]), fill=128)
########################################################################################################################



########################################################################################################################
# Open the file of how much you need to retire in each state
File = open('US.txt', 'r')

# Initiate the table
retirement_table = PrettyTable()
states_cant_retire = PrettyTable()
# add row names in the table where you can retire
retirement_table.field_names=["State", "Retirement Cost ($)"]
# add row names in the table wher you cannot reture
states_cant_retire.field_names=["States", "Retirement Cost ($)", "How much you need more ... "]
print("You can retire in: ")
# Iterate through the file
for y in File:
    # Split the list to configure
    y = y.split("\t")
    # Check the last of the list to check if it's lowered than
    if (int(y[1]) > MoneyEarnYearly and int(y[1]) > 0):
        # Draws red circle to places you cannot retire in
        draw.chord([(int(y[2]), int(y[3])), (int(y[4]), int(y[5]))], 0, 360, fill="red")
        # add row to the tables of states you cant retire
        states_cant_retire.add_row([y[0], '${0:.2f}'.format(float(y[1])), '${0:.2f}'.format(float(y[1]) - MoneyEarnYearly)])
    if int(y[1]) <= MoneyEarnYearly:
        # Draws green circles to places you can retire in
        draw.chord([(int(y[2]),  int(y[3])), (int(y[4]), int(y[5]))], 0, 360, fill="green")
        # add row to t he retirement table
        retirement_table.add_row([y[0],'${0:.2f}'.format(float(y[1]))])

# prints the table of states you cant retire
print(states_cant_retire)
# prints the the table of states you can retire
print(retirement_table)

# Closes the file
File.close()

########################################################################################################################
# Prints a text in the picture
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20)

red_text = 'The Red Circle is the states you cant retire.'
green_text = 'The Green Circle is the state you can retire.'
# drawing text size
draw.text((475, 0), red_text, font=font, align="left", fill='black')
draw.text((475, 25), green_text, font=font, align="left", fill = 'black')
########################################################################################################################
# Necessary
del draw
# show the pictures
im.show()

# This will make a list of 0 to the years of growth
index = np.arange(years_growth)

# This will plot the graph
plt.bar(years, money_growth, color='green', label="${0:.2f}".format(float(MoneyEarnYearly)))

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


