import matplotlib.pyplot as plt
import pandas as pd

# Preparing data for visualizations

state_data=pd.read_csv("state_data.csv")

# BJP's dominance
bjp_dominance = state_data[state_data['Leading Party'] == 'Bharatiya Janata Party']['State/UT'].value_counts()

# INC's performance
inc_performance = state_data[state_data['Leading Party'] == 'Indian National Congress']['State/UT'].value_counts()

# Coalition politics
coalition_politics = state_data['Leading Party'].value_counts()

# Regional parties' impact
regional_parties = state_data[state_data['Leading Party'].isin(['Samajwadi Party', 'All India Trinamool Congress'])]['State/UT'].value_counts()

# Plotting BJP's dominance
plt.figure(figsize=(10, 6))
bjp_dominance.plot(kind='bar', color='orange')
plt.title("BJP's Dominance by State")
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()

# Plotting INC's performance
plt.figure(figsize=(10, 6))
inc_performance.plot(kind='bar', color='blue')
plt.title("INC's Performance by State")
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()


# Plotting Coalition politics with "Other" category
threshold = 10
coalition_politics_grouped = coalition_politics[coalition_politics >= threshold]
others = coalition_politics[coalition_politics < threshold].sum()
coalition_politics_grouped['Other'] = others

plt.figure(figsize=(10, 6))
coalition_politics_grouped.plot(kind='pie', autopct='%1.1f%%')
plt.title('Coalition Politics in India')
plt.ylabel('')
plt.show()



# Plotting Regional parties' impact
plt.figure(figsize=(10, 6))
regional_parties.plot(kind='bar', color=['green', 'purple'])
plt.title("Regional Parties' Impact")
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()



# Define left parties for analysis
left_parties = ['Communist Party of India', 'Communist Party of India (Marxist)', 'Revolutionary Socialist Party']

# Left Parties' Decline
left_parties_decline = state_data[state_data['Leading Party'].isin(left_parties)]['State/UT'].value_counts()

# New Parties' Emergence
new_parties = ['Janasena Party', 'Voice of the People Party']
new_parties_emergence = state_data[state_data['Leading Party'].isin(new_parties)]['State/UT'].value_counts()

# Impact of Independent Candidates
independents_impact = state_data[state_data['Leading Party'] == 'Independent']['State/UT'].value_counts()

# Diverse Representation in Maharashtra
maharashtra_diversity = state_data[state_data['State/UT'] == 'Maharashtra']['Leading Party'].value_counts()

# Plotting Left Parties' Decline
plt.figure(figsize=(10, 6))
left_parties_decline.plot(kind='bar', color='red')
plt.title("Left Parties' Decline by State")
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()

# Plotting Emergence of New Parties
plt.figure(figsize=(10, 6))
new_parties_emergence.plot(kind='bar', color='cyan')
plt.title("Emergence of New Parties")
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()

# Plotting Impact of Independent Candidates
plt.figure(figsize=(10, 6))
independents_impact.plot(kind='bar', color='grey')
plt.title('Impact of Independent Candidates by State')
plt.xlabel('State/UT')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=90)
plt.show()

# Plotting Diverse Representation in Maharashtra
plt.figure(figsize=(10, 6))
maharashtra_diversity.plot(kind='pie', autopct='%1.1f%%')
plt.title('Diverse Representation in Maharashtra')
plt.ylabel('')
plt.show()

# Close contests (top 10 smallest margins)
close_contests = state_data.nsmallest(10, 'Margin')
# Plotting close contests
plt.figure(figsize=(12, 6))
plt.barh(close_contests['Constituency'], close_contests['Margin'], color='skyblue')
plt.xlabel('Margin of Victory')
plt.ylabel('Constituency')
plt.title('Top 10 Close Contests')
plt.gca().invert_yaxis()  # To display the smallest margin at the top
plt.show()


# Adding data for Tamil Nadu's Unique Scenario
tamil_nadu_data = pd.Series({
    'Dravida Munnetra Kazhagam': 22,
    'Indian National Congress': 9
})

# Plotting Tamil Nadu's Unique Scenario
plt.figure(figsize=(10, 6))
tamil_nadu_data.plot(kind='bar', color=['red', 'blue'])
plt.title("Tamil Nadu's Unique Scenario")
plt.xlabel('Party')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=0)
plt.show()