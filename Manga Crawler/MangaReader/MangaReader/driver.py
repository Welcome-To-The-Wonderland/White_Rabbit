import subprocess

# Run the scrapy command
subprocess.run(["scrapy", "crawl", "manga", "-o", "manga.json"], check=True)

# Run the Python script
subprocess.run(["python", "sorting.py"], check=True)