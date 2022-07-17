import requests
from bs4 import BeautifulSoup

# use the requests get function to get the webpage we want to scrape
port_webpage = requests.get('https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers')

# store the http response status code in a variable
status = port_webpage.status_code
# store the text of the website in a variable
txt = port_webpage.text
# store the content of the website in a variable
content = port_webpage.content

# pass webpage through beautiful soup
soup = BeautifulSoup(content, 'html.parser')

# examples of extracting elements with beautiful soup
title = soup.title.text
head = soup.head
body = soup.body

# using select to select elements from the page
# will select the text from the first h1
first_h1 = soup.select('h1')[0].text

# Start of program to scrape common port details from wikipedia
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

# searching for the appropriate table one the wikipedia page
my_table = soup.find('table', {'class':'sortable'})

# searching for all the entries within the table and parsing them into a table variable
entries = my_table.findAll('tr')

port_descriptions = []

# iterate through the port entry extracting the port numbers and description and writing them to a file
for i in range (1, len(entries)):
    port_dictionary = {}
    port_dictionary['Port'] = entries[i]('td')[0].text
    if len(entries[i]) > 10:
        port_dictionary['Description'] = entries[i]('td')[5].text.rstrip('\n')
    port_descriptions.append(port_dictionary)
    with open('port_descriptions.txt', 'a') as file:
        file.write(str(port_dictionary) + '\n')

