import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Only Apple iPads
brands = ['apple']

# Base URL for iPads (Jumia)
base_url = 'https://www.jumia.com.eg/ipads/'

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
    
    # Only look for products with the brand "Apple"
    category = None
    for brand in brands:
        if brand.lower() in name.lower():
            category = brand.capitalize()  # Capitalize the brand name for consistency
            break

    return {
        'Product Name': name,
        'Price': price,
        'Old Price': old_price,
        'Discount Percentage': discount_percentage,
        'Category': category  # Brand
    }

# Function to scrape products from a given page
def scrape_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all product entries on the page
        products = soup.find_all('div', {'class': 'info'})
        
        if not products:
            print("No products found on the page.")
            return None  # If no products are found, return None

        page_data = []
        for product in products:
            product_data = get_product_data(product)
            page_data.append(product_data)
        return page_data
    else:
        print(f"Failed to retrieve the page.")
        return None

# Function to save data to an Excel file
def save_to_excel(data):
    df = pd.DataFrame(data)
    # Specify a path to save the Excel file
    file_path = 'C:/Users/dell/Desktop/ipads_jumia_products.xlsx'  # Adjust the path as necessary
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Data saved to {file_path}")

# Main function to start the scraping process
def main():
    print("Scraping the page...")
    all_product_data = scrape_page()  # Scrape the single page
    
    if all_product_data:
        save_to_excel(all_product_data)  # Save data to an Excel file

if __name__ == '__main__':
    main()