import requests
from bs4 import BeautifulSoup
import pandas
import urllib.parse


# site for the tutorial =

# the website I scarpe
# Bringing the site to a variable
a = 'https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops?fts=laptops'

# using the get request to get the site
req = requests.get(a)

# parsing the site to soup variable
soup = BeautifulSoup(req.content, 'html.parser')

# getting all the div that have the element we need and storing it to results variable
results = soup.find_all('div', {'class': 'OfferBox'})

# getting name of the product
name_of_the_product = results[0].find('a', {'class': 'offerboxtitle'}).get_text()
# print(name_of_the_product)


# getting the price of the product
Price_of_the_product = results[0].find('span', {'class': 'offerprice'}).get_text()
# print('The price of the product is', Price_of_the_product)


# getting name of the rating
Rate_of_the_product = results[0].find('star-rating').get('rating-value')
# print('The rating of the product is', Rate_of_the_product)

# getting name of the review count
Rate_count_of_the_product = results[0].find('star-rating').get('ratings-count')
# print('The rating count of the product is', Rate_count_of_the_product)

# getting the relative url
relative_url = results[0].find('a', {'class': 'offerboxtitle'}).get('href')
# print(relative_url)

# url combine
root_url = 'https://www.laptopsdirect.co.uk'

# combining the url
url_combine = root_url + relative_url


# getting all the products
# creating a list that will hold the scarped raw data
product_name = []
all_price = []
review_rating = []
review_count = []
relative_url = []
product_details = []
url_combined = []

for result in results:
    try:
        product_name.append(result.find('a', {'class': 'offerboxtitle'}).get_text())
    except:
        product_name.append('n/a')# if there is no value attach n/a
    try:
        all_price.append(result.find('a', {'span': 'offerprice'}).get_text())
    except:
        all_price.append('n/a')# if there is no value attach n/a
    try:
        review_rating.append(result.find('star-rating').get('rating-value'))
    except:
        review_rating.append('n/a')# if there is no value attach n/a
    try:
        review_count.append(result.find('star-rating').get('ratings-count'))
    except:
        review_count.append('n/a')# if there is no value attach n/a
    try:
        relative_url.append(result.find('a', {'class': 'offerboxtitle'}).get('href'))
    except:
        relative_url.append('n/a')# if there is no value attach n/a

    try:
        product_details.append(result.find('div', {'class': 'productInfo'}).get_text().strip().replace('\n',','))
    except:
        product_details.append('n/a')

# print(relative_url)
for link in relative_url:
    url_combined.append(urllib.parse.urljoin(root_url,link))

# creating a data frame for the scarp data
product_over_view = pandas.DataFrame({'Name':product_name,'Price':all_price,'Ratings':review_rating,'Review count':review_count,'Link':url_combined,'Details':
                                      product_details})


# sending the scarped details to excel
product_over_view.to_excel('data_scarp2.xlsx',index=False)
