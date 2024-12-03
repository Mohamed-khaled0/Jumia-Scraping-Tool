import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of brands for fans & cooling products
brands = [
    'Cooler Master', 'Corsair', 'Gigamax', 'Thermaltake', 'Ipega', 
    'Arctic', 'Thermal', 'Gigamax', 'SilverStone', 'Aorus', 'Techno'
]

# Base URL for fans & cooling category with page placeholder
base_url = 'https://www.jumia.com.eg/computer-components-fans-cooling/?page={}'


# Function to get product data from each product div
def get_product_data(product):
    # Extract product name
    name = product.find('h3', {'class': 'name'}).get_text(strip=True)

    # Extract price (excluding the old price and discount percentage)
    price = product.find('div', {'class': 'prc'}).get_text(strip=True)

    # Extract product link (adjusted to get correct href)
    link_tag = product.find('a', {'class': 'core'})  # Check for correct class for the product link
    link = 'https://www.jumia.com.eg' + link_tag['href'] if link_tag else None

    # Extract product image URL (adjusted to get data-src)
    img_tag = product.find('img', {'class': 'img'})
    img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None

    # Ensure the image URL is valid
    if img_url and not img_url.startswith('http'):
        img_url = 'https:' + img_url  # Ensure the image URL starts with "https:"

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
    url = base_url.format(page_num)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all product entries on the page (adjusted to target correct divs)
        products = soup.find_all('article', {'class': 'prd _fb col c-prd'})  # Adjusted to find 'article' tags
        
        if not products:
            return None

        page_data = []
        for product in products:
            product_data = get_product_data(product)
            page_data.append(product_data)
        return page_data
    else:
        print(f"Failed to retrieve page {page_num}.")
        return None


# Function to scrape all pages
def scrape_all_pages():
    all_product_data = []
    page_num = 1

    while True:
        print(f"Scraping page {page_num}...")
        page_data = scrape_page(page_num)
        
        if not page_data:
            print(f"No products found on page {page_num}. Stopping scraping.")
            break
        
        all_product_data.extend(page_data)
        page_num += 1
        time.sleep(2)  # Add a delay to avoid overloading the server
    
    return all_product_data


# Function to save data to an Excel file
def save_to_excel(data):
    df = pd.DataFrame(data)
    file_path = 'C:/Users/dell/Desktop/fans_cooling_jumia_products.xlsx'  # Adjust the path
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Data saved to {file_path}")


# Main function to start scraping
def main():
    all_product_data = scrape_all_pages()
    if all_product_data:
        save_to_excel(all_product_data)


if __name__ == '__main__':
    main()
