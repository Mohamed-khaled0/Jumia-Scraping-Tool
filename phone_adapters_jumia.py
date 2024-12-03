import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of brands for mobile phone adapters
brands = [
    'Acefast', 'Adam Elements', 'Apple', 'Denmen', 'Devia', 'Earldom', 'Egeline', 'Generic', 'HP', 
    'JOYROOM', 'JSAUX', 'Ldino', 'Ldnio', 'Mcdodo', 'Powerline', 'Recci', 'Remax', 'Samsung', 
    'Standard', 'WiWU', 'X-Scoot', 'Yesido','OTG'
]

# Base URL for mobile phone adapters with page placeholder
base_url = 'https://www.jumia.com.eg/mobile-phone-adapters/?page={}'

# Function to extract product data
def get_product_data(product):
    # Extract product name
    name = product.find('h3', {'class': 'name'}).get_text(strip=True)

    # Extract price
    price = product.find('div', {'class': 'prc'}).get_text(strip=True)

    # Extract product link (adjusted to get correct href)
    link_tag = product.find('a', {'class': 'core'})
    link = 'https://www.jumia.com.eg' + link_tag['href'] if link_tag else None

    # Extract product image URL (adjusted to get data-src)
    img_tag = product.find('img', {'class': 'img'})
    img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None

    # Determine the category (brand) based on product name
    category = None
    for brand in brands:
        if brand.lower() in name.lower():
            category = brand
            break
    if not category:
        category = 'Other'  # For all other brands

    return {
        'Product Name': name,
        'Price': price,
        'Product Link': link,
        'Image URL': img_url,
        'Category': category
    }

# Function to scrape products from a given page
def scrape_page(page_num):
    url = base_url.format(page_num)  # Format the base URL with the current page number
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all product entries on the page (adjusted to find 'article' tags)
        products = soup.find_all('article', {'class': 'prd _fb col c-prd'})  # Correct class name for products
        
        if not products:
            return None  # If no products are found, return None

        page_data = []
        for product in products:
            product_data = get_product_data(product)
            page_data.append(product_data)
        return page_data
    else:
        print(f"Failed to retrieve page {page_num}.")
        return None

# Function to scrape all pages until the last page
def scrape_all_pages():
    all_product_data = []
    page_num = 1  # Start from page 1

    while True:
        print(f"Scraping page {page_num}...")
        page_data = scrape_page(page_num)
        
        if not page_data:
            print(f"No products found on page {page_num}. Stopping scraping.")
            break
        
        all_product_data.extend(page_data)  # Add the products from the current page
        
        page_num += 1  # Go to the next page
        time.sleep(2)  # Add a delay to avoid overloading the server
    
    return all_product_data

# Function to save data to an Excel file
def save_to_excel(data):
    df = pd.DataFrame(data)
    # Specify a path to save the Excel file
    file_path = 'C:/Users/dell/Desktop/adapters_jumia_products.xlsx'  # Adjust the path as necessary
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Data saved to {file_path}")

# Main function to start the scraping process
def main():
    all_product_data = scrape_all_pages()  # Scrape all pages
    if all_product_data:
        save_to_excel(all_product_data)  # Save data to an Excel file

if __name__ == '__main__':
    main()
