"""
File: AmazonBookPrice.py
------------------------
This program asks the user to input the Amazon URL of a book and returns the product's title and price.
Currently, it's limited to listings which are fulfilled directly by Amazon (rather than an Amazon
Marketplace vendor). Sample URL: https://www.amazon.co.jp/-/en/gp/product/1593279922/

Author: cb
Email: tokyopdm@gmail.com
Version: 1.0.0
Date of Creation: 22 Nov 2020
Last Modified: 23 Nov 2020
"""

import bs4, requests

def main():
    print('Enter an Amazon book URL:') # Prompt the user to enter a URL
    url = input() # User inputs an Amazon URL
    price, name = getAmazonPrice(url) # Pass the URL to the getAmazonPrice function and return product price and name
    print('The price of "' + name + '" is ' + price + '.') # Print the answer for the user


def getAmazonPrice(productUrl): 
    # This function takes the URL input by the user, requests the page HTML, parses it, and returns
    # the element which matches the defined CSS styling. As of version 1.0.0, Amazon product listings
    # which do not match the specified formatting will throw an error.

    headers = { # set User-Agent and Accept-Language to get around Amazon's CAPTCHA
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 
    'Accept-Language': 'en-US;q=0.7,ja;q=0.3'
    }
    
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status() # This checks that the page was successfully requested
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # This stores the page's source code in a text file
    price = soup.select('#buyNewSection > div.a-section > div.a-row > span.inlineBlock-display > span') # This searches for the element with the corresponding CSS styling for price
    name = soup.select('#productTitle') # This searches for the element with the corresponding CSS styling for product name
    return price[0].text.strip(), name[0].text.strip() # Return two values: price, title



if __name__ == "__main__":
    main()
