# icn-2025-group16
Final project for Computational Neuroscience Group 16
New Draft Abstract: Cortical Dynamics under Anesthesia
Understanding the dynamics of brain oscillations during anesthesia is essential for elucidating how altered states of consciousness affect cortical information processing. Ketamine/xylazine anesthesia is known to induce prominent slow-wave activity (SWA), characterized by alternating cortical up- and down-states. Using a publicly available high-resolution electrophysiological dataset collected from the neocortex of ketamine/xylazine-anesthetized rats (Horváth et al., 2021), we aim to explore the laminar-specific spectral architecture and phase-amplitude coupling (PAC) within and across cortical regions.

The dataset includes wideband local field potential (LFP) recordings from 128-site silicon probes inserted into primary sensory, motor, and parietal association cortices. These recordings provide access to continuous spontaneous neural activity, ideal for characterizing oscillatory patterns during SWA. Previous studies have shown that slow oscillations (~1 Hz) during anesthesia mimic features of non-REM sleep and are implicated in memory consolidation and synaptic downscaling (Fiáth et al., 2016; Neske, 2015).

We will perform spectral decomposition using Fourier and wavelet transforms to extract time-frequency features of SWA and its interaction with higher-frequency oscillations (e.g., gamma). Furthermore, we will assess PAC, focusing on coupling between the phase of low-frequency rhythms (delta, theta) and the amplitude of higher-frequency components. These analyses will be performed in a layer-resolved manner to uncover depth-dependent mechanisms of oscillatory coordination.

Hypothesis: Cortical slow-wave activity during ketamine/xylazine anesthesia exhibits robust phase-amplitude coupling that varies across cortical layers and regions, reflecting structured laminar dynamics underlying unconscious states.

Required Data: LFP recordings from anesthetized rats across cortical depths and regions; recording metadata including cortical area, insertion depth, and layer localization.

Analysis Techniques:
-Spectral Analysis:
Fourier Transform: Decompose signals into their frequency components.
Wavelet Transform: Capture time-frequency characteristics of oscillations.
-Phase-Amplitude Coupling (PAC):
Measurement of modulation indices to quantify low-frequency phase/high-frequency amplitude interactions across layers

Dataset derived from: https://www.nature.com/articles/s41597-021-00970-3
Data: https://gin.g-node.org/UlbertLab/High_Resolution_Cortical_Spikes

Code availability
All software used for the visualization, processing and analysis of this dataset are open access or custom written, Python- and MATLAB-based programs. The Kilosort2 MATLAB package was used for spike sorting (https://github.com/MouseLand/Kilosort; version 2.0; commit date, 8 April 2019)37, and the Phy Python module for subsequent manual curation of the data (https://github.com/cortex-lab/phy; version 2.0b1; release date, 7 February 2020). Spatial and temporal features of the single unit spike waveforms were calculated using custom MATLAB scripts or the CellExplorer MATLAB module (https://cellexplorer.org/; https://github.com/petersenpeter/CellExplorer; version 1.2; commit date, 25 September 2020)40. Single unit quality metrics were computed using the SpikeMetrics module (https://github.com/SpikeInterface/spikemetrics; version 0.2.2; commit date, 30 December 2020) of the SpikeInterface Python-based framework (https://github.com/SpikeInterface/spikeinterface; version 0.11.0; commit date, 10 December 2020)36. SpikeMetrics relies on the code of the quality metrics module developed at the Allen Institute for Brain Science (https://github.com/AllenInstitute/ecephys_spike_sorting/tree/master/ecephys_spike_sorting/modules/quality_metrics)3. NWB files were created using the MatNWB (https://github.com/NeurodataWithoutBorders/matnwb; version 2.2.4.0; commit data, 9 February 2021) application programming interface.
