import h5py
import csv
import os

def extract_location(nwb_file_path, channels=[4, 120]):
    try:
        with h5py.File(nwb_file_path, 'r') as f:
            location_path = 'general/extracellular_ephys/electrodes/location'
            if location_path in f:
                data = f[location_path][:]
                locations = {}
                for ch in channels:
                    if ch < len(data):
                        location = data[ch].decode("utf-8")
                        locations[ch] = location
                    else:
                        locations[ch] = None
                return locations
            else:
                print(f"'{location_path}' not found in: {nwb_file_path}")
                return None
    except Exception as e:
        print(f"Failed to open {nwb_file_path}: {e}")
        return None

def save_locations_to_csv(nwb_dir, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['NWB File', 'Channel', 'Location'])
        for filename in sorted(os.listdir(nwb_dir)):
            if filename.endswith(".nwb"):
                nwb_file_path = os.path.join(nwb_dir, filename)
                locations = extract_location(nwb_file_path)
                if locations:
                    for ch, location in locations.items():
                        writer.writerow([filename, ch, location])

nwb_directory = "/users/cpcostea/scratch/Anesthesia_data"
csv_output = "/users/cpcostea/scratch/Anesthesia_data/output.csv"


save_locations_to_csv(nwb_directory, csv_output)
