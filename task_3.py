import requests
import re
import os

# --- Configuration ---
# The fixed URL you want to scrape
TARGET_URL = 'https://www.google.com' 
# The file to save the extracted title to
OUTPUT_FILENAME = 'webpage_title.txt' 

def scrape_and_save_title(url, filename):
    """
    Fetches a webpage, extracts its HTML title, and saves the title to a file.
    """
    print(f"Attempting to fetch data from: {url}")
    
    try:
        # 1. Fetch the webpage content using the requests library
        response = requests.get(url, timeout=10)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status() 
        
        # Get the HTML content as a string
        html_content = response.text
        
        # 2. Scrape the title using a Regular Expression (or a simple string search)
        # The regex looks for the content between <title> and </title> tags
        # re.IGNORECASE is used to match <Title>, <TITLE>, etc.
        match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
        
        if match:
            # The title is in the first capturing group (group(1))
            title = match.group(1).strip()
            print(f"✅ Successfully scraped Title: \"{title}\"")
            
            # 3. Save the scraped title to a file (File Handling)
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Webpage URL: {url}\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"Page Title: {title}\n")
                
                print(f"✅ Title successfully saved to: {os.path.abspath(filename)}")
                
            except IOError:
                print(f"❌ Error: Could not write data to file {filename}.")
                
        else:
            print("❌ Error: Could not find the <title> tag on the page.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error during request to {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the automation script
if __name__ == "__main__":
    scrape_and_save_title(TARGET_URL, OUTPUT_FILENAME)