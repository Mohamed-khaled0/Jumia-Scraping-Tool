# Jumia Scraping Tool 

## Overview
Easy-to-use Python script to scrape product data from any category on Jumia Egypt.  
Choose one or more categories from the menu, and the script outputs an Excel file per category with all product details.

## Features
- **All Categories in One Place**  
  Every original category script is now a menu option—no duplication.  
- **Multi‑Select Menu**  
  Enter `1,3,5` to scrape multiple categories in one run.  
- **Generic Scraper Logic**  
  Shared code for requests, parsing, rate‑limiting, and exporting.  
- **Easy to Extend**  
  Add a new category by copying a function, updating `brands`, `base_url`, and `filename`, then decorating with `@register_scraper('Your Category')`.

## Prerequisites
- Python 3.x  
- Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/jumia-scraping-tool.git
   cd jumia-scraping-tool

2. **(Recommended) Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies**  
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl

4. **Usage**  
   ```bash
   python jumia_scraper_all.py

Example

Select categories to scrape (e.g. 1,3,5):
1. Accessories and Cables
2. Android Phones
3. Audio and Video Accessories
...
Enter numbers: 2,4

--- Scraping: Android Phones ---
Data saved to android_phones_jumia_products.xlsx

--- Scraping: Bluetooth Headsets ---
Data saved to bluetooth_headsets_jumia_products.xlsx
