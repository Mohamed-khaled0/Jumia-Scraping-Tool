# Jumia Scraping Tool

## Overview
This repository contains a Python script designed to scrape product data from specific categories on the Jumia Egypt website. The script extracts product information such as name, price, old price, and discount percentage and saves the data into an Excel file.

## Features
- Scrapes all pages of a specific product category.
- Extracts product details:
  - **Product Name**
  - **Price**
  - **Product Link**
  - **Product Category**
  - **Product Image**
- Saves data into an Excel file.

## Prerequisites
- Python 3.x installed on your system.
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

Install the required libraries using:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Usage
1. Clone the repository or copy the script.
2. Open the script file and set the base URL to the desired Jumia category.
   ```python
   base_url = 'https://www.jumia.com.eg/computing-audio-video-accessories/?page={}' OR  Add your url here  
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```
4. The scraped data will be saved as an Excel file in the specified location:
   ```
   C:/Users/dell/Desktop/audio_video_accessories_jumia.xlsx
   ```
