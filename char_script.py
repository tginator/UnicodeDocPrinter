import requests
from bs4 import BeautifulSoup

def fetch_and_print_grid(doc_url):

    # Retrieve doc
    response = requests.get(doc_url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parsing with BeautifulSoup library
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding <tr> tags to identify table
    rows = soup.find_all('tr')

    # Parse data into x, char, y grid
    grid_points = []

    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) == 3:
            x = int(cells[0].text.strip())
            char = cells[1].text.strip()
            y = int(cells[2].text.strip())
            grid_points.append((x, char, y))

    # Build grid
    grid_dict = {}
    max_x = max_y = 0
    for x, char, y, in grid_points:
        grid_dict[(y, x)] = char # row = y, col = x
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Print grid per row
    for y in range(max_y + 1):
        row_chars = []
        for x in range(max_x + 1):
            row_chars.append(grid_dict.get((y, x), ' '))
        print(' '.join(row_chars))
        
# Using URL given: 
url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

fetch_and_print_grid(url)
