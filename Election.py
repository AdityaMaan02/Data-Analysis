import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

urls_ut = [f'https://results.eci.gov.in/PcResultGenJune2024/statewiseU0{i}1.htm' for i in range(1,10)]
urls_state = [f'https://results.eci.gov.in/PcResultGenJune2024/statewiseS0{i}1.htm' for i in range(1, 10)]
urls_state += [f'https://results.eci.gov.in/PcResultGenJune2024/statewiseS{i}1.htm' for i in range(10, 31)]
urls = urls_ut + urls_state

all_data = []

#Extract content for every url
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the count of pagination pages
    page_counts = len(soup.select('ul.pagination li'))
    new_url = url
    data = []

    for page_count in range(page_counts):
        time.sleep(2)  # Wait for the page to load
        soup = BeautifulSoup(requests.get(new_url).content, "html.parser")

        # Extract constituency name
        page_title_div = soup.find('div', class_='page-title')
        name = page_title_div.find('h2').text.strip() if page_title_div else "Unknown Constituency"

        # Extract table rows
        all_trs = soup.find_all('tr')
        for tr in all_trs[2:]:
            cells = tr.find_all('td')
            cell_texts = [cell.get_text(strip=True) for cell in cells if cell.get_text(strip=True)]
            if len(cell_texts) == 30:
                cell_texts.insert(0, name)
                data.append(cell_texts)

        # Increment the last digit of the URL for the next page
        last_digit = new_url[-5]
        new_last_digit = int(last_digit) + 1
        new_url = new_url[:-5] + str(new_last_digit) + '.htm'

    # Create a DataFrame for the current URL
    df = pd.DataFrame(data)
    all_data.append(df)

# Concatenate all DataFrames
final_df = pd.concat(all_data, ignore_index=True)

# Select and rename columns
df = final_df.iloc[:, [0, 1, 2, 3, 5, 16, 18, 29]]
df.columns = ['State/UT', 'Constituency', 'Const. No.', 'Leading Candidate', 'Leading Party',
              'Trailing Candidate', 'Trailing Party', 'Margin']

# Display the final DataFrame
df.head(5)

df.shape

# Convert to csv file
df.to_csv('state_data.csv')