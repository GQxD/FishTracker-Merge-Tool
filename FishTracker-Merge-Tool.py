import os
import pandas as pd

# 1. Define the folder containing the text files
source_folder = rr"/path/to/your/folder"
output_file = os.path.join(source_folder, "CSOT_merged.txt")  

# 2. Initialize a list to store the DataFrames
all_data = []

# 3. Loop through all TXT files in the folder
for file_name in os.listdir(source_folder):
    if file_name.endswith("_tracks.txt"):  # Filter: files ending with "tracks.txt"
        file_path = os.path.join(source_folder, file_name)
        
        # Read the TXT file into a DataFrame with ";" as the separator
        df = pd.read_csv(file_path, delimiter=";") 
        
        # Add a "File" column with the file name
        df["File"] = file_name  
        
        # Extract the part of the file name from the 5th to the 15th character for the "Date" column
        Date_str = file_name[5:15]  # Extract characters from 5 to 15 (index 4 to 14)
        df["Date"] = Date_str  # Add the Date column

        # Extract the part of the file name from the 16th to the 22nd character for the "Time" column
        time_str = file_name[16:22]  # Extract characters from 16 to 22 (index 15 to 21)
        
        # Add ":" between each pair of digits (format 14:05:65)
        if len(time_str) == 6:
            formatted_time = f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:]}"  # Transform to "14:05:65"
        else:
            formatted_time = time_str  # If the string is not in the correct format, leave it as is
        
        df["Time"] = formatted_time  # Add the "Time" column with the formatted value
        
        # Add the processed DataFrame to the list
        all_data.append(df)
        
        # Define the output name based on the first file
        if output_file is None:
            output_file = os.path.join(
                source_folder, file_name[:15] + "_merged.txt"
            )

# 4. Combine all DataFrames into one
if all_data:
    combined_data = pd.concat(all_data, ignore_index=True)
    
    # 5. Save the final file with ";" as the separator
    combined_data.to_csv(output_file, sep=";", index=False)
    print(f"Combined file created: {output_file}")
else:
    print("No matching files (ending with 'tracks') were found in the folder.")
