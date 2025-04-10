# FishTracker Merge Tools

## Overview

This Python script processes multiple text files from a specified folder, extracts relevant information from filenames, and combines the data into a single output file. It is designed to work with exports from version 0.1 of the FishTracker software.

## Features

- Processes files ending with `_tracks.txt`.
- Extracts `Date` and `Time` information from filenames.
- Combines data into a single CSV file with ";" as the delimiter.
- Includes error handling to ensure robust processing.

## Requirements

- Python 3.x
- `pandas` library

## How to Use

1. Place the text files to be processed in a folder.
2. Update the `source_folder` variable in the script with the path to your folder.
3. Run the script:
   ```bash
   python script_name.py
   ```
4. The combined output file will be saved in the same folder.

## Error Handling

The script uses `try-except` blocks to handle errors during file processing. If an error occurs, it will be logged, and the script will continue processing other files.

## Compatibility

This script is tailored for FishTracker version 0.1 exports. Ensure that filenames follow the expected format for correct processing.

## License

This project is licensed under the terms of the GNU General Public License v3.0.  
You can find the full license text [here](https://www.gnu.org/licenses/gpl-3.0.en.html).