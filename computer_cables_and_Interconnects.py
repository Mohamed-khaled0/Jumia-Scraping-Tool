import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of brands to classify products
brands = [
    '2B', '3M', 'Adapter', 'admin', 'Anker', 'Apple', 'Baci', 'Baseus', 'Belkin', 'Black Box', 'Blitz', 'Cable',
    'CABLETIME', 'Choetech', 'Cisco', 'Comma', 'D-Link', 'Dadu', 'Devia', 'Earldom', 'Eti', 'E Train', 'Fort',
    'France Tech', 'General', 'Generic', 'Grand', 'Havit', 'High Quality', 'Hikvision', 'HP', 'Iconz', 'JOYROOM',
    'JSAUX', 'Jumbo', 'Kongda', "L'Avvento", 'Lan', 'Lava', 'LAVVENTO', 'Ldnio', 'Leader', 'Legrand', 'Leviton',
    'Manhattan', 'MOMO', 'Not Specific', 'Onten', 'Oraimo', 'Panduit Netkey', 'Point', 'Port', 'Power A', 'Premium',
    'Premium Line', 'PROLINK', 'Promate', 'Raoop', 'REDERIMIDE', 'Riversong', 'Rock', 'RockRose', 'Sikenai',
    'SoundKing', 'Spark Fox', 'SPEEDLINK', 'Systimax', 'Tera', 'TOTAL', 'TP-Link', 'Ugreen', 'VABi', 'Vega', 'Vidvie',
    'WiWU', 'World Cables', 'WUW', 'X-Scoot', 'XO', 'Yesido', 'ZERO'
]

def get_product_data(product):
    try:
        # Extract product name
        name = product.find('h3', {'class': 'name'}).get_text(strip=True)
        
        # Extract price
        price = product.find('div', {'class': 'prc'}).get_text(strip=True)

        # Extract product link
        link_tag = product.find('a', {'class': 'core'})
        link = 'https://www.jumia.com.eg' + link_tag['href'] if link_tag else None

        # Extract product image URL
        img_tag = product.find('img', {'class': 'img'})
        img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None

        # Determine the category (brand) based on product name
        category = "Unknown Chinese brand"
        for brand in brands:
            if brand.lower() in name.lower():
                category = brand
                break

        return {
            'Product Name': name,
            'Price': price,
            'Product Link': link,
            'Image URL': img_url,
            'Category': category
        }
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None


def scrape_page(page_url):
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('article', {'class': 'prd _fb col c-prd'})
            
            if not products:
                return None

            page_data = []
            for product in products:
                product_data = get_product_data(product)
                if product_data:
                    page_data.append(product_data)
            return page_data
        else:
            print(f"Failed to retrieve page. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error scraping page: {e}")
        return None


def save_to_excel(data):
    df = pd.DataFrame(data)
    file_path = 'C:/Users/dell/Desktop/computer_cables_products.xlsx'
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Data saved to {file_path}")


def main():
    base_url = 'https://www.jumia.com.eg/computer-cables-interconnects/?page={}#catalog-listing'
    all_product_data = []
    page_num = 1

    while True:
        print(f"Scraping page {page_num}...")
        page_url = base_url.format(page_num)
        page_data = scrape_page(page_url)

        if not page_data:
            print(f"No products found on page {page_num}. Stopping scraping.")
            break

        all_product_data.extend(page_data)
        page_num += 1
        time.sleep(2)  # Add delay to avoid overloading the server

    if all_product_data:
        save_to_excel(all_product_data)


if __name__ == '__main__':
    main()
