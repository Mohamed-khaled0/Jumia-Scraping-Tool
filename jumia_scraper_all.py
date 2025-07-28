"""
Jumia Scraping Tool - Unified Script

Usage:
- Run this script.
- Select a category from the menu to scrape products from Jumia Egypt.
- The results will be saved as an Excel file in the current directory.

To add a new category, copy one of the functions below, adjust the brands, base_url, and filename, and decorate it with @register_scraper('Category Name').
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- CATEGORY SCRAPER REGISTRATION ---
CATEGORY_SCRAPERS = {}

def register_scraper(name):
    def decorator(func):
        CATEGORY_SCRAPERS[name] = func
        return func
    return decorator

# --- CATEGORY SCRAPER FUNCTIONS ---
# Each function below registers a category for the menu.

@register_scraper('Accessories and Cables')
def scrape_accessories_and_cables():
    brands = [
        '2B', 'Acefast', 'Adam Elements', 'Anker', 'Apple', 'Aspor', 'Aukey', 'Baseus', 'Blitz', 'Borofone', 'Buddy', 'Cable', 'Celebrat', 'Choetech', 'Corn', 'Coteetci', 'Dadu', 'Dausen', 'Devia', 'Earldom', 'Eloroby', 'EMB', 'Energiemax', 'Energizer', 'Eugizmo', 'Genai', 'General', 'Generic', 'Gerlax', 'GFUZ', 'GravaStar', 'Havit', 'Hoco', 'HP', 'Iconix', 'Iconz', 'Infinix', 'Inkax', 'Jellico', 'JOYROOM', 'JSAUX', 'K3', 'Kingleen', 'Konfulon', "L'Avvento", 'Lanex', 'Ldino', 'Ldnio', 'Lightning', 'Linein', 'Majentik', 'Manhattan', 'Mcdodo', 'Mcgear', 'Mi', 'Momax', 'MOMO', 'Moxom', 'Nillkin', 'Nubia', 'Odoyo', 'Onten', 'Oraimo', 'Orimo', 'Over', 'Pavareal', 'Powerline', 'Proda', 'Promate', 'Ravpower', 'realme', 'Recci', 'Remax', 'RockRose', 'Romoss', 'Samsung', 'Sanyon', 'Sendem', 'Shark', 'Sikenai', 'Smart Gate', 'Soda', 'Strong', 'super touch', 'Tronsmart', 'Ugreen', 'Vidivi', 'Vidvie', 'WiWU', 'WK Design', 'wopow', 'WUW', 'X-Plus', 'X-Scoot', 'XIAOMI', 'XO', 'Yesido'
    ]
    base_url = 'https://www.jumia.com.eg/mobile-phone-accessories-cables/?page={}'
    filename = 'accessories_and_cables_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Android Phones')
def scrape_android_phones():
    brands = ['Alcatel', 'Apple', 'Benco', 'Black Shark', 'CAT', 'Earldom', 'Generic', 'Honor', 'Iku', 'Infinix', 'Itel', 'Lava', 'Lenovo', 'M-Horse', 'Realme', 'Nokia', 'Nubia', 'OPPO', 'Poco', 'realme', 'Redmi', 'Samsung', 'TAG-PHONE', 'Tecno', 'unihertz', 'Vivo', 'VIVO MATTRESS', 'X-Plus', 'Xaomi', 'XIAOMI', 'ZTE']
    base_url = 'https://www.jumia.com.eg/android-phones/?page={}'
    filename = 'android_phones_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Audio and Video Accessories')
def scrape_audio_and_video_accessories():
    brands = ["2B", "A4tech", "Awei", "Axtel", "Boya", "Comica", "Corn", "Crash", "Dji", "Elgato", "FANTECH", "Forev", "GAMMA", "Generic", "Genius", "Gigamax", "Godox", "Golden King", "Goldenking", "Havit", "Hood", "HP", "HyperX", "Jabra", "Kisonili", "Kisonli", "L'Avvento", "Lenovo", "Logitech", "Manhattan", "Marvo", "Maxi", "Media Tech", "Meetion", "Microsoft", "Nacon", "Neutrik", "No Band", "Onikuma", "Ovleng", "P47", "Philips", "Point", "Porodo", "Porsh Dob", "Powerology", "Rapoo", "Razer", "Recci", "Redragon", "Rode", "Sades", "Saramonic", "Smile", "Soda", "SPEEDLINK", "Speed Link", "Standard", "SUNWIND", "Techno Zone", "TERMINATOR", "UNIC", "XO", "XTRIKE ME", "ZERO"]
    base_url = 'https://www.jumia.com.eg/computing-audio-video-accessories/?page={}'
    filename = 'audio_video_accessories_jumia.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Bluetooth Headsets')
def scrape_bluetooth_headsets():
    brands = ['Anker', 'Apple', 'B12', 'Belkin', 'Black Shark', 'Bose', 'Cardoo', 'Celebrat', 'Choetech', 'Cmf', 'Corn', 'Creative', 'Denmen', 'Devia', 'Dob', 'Earldom', 'E Train', 'Geekery', 'General', 'Generic', 'Harman', 'Hbq', 'Honor', 'Huawei', 'Iconz', 'Infinix', 'Inkax', 'iPlus', 'Itel', 'JBL', 'JOYROOM', 'Jumbo', 'Kitsound', "L'Avvento", 'Lenovo', 'Logitech', 'Majentik', 'Marshall Minor', 'Mi', 'Nothing', 'One Plus', 'OPPO', 'Oraimo', 'P47', 'Philips', 'Proda', 'Promate', 'Qcy', 'Razer', 'realme', 'Recci', 'Redmi', 'Remax', 'RENO', 'Riversong', 'Samsung', 'Skyworth', 'Smart', 'Soda', 'SODO', 'Sony', 'Soundcore', 'SOUNDPEATS', 'Sports', 'Telzeal', 'Tronsmart', 'Ugreen', 'Unitronics', 'Vidvie', 'WUW', 'XIAOMI', 'X Loud', 'XO', 'YISON', 'Yk Design', 'YooKie', 'ZERO']
    base_url = 'https://www.jumia.com.eg/mobile-phone-bluetooth-headsets/?page={}'
    filename = 'bluetooth_headsets_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Chargers and Power Adapters')
def scrape_chargers_and_power_adapters():
    brands = ['2B', 'Acefast', 'Adam Elements', 'Anker', 'Apple', 'Aspor', 'Aukey', 'Awei', 'Baseus', 'Blitz', 'Borofone', 'Buddy', 'Cable', 'Celebrat', 'Choetech', 'Corn', 'Coteetci', 'Dadu', 'Dausen', 'Devia', 'Earldom', 'Eloroby', 'EMB', 'Energiemax', 'Energizer', 'Eugizmo', 'Genai', 'General', 'Generic', 'Gerlax', 'GFUZ', 'GravaStar', 'Havit', 'Hoco', 'HP', 'Iconix', 'Iconz', 'Infinix', 'Inkax', 'Jellico', 'JOYROOM', 'JSAUX', 'K3', 'Kingleen', 'Konfulon', "L'Avvento", 'Lanex', 'Ldino', 'Ldnio', 'Lightning', 'Linein', 'Majentik', 'Manhattan', 'Mcdodo', 'Mcgear', 'Mi', 'Momax', 'MOMO', 'Moxom', 'Nillkin', 'Nubia', 'Odoyo', 'Onten', 'Oraimo', 'Orimo', 'Over', 'Pavareal', 'Powerline', 'Proda', 'Promate', 'Ravpower', 'realme', 'Recci', 'Remax', 'RockRose', 'Romoss', 'Samsung', 'Sanyon', 'Sendem', 'Shark', 'Sikenai', 'Smart Gate', 'Soda', 'Strong', 'super touch', 'Tronsmart', 'Ugreen', 'Vidivi', 'Vidvie', 'WiWU', 'WK Design', 'wopow', 'WUW', 'X-Plus', 'X-Scoot', 'XIAOMI', 'XO', 'Yesido']
    base_url = 'https://www.jumia.com.eg/mobile-phone-accessories-cables/?page={}'
    filename = 'chargers_and_power_adapters_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Computer Cables and Interconnects')
def scrape_computer_cables_and_interconnects():
    brands = ['2B', '3M', 'Adapter', 'admin', 'Anker', 'Apple', 'Baci', 'Baseus', 'Belkin', 'Black Box', 'Blitz', 'Cable', 'CABLETIME', 'Choetech', 'Cisco', 'Comma', 'D-Link', 'Dadu', 'Devia', 'Earldom', 'Eti', 'E Train', 'Fort', 'France Tech', 'General', 'Generic', 'Grand', 'Havit', 'High Quality', 'Hikvision', 'HP', 'Iconz', 'JOYROOM', 'JSAUX', 'Jumbo', 'Kongda', "L'Avvento", 'Lan', 'Lava', 'LAVVENTO', 'Ldnio', 'Leader', 'Legrand', 'Leviton', 'Manhattan', 'MOMO', 'Not Specific', 'Onten', 'Oraimo', 'Panduit Netkey', 'Point', 'Port', 'Power A', 'Premium', 'Premium Line', 'PROLINK', 'Promate', 'Raoop', 'REDERIMIDE', 'Riversong', 'Rock', 'RockRose', 'Sikenai', 'SoundKing', 'Spark Fox', 'SPEEDLINK', 'Systimax', 'Tera', 'TOTAL', 'TP-Link', 'Ugreen', 'VABi', 'Vega', 'Vidvie', 'WiWU', 'World Cables', 'WUW', 'X-Scoot', 'XO', 'Yesido', 'ZERO']
    base_url = 'https://www.jumia.com.eg/computer-cables-interconnects/?page={}#catalog-listing'
    filename = 'computer_cables_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Desktop Computers')
def scrape_desktop_computers():
    brands = ['Acer', 'Apple', 'ASUS', 'Dell', 'HP', 'Lenovo', 'MSI', 'Microsoft', 'Razer', 'Samsung', 'Toshiba', 'Xerox', 'Zotac']
    base_url = 'https://www.jumia.com.eg/desktop-computers/?page={}'
    filename = 'desktop_computers_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('External Hard Drives')
def scrape_external_hd():
    brands = ['Ugreen', 'Redragon', 'Western', 'Sandisk', 'WD', 'Sytek', 'Universal', 'Samsung']
    base_url = 'https://www.jumia.com.eg/external-hd/?page={}'
    filename = 'external_hd_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Fans and Cooling')
def scrape_fans_cooling():
    brands = ['Cooler Master', 'Corsair', 'Gigamax', 'Thermaltake', 'Ipega', 'Arctic', 'Thermal', 'Gigamax', 'SilverStone', 'Aorus', 'Techno']
    base_url = 'https://www.jumia.com.eg/computer-components-fans-cooling/?page={}'
    filename = 'fans_cooling_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Gaming Laptops')
def scrape_gaming_laptops():
    brands = ['Acer', 'Alienware', 'Apple', 'Asus', 'Dell', 'Gigabyte', 'HP', 'Lenovo', 'MSI', 'Razer', 'Samsung', 'Toshiba', 'XPG', 'Xiaomi']
    base_url = 'https://www.jumia.com.eg/gaming-laptops/?page={}'
    filename = 'gaming_laptops_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Graphics Cards')
def scrape_graphics_cards():
    brands = ['ASUS', 'MSI', 'Gigabyte', 'Zotac', 'EVGA', 'Palit', 'NVIDIA', 'AMD', 'Sapphire', 'XFX', 'PNY', 'PowerColor', 'Intel']
    base_url = 'https://www.jumia.com.eg/computer-components-graphics-cards/?page={}'
    filename = 'graphics_cards_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Internal Hard Drives')
def scrape_internal_hd():
    brands = ['Crucial', 'Lexar', 'Samsung', 'Seagate', 'Team Group', 'Toshiba', 'WD', 'Western Digital']
    base_url = 'https://www.jumia.com.eg/internal-hd/?page={}'
    filename = 'internal_hd_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('iOS Phones')
def scrape_ios_phones():
    brands = ['Apple']
    base_url = 'https://www.jumia.com.eg/ios-phones/?page={}'
    filename = 'ios_phones_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('iPads')
def scrape_ipads():
    brands = ['apple']
    base_url = 'https://www.jumia.com.eg/ipads/?page={}'
    filename = 'ipads_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Keyboards')
def scrape_keyboards():
    brands = ["2B", "A4tech", "AiTNT", "Apple", "Aula", "E Train", "Firex", "Forever", "General", "Generic", "Gigamax", "Green Lion", "HP", "Iconz", "L'Avvento", "LAVVENTO", "Logitech", "Manhattan", "Meetion", "Microsoft", "Point", "Razer", "Redragon", "Smile", "Soda", "SPEEDLINK", "Vesta", "White Shark", "XO", "ZERO"]
    base_url = 'https://www.jumia.com.eg/computer-keyboards/?page={}#catalog-listing'
    filename = 'keyboards_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Memory Cards')
def scrape_memory_cards():
    brands = ['Adata', 'ADATA', 'Angelbird', 'Apacer', 'Bavvo', 'Blex', 'Corsair', 'Crucial', 'Evo', 'Hikvision', 'Kingston', 'Lexar', 'Sandisk', 'Mushkin', 'Patriot', 'sanDisk', 'Samsung', 'Toshiba', 'Transcend', 'Verbatim', 'Vitec', 'Western Digital', 'Yesido']
    base_url = 'https://www.jumia.com.eg/mobile-phone-memory-cards/?page={}'
    filename = 'memory_cards_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Monitors')
def scrape_monitors():
    brands = ['Acer', 'Alienware', 'Aoc', 'Benq', 'Dahua', 'DELL', 'Elgato', 'Generic', 'HP', 'Lenovo', 'Lumi', 'MSI', 'Philips', 'Samsung', 'XIAOMI']
    base_url = 'https://www.jumia.com.eg/monitors/?page={}'
    filename = 'monitors_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Mouses')
def scrape_mouses():
    brands = ['2B', 'A4tech', 'Apple', 'Aula', 'E Train', 'FANTECH', 'Fd', 'Forev', 'Fort', 'Fox', 'GAMMA', 'Generic', 'Genius', 'Gigamax', 'Golden King', 'Goldenking', 'Grand', 'Havit', 'Hb', 'Hood', 'HP', 'Iconz', 'Jertech', "L'Avvento", 'Lava', 'LAVVENTO', 'Leishe', 'Lenovo', 'Logitech', 'Manhattan', 'Margo', 'Marvo', 'Meetion', 'Microsoft', 'Ox', 'Point', 'Porsh', 'R8', 'Raoop', 'Rapoo', 'Redragon', 'Smile', 'Soda', 'Soyntec', 'SPEEDLINK', 'T-Dagger', 'Twins', 'UNBLACK', 'Utopia', 'XO', 'XP', 'XTRIKE ME', 'Yafox', 'ZERO', 'ZIDLI', 'ZornWee']
    base_url = 'https://www.jumia.com.eg/mouse/?page={}#catalog-listing'
    filename = 'mouse_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Network Adapters')
def scrape_network_adapters():
    brands = ["2B", "Air Live", "Aruba", "Buddy", "D-Link", "Generic", "Gigabite", "I-ROCK", "Iconz", "Lb Link", "Legrand", "Manhattan", "Mercusys", "Netgear", "Point", "tenda", "TP-Link", "TPLink", "Ugreen"]
    base_url = 'https://www.jumia.com.eg/network-adapters/?page={}#catalog-listing'
    filename = 'network_adapters_jumia.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Network Routers')
def scrape_network_routers():
    brands = ['Air Live', 'Asus', 'D-Link', 'Generic', 'Green', 'Mercury', 'Mercusys', 'Mikrotik', 'tenda', 'TP-Link', 'TPLink', 'Ubiquiti', 'XIAOMI']
    base_url = 'https://www.jumia.com.eg/computer-networking-routers/?page={}#catalog-listing'
    filename = 'routers_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Network Hubs')
def scrape_network_hubs():
    brands = ["Adam Elements", "Baseus", "Earldom", "Generic", "Jcpal", "JSAUX", "L'Avvento", "LAVVENTO", "Manhattan", "Onten", "Promate", "QGeeM", "Recci", "TP-Link", "TPLink", "Ugreen", "WiWU", "Yesido"]
    base_url = 'https://www.jumia.com.eg/networking-hubs/?page={}#catalog-listing'
    filename = 'networking_hubs_jumia.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Network Switches')
def scrape_network_switches():
    brands = ["Air Live", "Aruba", "At Netgear", "Cisco", "D-Link", "Dtech", "Generic", "Hikvision", "Linksys", "Mercusys", "Mikrotik", "Ruiji", "Ruijie", "Tenda", "TP-Link", "TPLink"]
    base_url = 'https://www.jumia.com.eg/computer-networking-switches/?page={}#catalog-listing'
    filename = 'networking_switches_jumia.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Phone Adapters')
def scrape_phone_adapters():
    brands = ['Acefast', 'Adam Elements', 'Apple', 'Denmen', 'Devia', 'Earldom', 'Egeline', 'Generic', 'HP', 'JOYROOM', 'JSAUX', 'Ldino', 'Ldnio', 'Mcdodo', 'Powerline', 'Recci', 'Remax', 'Samsung', 'Standard', 'WiWU', 'X-Scoot', 'Yesido','OTG']
    base_url = 'https://www.jumia.com.eg/mobile-phone-adapters/?page={}'
    filename = 'adapters_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Phone Batteries')
def scrape_phone_batteries():
    brands = ['Anker', 'Awei', 'Dadu', 'Devia', 'Earldom', 'Elite', 'Energizer', 'Eveready', 'France Tech', 'Genai', 'Generic', 'Havit', 'Hoco', 'Iconz', 'JOYROOM', 'Kakusiga', 'Konfulon', "L'Avvento", 'Lanex', 'Ldnio', 'Lenovo', 'LYZ', 'Majentik', 'Matrix', 'Mi', 'Momax', 'Oraimo', 'Powerology', 'Proda', 'Promate', 'Puridea', 'Pzx', 'Ravpower', 'Recci', 'Remax', 'RENO', 'Riversong', 'RockRose', 'Samsung', 'Start', 'SUNPIN', 'Ugreen', 'Usams', 'Vidvie', 'WiWU', 'XO', 'Yesido', 'Yk Design', 'ZTE']
    base_url = 'https://www.jumia.com.eg/mobile-phone-batteries-battery-packs/?page={}'
    filename = 'mobile_batteries_and_battery_packs_jumia.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Power Banks')
def scrape_power_banks():
    brands = ['Anker', 'Awei', 'Dadu', 'Devia', 'Earldom', 'Energizer', 'Genai', 'Generic', 'Havit', 'Hoco', 'JOYROOM', 'Kakusiga', 'Konfulon', "L'Avvento", 'Lanex', 'Ldnio', 'LYZ', 'Majentik', 'Matrix', 'Mi', 'Momax', 'Oraimo', 'Powerology', 'Pzx', 'Ravpower', 'Recci', 'Remax', 'RENO', 'RockRose', 'Samsung', 'Start', 'SUNPIN', 'Ugreen', 'Usams', 'Vidvie', 'WiWU', 'XO', 'Yesido']
    base_url = 'https://www.jumia.com.eg/mlp-portable-power-banks/?page={}'
    filename = 'power_banks_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Printers')
def scrape_printers():
    brands = ["Bixolon", "Brother", "Canon", "Epson", "Generic", "HP", "Kyocera", "Lenovo", "Muratec", "Pantum", "TSC", "Xerox", "XP", "XPrinter", "Zebra"]
    base_url = 'https://www.jumia.com.eg/printers/?page={}#catalog-listing'
    filename = 'printers_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Scanners')
def scrape_scanners():
    brands = ['HP', 'TP-Link', 'Penpower', 'Ugreen', 'Canon', 'Epson','Oka']
    base_url = 'https://www.jumia.com.eg/scanners/?page={}#catalog-listing'
    filename = 'scanners_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Smart Watches')
def scrape_smart_watches():
    brands = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Garmin']
    base_url = 'https://www.jumia.com.eg/smart-watches/?page={}'
    filename = 'smart_watches_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Tablets')
def scrape_tablets():
    brands = ['honor', 'huawei', 'lenovo', 'samsung', 'xiaomi']
    base_url = 'https://www.jumia.com.eg/tablets/?page={}#catalog-listing'
    filename = 'tablets_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('USB Flash Drives')
def scrape_usb_flash_drives():
    brands = ['Adam Elements', 'Dahua', 'Eaget', 'Eti', 'Evo',  'Generic', 'Hiksemi', 'Hikvision', 'Iconix', 'Kingston', 'KIOXIA', 'Lexar', 'Normal', 'Redragon', 'Sandisk', 'Sytek', 'Universal', 'Zoser']
    base_url = 'https://www.jumia.com.eg/flash-drives/?page={}'
    filename = 'usb_flash_drives_jumia_products.xlsx'
    _scrape_category(brands, base_url, filename)

@register_scraper('Wireless Access Points')
def scrape_wireless_access_points():
    brands = ['Air Live', 'Aruba', 'D-Link', 'Grandstream', 'Linksys', 'Mercusys', 'Mikrotik', 'Ruijie', 'Tenda', 'TP-Link', 'TPLink']
    base_url = 'https://www.jumia.com.eg/wireless-access-points/?page={}#catalog-listing'
    filename = 'wireless_access_points.xlsx'
    _scrape_category(brands, base_url, filename)

# --- GENERIC SCRAPER LOGIC ---
def _scrape_category(brands, base_url, filename):
    """Scrape all pages for a category and save to Excel."""
    def get_product_data(product):
        name = product.find('h3', {'class': 'name'}).get_text(strip=True)
        price = product.find('div', {'class': 'prc'}).get_text(strip=True)
        link_tag = product.find('a', {'class': 'core'})
        link = 'https://www.jumia.com.eg' + link_tag['href'] if link_tag else None
        img_tag = product.find('img', {'class': 'img'})
        img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None
        category = next((brand for brand in brands if brand.lower() in name.lower()), 'Other')
        return {
            'Product Name': name,
            'Price': price,
            'Product Link': link,
            'Image URL': img_url,
            'Category': category
        }
    all_product_data = []
    page_num = 1
    while True:
        print(f"Scraping page {page_num}...")
        url = base_url.format(page_num)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_num}.")
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('article', {'class': 'prd _fb col c-prd'})
        if not products:
            print(f"No products found on page {page_num}. Stopping scraping.")
            break
        for product in products:
            product_data = get_product_data(product)
            all_product_data.append(product_data)
        page_num += 1
        time.sleep(2)  # Be polite to the server
    if all_product_data:
        df = pd.DataFrame(all_product_data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"Data saved to {filename}")
    else:
        print("No data scraped.")

# --- MAIN MENU ---
def main():
    print("\nJumia Scraping Tool - Unified Script\n")
    print("Select one or more categories to scrape (comma-separated, e.g. 1,3,5):")
    for i, name in enumerate(CATEGORY_SCRAPERS.keys(), 1):
        print(f"{i}. {name}")
    try:
        choices = input("\nEnter the number(s) of the category: ")
        indices = [int(x.strip()) for x in choices.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(CATEGORY_SCRAPERS):
                print(f"\n--- Scraping: {list(CATEGORY_SCRAPERS.keys())[idx-1]} ---")
                list(CATEGORY_SCRAPERS.values())[idx-1]()
            else:
                print(f"Invalid choice: {idx}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main() 