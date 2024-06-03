# import subprocess

# # Run the scrapy spider command for manga crawler and save the output to scrapy_output.txt
# with open('scrapy_output.txt', 'w') as scrapy_output:
#     subprocess.run(
#         ["scrapy", "crawl", "manga", "-o", "manga.json"],
#         check=True,
#         stdout=scrapy_output,
#         stderr=subprocess.STDOUT
#     )

# # Run the Python script and save the output to sorting_output.txt
# with open('sorting_output.txt', 'w') as sorting_output:
#     subprocess.run(
#         ["python", "sorting.py"],
#         check=True,
#         stdout=sorting_output,
#         stderr=subprocess.STDOUT
#     )

import json
from itertools import groupby
from operator import itemgetter

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while trying to open {file_path}: {e}")
        return None

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError:
        print(f"Error: Failed to write to {file_path}.")

def process_data(data):
    # Debug: Check the structure of data
    print("Data structure:", type(data))
    if isinstance(data, list) and all(isinstance(i, list) for i in data):
        # Flatten the list of lists
        data = [item for sublist in data for item in sublist]
        print("Flattened data structure:", type(data))

    # Debug: Print the first few items to inspect their structure
    print("First few items in the flattened data:", data[:5])

    # Convert "Chapter" to float and sort the data by "Title" and "Chapter"
    for item in data:
        if not isinstance(item, dict):
            print("Warning: Skipping non-dictionary item:", item)
            continue
        try:
            item['Chapter'] = float(item['Chapter'])
        except ValueError:
            print(f"Warning: Could not convert {item['Chapter']} to float. Skipping this entry.")
            continue

    data.sort(key=itemgetter('Title', 'Chapter'))

    # Group the data by "Title" and order the chapters numerically
    grouped_data = []
    for key, group in groupby(data, key=itemgetter('Title')):
        sorted_group = sorted(list(group), key=itemgetter('Chapter'))
        grouped_data.append(sorted_group)
    
    return grouped_data

def sort_json(file_path):
    data = load_json(file_path)
    if data is None:
        return

    grouped_data = process_data(data)
    save_json(grouped_data, file_path)

# Ensure you are passing the correct path to the JSON file
myVar = 'manga.json'
sort_json(myVar)
