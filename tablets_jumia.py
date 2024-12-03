import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of tablet brands (can be extended or modified as needed)
brands = [
    'honor', 'huawei', 'lenovo', 'samsung', 'xiaomi'
]

# Base URL for tablets (assumed to be a single page here)
base_url = 'https://www.jumia.com.eg/other-tablets/honor--huawei--lenovo--samsung--xiaomi/#catalog-listing'

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
def scrape_page():
    url = base_url  # Use the base URL directly (assuming only one page)
    response = requests.get(url)
    
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
    file_path = 'C:/Users/dell/Desktop/tablets_jumia_products.xlsx'  # Adjust the path as necessary
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
