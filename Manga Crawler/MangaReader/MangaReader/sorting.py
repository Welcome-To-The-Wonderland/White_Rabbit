import json
from itertools import groupby
from operator import itemgetter

def sort_json():
    with open('manga.json', 'r') as f:
        data = json.load(f)

    # Convert "Chapter" to float and sort the data by "Title" and "Chapter"
    for item in data:
        item['Chapter'] = float(item['Chapter'])
    data.sort(key=itemgetter('Title', 'Chapter'))

    # Group the data by "Title"
    grouped_data = []
    for key, group in groupby(data, key=itemgetter('Title')):
        grouped_data.append(list(group))

    with open('manga.json', 'w') as f:
        json.dump(grouped_data, f, indent=4)

sort_json()