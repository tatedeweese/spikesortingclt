from parameters import *
import os
import json

# ecephys: sglx_multi_run_pipeline.py
os.makedirs(catGT_dest, exist_ok=True)
os.makedirs(json_directory, exist_ok=True)
scripts_folder = os.path.join(ecephys_directory, "scripts")
sglx_file = os.path.join(scripts_folder, "sglx_multi_run_pipeline.py")
clt_folder = os.path.dirname(os.path.realpath(__file__))
clt_head_folder = os.path.dirname(clt_folder)

# ecephys: quality_metrics
quality_input_json = os.path.join(json_directory, f"{runName}_imec0-input.json")
quality_output_json = os.path.join(json_directory, f"{runName}_imec0-output.json")

# burst-detector
plot_units = os.path.join(burst_detector_path, "burst_detector", "plot_units.py")
custom_metrics = os.path.join(burst_detector_path, "burst_detector", "custom_metrics.py")
# create json
burst_input_json_path = os.path.join(burst_detector_path, "json_files", f"{runName}_g0.json")
burst_output_json_path = os.path.join(burst_detector_path, "json_files", f"{runName}_g0-output.json")
catgt_folder = os.path.join(catGT_dest, f"catgt_{runName}_g0")
imec_folder = os.path.join(catgt_folder, f"{runName}_g0_imec0")
ks_folder = os.path.join(imec_folder, "imec0_ks2")
burst_dir = {
    "data_filepath": os.path.join(imec_folder, f"{runName}_g0_tcat.imec0.ap.bin"),
    "KS_folder": ks_folder
}
with open(burst_input_json_path, "w+") as f:
    json.dump(burst_dir, f)

# create bash file
run_helper = os.path.join(clt_folder, "run.sh")

with open(run_helper, 'w+') as f:
    f.write(f'''\
#! /bin/bash
set -e
eval "$(conda shell.bash hook)"
echo "(base) conda activate {ecephys_env}"
conda activate {ecephys_env}
echo '({ecephys_env}) pip install "{clt_head_folder}"'
pip install "{clt_head_folder}"
echo '({ecephys_env}) python "{sglx_file}"'
python "{sglx_file}"
echo "({ecephys_env}) conda activate {burst_env}"
conda activate {burst_env}
echo '({burst_env}) python "{plot_units}" --input "{burst_input_json_path}" --output "{burst_output_json_path}"'
python "{plot_units}" --input "{burst_input_json_path}" --output "{burst_output_json_path}"
echo "({burst_env}) conda activate {ecephys_env}"
conda activate {ecephys_env}
echo '({ecephys_env}) python -m ecephys_spike_sorting.modules.quality_metrics --input "{quality_input_json}" --output "{quality_output_json}"'
python -m ecephys_spike_sorting.modules.quality_metrics --input "{quality_input_json}" --output "{quality_output_json}"
echo "({ecephys_env}) conda activate {burst_env}"
conda activate {burst_env}
echo '({burst_env}) python "{custom_metrics}"'
python "{custom_metrics}"
echo '({burst_env}) cd "{ks_folder}"'
cd "{ks_folder}"
echo '({burst_env}) conda activate {phy_env}'
conda activate {phy_env}
echo '({phy_env}) phy template-gui params.py'
phy template-gui params.py
''')

