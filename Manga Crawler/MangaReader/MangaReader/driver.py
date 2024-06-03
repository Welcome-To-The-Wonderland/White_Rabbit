import subprocess

# Run the scrapy spider command for manga crawler 
subprocess.run(["scrapy", "crawl", "manga", "-o", "manga.json"], check=True)

# Run the Python script
subprocess.run(["python", "sorting.py"], check=True)


# Run the Python script and save the output to sorting_output.txt
with open('sorting_output.txt', 'w') as sorting_output:
    subprocess.run(
        ["python", "sorting.py"],
        check=True,
        stdout=sorting_output,
        stderr=subprocess.STDOUT
    )