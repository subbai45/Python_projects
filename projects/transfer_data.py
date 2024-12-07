import shutil
import os

# Source file path
source_path = r"E:\movies\(Movies4u.Vip).Devara Part 1 2024 HDTC 1080p Hindi + Multi 4 x264 AAC HC-ESub 5.9Gb.mkv"

# Destination file path (including the file name at the destination)
destination_path = os.path.join(r"F:\LOST.DIR", "(Movies4u.Vip).Devara Part 1 2024 HDTC 1080p Hindi + Multi 4 x264 AAC HC-ESub 5.9Gb.mkv")

# Transfer the file
try:
    shutil.copy2(source_path, destination_path)
    print("File transfer completed!")
except OSError as e:
    print(f"Error: {e}")
