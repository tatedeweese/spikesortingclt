import os
# compiles parameters in one place for subsequent spike sorting

# ecephys_spike_sorting: sglx_multi_run_pipeline.py parameters
logName = "" # Default: runName_log.csv
npx_directory = r'C:\Users\tdeweese\Documents\test-data' # folder above _g0
# run_specs = name, gate, trigger and probes to process
runName = '012223_INS10_DT3_rec' # run_specs, before _g0 in folder name
run_specs = [[runName, '0', '0,0', '0', ['cortex'] ]]
catGT_dest = "" # Default: npx_directory/runName_g0_out
run_CatGT = True
runTPrime = True
modules = [  # comment out undesired modules 
    'kilosort_helper',
    'kilosort_postprocessing',
    'noise_templates',
    # 'mean_waveforms',
    'quality_metrics'
]
json_directory = "" # Default: ecephys_spike_sorting/json_files

# burst-detector
burst_detector_path = r'C:\Users\tdeweese\Documents\SpikeSorting\burst-detector'

# conda environment names
ecephys_env = "ece_pyks2"
phy_env = "phy2"
burst_env = "burst-detector"

### DO NOT EDIT BELOW ###
# Set default names if not defined above
if not catGT_dest:
    catGT_dest = os.path.join(npx_directory, f"{runName}_g0_out")
if not json_directory:
    ecephys_head = os.path.dirname(ecephys_directory)
    json_directory = os.path.join(ecephys_head, "json_files")
if not logName:
    logName = f"{runName}_log.csv"