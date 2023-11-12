completed code

import pandas as py
import numpy as np
import matplotlib.pyplot as plt

data=py.read_csv("data.csv")

# Q1. Share of International Reputation for the Football Players
plt.figure(figsize=(8, 8))
data['International Reputation'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Share of International Reputation for Football Players')
plt.show()

# Q2. Distribution of Weak Foot among Players
plt.figure(figsize=(10, 6))
data['Weak Foot'].value_counts().sort_index().plot.bar()
plt.title('Distribution of Weak Foot among Players')
plt.xlabel('Weak Foot Rating')
plt.ylabel('Number of Players')
plt.show()

# Q3. Comparison of Preferred Foot over Different Players / Most Preferred Foot of the Players
plt.figure(figsize=(8, 8))
data['Preferred Foot'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Preferred Foot of Football Players')
plt.show()

# Q4. Score Distribution of Different Abilities
abilities = ['Dribbling', 'ShortPassing', 'LongPassing',]
plt.figure(figsize=(12, 6))
data[abilities].boxplot()
plt.title('Score Distribution of Different Abilities')
plt.ylabel('Ability Score')
plt.show()

# Q5. Different Positions Acquired by the Players
plt.figure(figsize=(12, 6))
data['Position'].value_counts().plot.bar()
plt.title('Different Positions Acquired by Players')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.show()

# Q6. Distribution of Players' Weight
plt.figure(figsize=(10, 6))
data["Weight"].value_counts().sort_index().plot.bar()
plt.title('Distribution of Players\ Weight')
plt.xlabel('Weight')
plt.ylabel('Number of Players')
plt.show()

# Q7. Count of Players on the Basis of Their Skill Moves
plt.figure(figsize=(10, 6))
data['Skill Moves'].value_counts().sort_index().plot.bar()
plt.title('Count of Players based on Skill Moves')
plt.xlabel('Skill Moves Rating')
plt.ylabel('Number of Players')
plt.show()

# Q8. Potential Scores and Overall Scores of the Players in One Plot
plt.figure(figsize=(10, 8))
plt.scatter(data['Potential'], data['Overall'])
plt.title('Potential Scores vs Overall Scores of Players')
plt.xlabel('Potential Score')
plt.ylabel('Overall Score')
plt.show()

# Q9. Distribution of Overall Score in Different Popular Clubs
some_clubs = ['FC Barcelona', 'Real Madrid', 'Manchester United', 'Juventus']
plt.figure(figsize=(12, 8))
data[data['Club'].isin(some_clubs)].boxplot(column='Overall', by='Club', rot=45)
plt.title('Distribution of Overall Score in Popular Clubs')
plt.xlabel('Club')
plt.ylabel('Overall Score')
plt.show()

# Q10. Countries with Most Players
plt.figure(figsize=(12, 6))
data['Nationality'].value_counts().head(10).plot.bar()
plt.title('Top 10 Countries with Most Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.show()

# Define a function to convert 'Weight' to numeric values
def convert_to_numeric(weight):
    try:
        # Extract numeric part and convert to float
        return float(''.join(filter(str.isdigit, str(weight))))
    except ValueError:
        return None

# Apply the conversion function to the 'Weight' column
data['Weight'] = data['Weight'].apply(convert_to_numeric)

# Q11. Distribution of Weight of Players from Different Countries
selected_countries = ['Argentina', 'Brazil', 'Germany', 'Spain', 'France']
plt.figure(figsize=(12, 8))
data[data['Nationality'].isin(selected_countries)].boxplot(column='Weight', by='Nationality', rot=45)
plt.title('Distribution of Weight of Players from Different Countries')
plt.xlabel('Country')
plt.ylabel('Weight')
plt.show()

# Q12. Distribution of International Reputation of Players from Different Countries
plt.figure(figsize=(12, 8))
data[data['Nationality'].isin(selected_countries)].boxplot(column='International Reputation', by='Nationality', rot=45)
plt.title('Distribution of International Reputation of Players from Different Countries')
plt.xlabel('Country')
plt.ylabel('International Reputation')
plt.show()

