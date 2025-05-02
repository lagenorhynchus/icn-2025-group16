
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from pynwb import NWBFile


def create_lfp_spectrogram(nwb_file_path, lfp_acquisition_name, freq_range):
    """
    Generates a spectrogram from LFP data stored in an NWB file.

    Args:
        nwb_file_path (str): Path to the NWB file.
        lfp_acquisition_name (str): Name of the LFP acquisition in the NWB file.
        freq_range (tuple): Frequency range of interest (e.g., (1, 100)).
    """
    # 1. Error handling: Check if the NWB file exists
    if not os.path.exists(nwb_file_path):
        raise FileNotFoundError(f"NWB file not found at: {nwb_file_path}")

    try:
        # 2. Open the NWB file in read-only mode
        nwb_file = NWBFile(nwb_file_path, 'r')

        # 3. Fetch LFP data and sampling rate.  Handles potential errors
        if lfp_acquisition_name not in nwb_file.acquisition:
            nwb_file.close()
            raise KeyError(f'LFP acquisition named "{lfp_acquisition_name}" not found in the NWB file.')

        lfp_data = nwb_file.acquisition[lfp_acquisition_name].data[:]  # Load all data
        sampling_rate = nwb_file.acquisition[lfp_acquisition_name].rate

        # 4. Check if LFP data is empty
        if lfp_data.size == 0:
            nwb_file.close()
            raise ValueError('LFP data is empty.')

        # 5. Check if the sampling rate is valid
        if not isinstance(sampling_rate, (int, float)) or sampling_rate <= 0:
            nwb_file.close()
            raise ValueError('Invalid sampling rate found in the NWB file.')

        # 6. Spectrogram parameters
        window_length = 512  # Window length in samples
        overlap = int(0.75 * window_length)  # Overlap (75%)
        nfft = 1024

        # 7. Calculate the spectrogram using scipy.signal.spectrogram
        frequencies, times, sxx = signal.spectrogram(lfp_data, fs=sampling_rate,
                                                    window='hann', nperseg=window_length,
                                                    noverlap=overlap, nfft=nfft,
                                                    scaling='density')

        # 8. Visualize the spectrogram using matplotlib.pyplot.imshow
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(times, frequencies, 10 * np.log10(sxx), shading='auto', cmap='viridis')  # Use pcolormesh
        plt.colorbar(label='Power/Frequency (dB/Hz)')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (s)')
        plt.title(f'LFP Spectrogram - Anesthetized Rat - Area: {lfp_acquisition_name}')  # Include acquisition name
        plt.ylim(freq_range)  # Set frequency range
        plt.show()

        # 9. Close the NWB file
        nwb_file.close()

    except Exception as e:
        # 10. Catch and display any errors
        print(f"An error occurred: {e}")
        if 'nwb_file' in locals():  # Check if nwb_file was defined
            nwb_file.close()

if __name__ == "__main__":
    # Example usage:
    nwb_file_path = './Rat01_Insertion1_Depth1.nwb'  # Replace with your NWB file path
    lfp_acquisition_name = 'LFP'  # Replace with the correct LFP acquisition name
    freq_range = (1, 100)  # Frequency range of interest

    create_lfp_spectrogram(nwb_file_path, lfp_acquisition_name, freq_range)