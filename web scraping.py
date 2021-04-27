import requests
import datetime
from requests_html import HTML
import pandas as pd


now = datetime.datetime.now()
year = now.year


def url_to_txt(url, filename='world.html',save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f'world-{year}.html', 'w') as f:
                f.write(html_text)
        return html_text
    return ''


url = 'https://www.boxofficemojo.com/year/world/'

html_text = url_to_txt(url)
r_html = HTML(html=html_text)
table_class = '.imdb-scroll-table'
# table_class = '#table' put '#' bcz its an id put '.' bcz its an class
r_table = r_html.find(table_class)
# print(r_table)

table_data = []
hader_names = []
if len(r_table) == 1:
    parse_table = r_table[0]
    rows = parse_table.find('tr')
    header_row = rows[0]
    header_col = header_row.find('th')
    hader_names = [x.text for x in header_col]

    for row in rows[1:]:
        print(row.text)
        cols = row.find('td')
        row_data = []
        for i, col in enumerate(cols):
            # print(i, col.text,'\n\n')
            row_data.append(col.text)
        table_data.append(row_data)

print(hader_names)
print(table_data)


df = pd.DataFrame(table_data, columns=hader_names)
df.to_csv('movies.csv', index=False)















































# import requests
# import datetime
#
# now = datetime.datetime.now()
# year = now.year
#
# # This code is only create a file and store data
# def url_to_file(url, filename='world.html'):
#     r = requests.get(url)
#     if r.status_code == 200:
#         html_text = r.text
#         with open(f'world-{year}.html', 'w') as f:
#             f.write(html_text)
#         return html_text
#     return ''
#
#
# url = 'https://www.boxofficemojo.com/year/world/'
#
# url_to_file(url)




