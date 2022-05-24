#Program to scrape titles and prices of all books rated 4 star or above
#Import necessary libraries
import bs4, requests

#Setting up the variables
#Prices and Titles will be stored as a list of lists
book_titles_and_prices = []
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

#Going through the 50 pages
for num in range(1,51):
    url_to_scrape = base_url.format(num)
    res = requests.get(url_to_scrape)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    #All books are under the class product_pod
    books = soup.select(".product_pod")
    
    #Going through all the books
    for book in books:
        #Checking if it is 4 star or 5 star
        if len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five")) != 0:
            title = book.select('a')[1]['title']
            price = book.select('p')[1].getText()
            title_and_price = [title, price]
            book_titles_and_prices.append(title_and_price)

print("Book Title \t Price")
for item in book_titles_and_prices:
    print(f"{item[0]} \t {item[1]}")