import os
from pydub import AudioSegment

# Parent folder containing all subfolders
parent_folder = "./data/train"

# Output folder to save combined files
output_folder = "./test"
os.makedirs(output_folder, exist_ok=True)

# Initialize a dictionary to hold lists of files for each sound index
sound_files = {f"{i:02d}": [] for i in range(1, 53)}

# Traverse subfolders and gather files
for root, _, files in os.walk(parent_folder):
    for file in files:
        if file.endswith(".wav"):
            # Extract sound index (last 2 characters before .wav)
            sound_index = file[-6:-4]
            if sound_index in sound_files:
                sound_files[sound_index].append(os.path.join(root, file))

# Process and combine sounds for each index
for sound_index, file_list in sound_files.items():
    if not file_list:
        continue  # Skip if no files for this sound index

    # Sort files alphabetically by speaker name (first part of filename)
    file_list.sort(key=lambda x: os.path.basename(x))

    # Combine files
    combined_sound = AudioSegment.empty()
    for file_path in file_list:
        sound = AudioSegment.from_wav(file_path)
        combined_sound += sound

    # Export combined sound to output folder
    output_path = os.path.join(output_folder, f"combined_{sound_index}.wav")
    combined_sound.export(output_path, format="wav")
    print(f"Combined file for sound index {sound_index} saved at {output_path}")