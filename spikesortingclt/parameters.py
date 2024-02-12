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


# ----------------------------------
# SGLX_MULTI_RUN_PIPELINE PARAMETERS
# ----------------------------------
logName = "" # Default: runName_log.csv
npx_directory = r'D:\\' # C:\Users\tdeweese\Documents\test-data' # folder above _ga (e.g. g0)
run_specs = [ # run_specs = name, gate, trigger and probes to process
    ['012223_INS10_DT3_rec', '0', '0,0', '0', ['cortex']]
]
# CATGT PARAMETERS
run_CatGT = True
catGT_dest = "" # Default: npx_directory/runName_ga_out (if multiple runNames will use first)
process_lf = False
catGT_cmd_string = '-prb_fld -out_prb_fld -apfilter=butter,12,300,10000 -lffilter=butter,12,1,500 -gfix=0.4,0.10,0.02 '
ni_present = True # will validate this
ni_extract_string = '-xa=0,0,0,1,3,500 -xia=0,0,1,3,3,0 -xd=0,0,-1,1,50 -xid=0,0,-1,2,1.7 -xid=0,0,-1,3,5'
# TPRIME PARAMETERS
runTPrime = True
# MODULES LIST
modules = [  # comment out undesired modules 
    'kilosort_helper',
    'kilosort_postprocessing',
    'noise_templates',
    # 'mean_waveforms',
    'quality_metrics'
]
json_directory = "" # Default: ecephys_spike_sorting/json_files

# --------------
# CLT PARAMETERS (should only need to set once)
# --------------
burst_detector_path = r'C:\Users\tdeweese\Documents\SpikeSorting\burst-detector'
ecephys_directory = r'C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\ecephys_spike_sorting'

# conda environment names
ecephys_env = "ece_pyks2"
phy_env = "phy2"
burst_env = "burst-detector"

### DO NOT EDIT BELOW ###
# Set default names if not defined above
runName = run_specs[0][0]
if not catGT_dest:
    # edge-case if npx_directory is drive
    npx_directory = npx_directory.rstrip('\\')
    npx_directory = npx_directory.rstrip('/')
    if len(npx_directory) == 2: # drive
        catGT_dest = os.path.join(npx_directory, os.sep, f"{runName}_g0_out")
        print(catGT_dest)
    else:
        catGT_dest = os.path.join(npx_directory, f"{runName}_g0_out")
if not json_directory:
    ecephys_head = os.path.dirname(ecephys_directory)
    json_directory = os.path.join(ecephys_head, "json_files")
if not logName:
    logName = f"{runName}_log.csv"