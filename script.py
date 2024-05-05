import json
import os

# Open the JSON file for reading
with open('newpipe-subscriptions.json', 'r', encoding='utf-8') as file:
    # Load the data into a variable
    subscriptions = json.load(file)

# Loop through each subscription object
for sub in subscriptions['subscriptions']:
    # Extract the URL from the 'url' field
    url = sub['url']

    # Replace the old URL with the new one
    new_url = url.replace('https://www.youtube.com/channel/', 'https://www.youtube.com/feeds/videos.xml?channel_id=')

    # Write the URL to a new text file
    with open('urls.txt', 'a', encoding='utf-8') as outfile:
        outfile.write(f'{new_url}\n')


# Loop through each subscription object
for sub in subscriptions['subscriptions']:
    # Extract the URL from the 'url' field
    name = sub['name']

    # Write the URL to a new text file
    with open('names.txt', 'a', encoding='utf-8') as outfile:
        outfile.write(f'{name}\n')

# Creates OPML file
def create_opml_file(urls_file, names_file, output_file):
    with open(urls_file, 'r', encoding='utf-8') as urls_file:
        feed_urls = [line.strip() for line in urls_file.readlines()]

    with open(names_file, 'r', encoding='utf-8') as names_file:
        website_names = [line.strip() for line in names_file.readlines()]

    with open(output_file, 'w', encoding='utf-8') as opml_file:
        opml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        opml_file.write('<opml version="1.0">\n')
        opml_file.write('<head>\n')
        opml_file.write('    <title>YouTube Feed</title>\n')
        opml_file.write('</head>\n')
        opml_file.write('<body>\n')

        for url, name in zip(feed_urls, website_names):
            opml_file.write(f'    <outline text="{name}" title="{name}" type="rss" xmlUrl="{url}"/>\n')

        opml_file.write('</body>\n')
        opml_file.write('</opml>\n')

# Deletes tmp files

def delete_txt_files():
    for filename in os.listdir("."):
        if filename.endswith(".txt"):
            file_path = os.path.join(".", filename)
            os.remove(file_path)

if __name__ == "__main__":
    urls_file = "urls.txt"
    names_file = "names.txt"
    output_file = "feeds.opml"
    create_opml_file(urls_file, names_file, output_file)
    print(f"OPML file '{output_file}' created successfully.")
    delete_txt_files()
