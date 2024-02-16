import os
# compiles parameters in one place for subsequent spike sorting

# ------------
# RUN COMMANDS
# ------------
run_pipeline = True # ecephys_spike_sorting/ecephys_spike_sorting/scripts/sglx_multi_run_pipeline.py
plot_units = True # burst-detector/burst_detector/plot_units.py
quality_metrics = True # ecephys_spike_sorting.modules.quality_metrics
custom_metrics = True # burst-detector/burst_detector/custom_metrics.py
phy = True # startup phy in KS_folder

burst_detector_path = r'C:\Users\tdeweese\Documents\SpikeSorting\burst-detector'
ecephys_directory = r'C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\ecephys_spike_sorting'
# conda_path = r"C:\Users\tdeweese\miniconda3"

# conda environment names
ecephys_env = "ece_pyks2"
phy_env = "phy2"
burst_env = "burst-detector"
