import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of mobile brands
brands = [
    'alcatel', 'apple', 'benco', 'black shark', 'cat', 'earldom', 'generic', 'honor', 'iku', 'infinix', 'itel', 
    'lava', 'lenovo', 'm-horse', 'nokia', 'nubia', 'oppo', 'poco', 'redmi', 'samsung', 'tag-phone', 'tecno', 
    'unihertz', 'vivo', 'vivo mattress', 'x-plus', 'zte'
]
# Base URL with a placeholder for the page number
base_url = 'https://www.jumia.com.eg/android-phones/alcatel--apple--benco--black-shark--cat--earldom--generic--honor--iku--infinix--itel--lava--lenovo--m-horse--mi--nokia--nubia--oppo--poco--realme--redmi--samsung--tag-phone--tecno--unihertz--vivo--vivo-mattress--x-plus--xaomi--xiaomi--zte/?page={}#catalog-listing'

# Function to get product data from each product div
def get_product_data(product):
    name = product.find('h3', {'class': 'name'}).get_text(strip=True)
    price = product.find('div', {'class': 'prc'}).get_text(strip=True)
    old_price = product.find('div', {'class': 'old'})
    if old_price:
        old_price = old_price.get_text(strip=True)
    else:
        old_price = None
    discount = product.find('div', {'class': 'bdg _dsct _sm'})
    if discount:
        discount_percentage = discount.get_text(strip=True)
    else:
        discount_percentage = None
    
    # Determine the brand/category based on product name
    category = None
    for brand in brands:
        if brand.lower() in name.lower():
            category = brand.capitalize()  # Capitalize the brand name for consistency
            break
    
    # If the product is realme or mi, treat it as Xiaomi
    if 'realme' in name.lower() or 'mi' in name.lower():
        category = 'Xiaomi'
    
    return {
        'Product Name': name,
        'Price': price,
        'Old Price': old_price,
        'Discount Percentage': discount_percentage,
        'Category': category  # Added the category (brand)
    }

# Function to scrape products from a given page
def scrape_page(page_num):
    url = base_url.format(page_num)  # Format the base URL with the current page number
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all product entries on the page
        products = soup.find_all('div', {'class': 'info'})
        
        if not products:
            return None  # Return None if no products are found, signaling the last page

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
    file_path = 'C:/Users/dell/Desktop/mobile_jumia_products.xlsx'  # Adjust the path as necessary
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Data saved to {file_path}")

# Main function to start the scraping process
def main():
    all_product_data = scrape_all_pages()  # Scrape all pages
    if all_product_data:
        save_to_excel(all_product_data)  # Save data to an Excel file

if __name__ == '__main__':
    main()
