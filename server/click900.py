import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from driverson import Driverson
import openpyxl
import concurrent.futures

# Function to process a chunk of URLs
def process_url_chunk(url_chunk, start_index):
    driver = Driverson()  # Initialize the browser
    driver.maximize_window()
    
    for index, url in enumerate(url_chunk, start=start_index):
        for i in range(900):
            driver.get(url)  # Open browser to the URL
            time.sleep(3)  # Adjust sleep time for page load
            print(f"This is {index}th url, Completed 900 clicks for link in {i + 1}")
    
    driver.quit()  # Close the browser once done

# Load the workbook and select the active sheet
file_path = 'C:/Users/jiang/Desktop/日常学习/日常学习/药销通/脚本/auto click/JCYY_cl/yyh.xlsx'
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Initialize an empty list to store the F column data
f_column_data = []

# Loop through the rows and get the data from column F (index 6)
for row in sheet.iter_rows(min_col=6, max_col=6, min_row=2, values_only=True):
    f_column_data.append(row[0])  # row[0] is the F column value for the current row

# Print the collected data from column F
print(f_column_data)

# Parameters for multi-threading
start_index = 3  # Start from the fourth URL (index 3)
total_urls = len(f_column_data)  # Total number of URLs
num_threads = 4  # Number of threads
remaining_urls = total_urls - start_index  # Remaining URLs after the first three
chunk_size = (remaining_urls // num_threads) + (remaining_urls % num_threads > 0)  # URLs per thread

# Create chunks of URLs to be processed by each thread, starting from the fourth URL
url_chunks = [f_column_data[i:i + chunk_size] for i in range(start_index, total_urls, chunk_size)]

# Start multi-threading using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for i, chunk in enumerate(url_chunks):
        start_index_for_chunk = start_index + i * chunk_size  # Calculate the starting index for each thread
        futures.append(executor.submit(process_url_chunk, chunk, start_index_for_chunk))

    # Wait for all threads to complete
    concurrent.futures.wait(futures)

print("All URLs processed.")
