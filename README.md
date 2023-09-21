# YT2RSS
This Python script is designed to convert your YouTube channel subscriptions from a JSON format (commonly exported from services like NewPipe) into an OPML file, which can be easily imported into various RSS feed readers.

## How it works

1. **Input JSON File**: The script takes as input a JSON file named `newpipe-subscriptions.json`, which contains information about your YouTube channel subscriptions.

2. **Extract URLs**: It extracts the subscription URLs from the JSON file and modifies them to generate valid RSS feed URLs using the YouTube channel IDs.

3. **Extract Names**: It also extracts the names of the YouTube channels from the JSON file.

4. **Create Text Files**: The script creates two text files, `urls.txt` and `names.txt`, to store the modified URLs and channel names, respectively.

5. **Create OPML File**: Finally, it generates an OPML file named `feeds.opml`, which includes the channel names and their corresponding RSS feed URLs.

6. **Cleanup**: Temporary text files (`urls.txt` and `names.txt`) are deleted after creating the OPML file.

## Usage

1. **Export NewPipe Subscriptions**: First, export your YouTube channel subscriptions from NewPipe in JSON format and save the file as `newpipe-subscriptions.json`.

2. **Run the Script**: Execute the script in the same directory where you have the `newpipe-subscriptions.json` file.

   ```bash
   python script.py
   ```

3. **Import OPML File**: You can now import the generated `feeds.opml` file into your preferred RSS feed reader. The OPML file will contain all the YouTube channel subscriptions with their proper names.

4. **Cleanup (Optional)**: The script will automatically delete the temporary text files (`urls.txt` and `names.txt`) after creating the OPML file.

## Important Note

- This script is designed for use with NewPipe subscription exports. Ensure that your JSON file follows the expected format.


Feel free to customize the script or reach out for assistance if you encounter any issues. Enjoy reading your YouTube channel subscriptions in your RSS feed reader!
