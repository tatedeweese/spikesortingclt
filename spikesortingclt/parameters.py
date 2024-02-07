import os
# compiles parameters in one place for subsequent spike sorting

# ecephys_spike_sorting: create_input_json.py
ecephys_directory = r'C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\ecephys_spike_sorting'
kilosort_repository = r'C:\Users\tdeweese\Documents\SpikeSorting\Kilosort-2.5'
KS2ver = '2.5' 
npy_matlab_repository = r'C:\Users\tdeweese\Documents\MATLAB\npy-matlab'
catGTPath = r'C:\Users\tdeweese\Documents\SpikeSorting\CatGT-win'
tPrime_path = r'C:\Users\tdeweese\Documents\SpikeSorting\TPrime-win'
cWaves_path = r'C:\Users\tdeweese\Documents\SpikeSorting\C_Waves-win'

# ecephys_spike_sorting: sglx_multi_run_pipeline.py parameters
logName = 'INS10_log.csv' # can be anything you want
npx_directory = r'C:\Users\tdeweese\Documents\test-data' # folder above _g0
runName = '012223_INS10_DT3_rec' # run_specs, before _g0 in folder name
gateIndex = '0' # run_specs, won't really change this
triggers = '0,0' # run_specs
probes = '0' # run_specs
brainRegions = ['cortex'] # run_specs
catGT_dest = "" # default is npx_directory/runName_g0_out
run_CatGT = True
runTPrime = True
modules = [  # comment out undesired modules 
    'kilosort_helper',
    'kilosort_postprocessing',
    'noise_templates',
    # 'mean_waveforms',
    'quality_metrics'
]
json_directory = "" # default is ecephys_spike_sorting/json_files

# burst-detector
burst_detector_path = r'C:\Users\tdeweese\Documents\SpikeSorting\burst-detector'

# conda environment names
ecephys_env = "ece_pyks2"
phy_env = "phy2"
burst_env = "burst-detector"
conda_activate_path = r'"C:\Users\tdeweese\miniconda3\Scripts\activate.bat"'

### DO NOT EDIT BELOW ###
if not catGT_dest:
    catGT_dest = os.path.join(npx_directory, f"{runName}_g0_out")
if not json_directory:
    ecephys_head = os.path.dirname(ecephys_directory)
    json_directory = os.path.join(ecephys_head, "json_files")
run_specs = [runName, gateIndex, triggers, probes, brainRegions]