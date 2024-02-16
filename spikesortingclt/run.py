
from parameters import *
import sys
sys.path.append(os.path.join(ecephys_directory, "scripts")) # to avoid module not found errors with sglx_multi_run_pipeline import
from ecephys_spike_sorting.scripts.sglx_multi_run_pipeline import npx_directory, run_specs, json_directory
import os
import json
import subprocess

conda_prompt_path = os.path.join(sys.exec_prefix, "Scripts", "activate.bat") # this is dependent on environment I python run this in

def create_burst_json(filepath, imec_folder, ks_folder, run_str, prb):
    data_filepath = os.path.join(imec_folder, f"{run_str}_tcat.imec{prb}.ap.bin")
    burst_dir = {
        "data_filepath": data_filepath.replace('\\', '/'),
        "KS_folder": ks_folder.replace('\\', '/')
    }
    with open(filepath, "w+") as f:
        json.dump(burst_dir, f, indent=4)

def execute(cmd, conda=True):
    if conda:
        cmd = f"call {conda_prompt_path} && {cmd}"
    with subprocess.Popen(cmd.split(), shell=True, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) as popen:
        for stdout_line in popen.stdout:
            print(stdout_line, end="")
    if popen.returncode != 0:
        print(f"Error: {popen.stderr.read()}")
        raise subprocess.CalledProcessError(popen.returncode, popen.args)

def run_subprocesses(burst_input_json_path, burst_output_json_path, quality_input_json, quality_output_json, ks_folder):
    sglx_file = os.path.join(ecephys_directory, "scripts", "sglx_multi_run_pipeline.py")
    plot_units_file = os.path.join(burst_detector_path, "burst_detector", "plot_units.py")
    custom_metrics_file = os.path.join(burst_detector_path, "burst_detector", "custom_metrics.py")
    phy_file = os.path.join(ks_folder, "params.py")
    if run_pipeline:
        print("~~~RUNNING SGLX_MULTI_RUN_PIPELINE~~~")
        conda_cmd = f"conda activate {ecephys_env}"
        python_cmd = f"python {sglx_file}"
        print(conda_cmd)
        print(python_cmd)
        execute(f"{conda_cmd} && {python_cmd}")
    if plot_units:
        print("~~~RUNNING PLOT_UNITS~~~")
        conda_cmd = f"conda activate {burst_env}"
        python_cmd = f"python {plot_units_file} --input {burst_input_json_path} --output {burst_output_json_path}"
        print(conda_cmd)
        print(python_cmd)
        execute(f"{conda_cmd} && {python_cmd}")
    if quality_metrics:
        print("~~~RUNNING QUALITY_METRICS~~~")
        conda_cmd = f"conda activate {ecephys_env}"
        python_cmd = f"python -m ecephys_spike_sorting.modules.quality_metrics --input {quality_input_json} --output {quality_output_json}"
        print(conda_cmd)
        print(python_cmd)
        execute(f"{conda_cmd} && {python_cmd}")
    if custom_metrics:
        print("~~~RUNNING CUSTOM_METRICS~~~")
        conda_cmd = f"conda activate {burst_env}"
        python_cmd = f"python {custom_metrics_file}"
        print(conda_cmd)
        print(python_cmd)
        execute(f"{conda_cmd} && {python_cmd}")
    if phy:
        print("~~~RUNNING PHY~~~")
        conda_cmd = f"conda activate {phy_env}"
        phy_cmd = f"phy template-gui {phy_file}"
        print(conda_cmd)
        print(phy_cmd)
        execute(f"{conda_cmd} && {phy_cmd}")
    
def main():
    prb = 0
    gate = 0
    runName = run_specs[0][0]
    run_str = f"{runName}_g{gate}"
    prb_str = f"{run_str}_imec{prb}"
    catgt_folder = os.path.join(npx_directory, run_str, f"catgt_{run_str}")

    # create json
    burst_input_json_path = os.path.join(burst_detector_path, "json_files", f"{run_str}.json")    
    burst_output_json_path = os.path.join(burst_detector_path, "json_files", f"{run_str}-output.json")
    imec_folder = os.path.join(catgt_folder, prb_str)
    ks_folder = os.path.join(imec_folder, f"imec{prb}_ks2")
    create_burst_json(burst_input_json_path, imec_folder, ks_folder, run_str, prb)

    # ecephys: quality_metrics
    quality_input_json = os.path.join(json_directory, f"{runName}_imec{prb}-input.json")
    quality_output_json = os.path.join(json_directory, f"{runName}_imec{prb}-output.json")
 
    run_subprocesses(burst_input_json_path, burst_output_json_path, quality_input_json, quality_output_json, ks_folder)

    
if __name__ == "__main__":
    main()


