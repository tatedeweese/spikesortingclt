from parameters import *
import os
import json

def modules_line(mod_value):
    mod_str = "modules = ["
    modules = ["kilosort_helper", "kilosort_postprocessing", "noise_templates", "mean_waveforms", "quality_metrics", "psth_events"]
    for mod in modules:
        pre = "" if mod in mod_value else "# "
        mod_str += f"\n\t{pre}\'{mod}\',"
    mod_str = mod_str[:-1]
    mod_str += "\n]\n"
    return mod_str

def run_line(run_value):
    run_str = "run_specs = ["
    for run in run_value:
        run_str += f"\n\t{run},"
    run_str = run_str[:-1]
    run_str += "\n]\n"
    return run_str

def update_sglx_file(sglx_file):
    params = ["logName", "npx_directory", "run_specs", "run_CatGT", "process_lf", "catGT_cmd_string", "ni_present", "ni_extract_string", "runTPrime", "modules", "json_directory"]
    with open(sglx_file, "r") as in_f:
        with open(sglx_file + '.tmp', 'w+') as out_f:
            line = in_f.readline()
            while line:
                newline = line
                key = newline.split(' ', 1)[0]
                if key in params:
                    value = globals()[key]
                    if key in ["npx_directory", "json_directory"]: # directory
                        newline = f"{key} = r\'{value}\'\n"
                    elif key in ["run_specs", "modules"]: # possibly multiline
                        open_brackets = line.count("[")
                        closed_brackets = line.count("]")
                        while open_brackets > closed_brackets:
                            line = in_f.readline()
                            open_brackets += line.count("[")
                            closed_brackets += line.count("]")
                        newline = run_line(value) if key == "run_specs" else modules_line(value)
                    else:
                        if type(value) == str:
                            newline = f"{key} = \'{value}\'\n"
                        else:
                            newline = f"{key} = {value}\n"
                line = in_f.readline()
                out_f.write(newline)
    os.replace(sglx_file + '.tmp', sglx_file)

def create_burst_json(filepath, imec_folder, ks_folder):
    data_filepath = os.path.join(imec_folder, f"{runName}_g0_tcat.imec0.ap.bin")
    burst_dir = {
        "data_filepath": data_filepath.replace('\\', '/'),
        "KS_folder": ks_folder.replace('\\', '/')
    }
    with open(filepath, "w+") as f:
        json.dump(burst_dir, f, indent=4)

def generate_bash(sglx_file, burst_input_json_path, burst_output_json_path, quality_input_json, quality_output_json, ks_folder):
    plot_units_file = os.path.join(burst_detector_path, "burst_detector", "plot_units.py")
    custom_metrics_file = os.path.join(burst_detector_path, "burst_detector", "custom_metrics.py")
    clt_folder = os.path.dirname(os.path.realpath(__file__))
    run_helper = os.path.join(clt_folder, "run.sh")
    env = "base"
    bash_str = """\
#! /bin/bash
set -e
eval "$(conda shell.bash hook)"
"""

    if run_pipeline:
        bash_str += f"""\
echo "({env}) conda activate {ecephys_env}"
conda activate {ecephys_env}
echo '({ecephys_env}) python "{sglx_file}"'
python "{sglx_file}"
"""
        env = ecephys_env

    if plot_units:
        bash_str += f"""\
echo "({env}) conda activate {burst_env}"
conda activate {burst_env}
echo '({burst_env}) python "{plot_units_file}" --input "{burst_input_json_path}" --output "{burst_output_json_path}"'
python "{plot_units_file}" --input "{burst_input_json_path}" --output "{burst_output_json_path}"
"""
        env = burst_env

    if quality_metrics:
        bash_str += f"""\
echo "({env}) conda activate {ecephys_env}"
conda activate {ecephys_env}
echo '({ecephys_env}) python -m ecephys_spike_sorting.modules.quality_metrics --input "{quality_input_json}" --output "{quality_output_json}"'
python -m ecephys_spike_sorting.modules.quality_metrics --input "{quality_input_json}" --output "{quality_output_json}"
"""
        env = ecephys_env

    if custom_metrics:
        bash_str += f"""\
echo "({env}) conda activate {burst_env}"
conda activate {burst_env}
echo '({burst_env}) python "{custom_metrics_file}"'
python "{custom_metrics_file}"
"""
        env = burst_env
    
    if phy:
        bash_str += f"""\
echo '({env}) cd "{ks_folder}"'
cd "{ks_folder}"
echo '({env}) conda activate {phy_env}'
conda activate {phy_env}
echo '({phy_env}) phy template-gui params.py'
phy template-gui params.py
"""
    with open(run_helper, 'w+') as f:
        f.write(bash_str)

def main():
    # ecephys: sglx_multi_run_pipeline.py
    os.makedirs(json_directory, exist_ok=True)
    scripts_folder = os.path.join(ecephys_directory, "scripts")
    sglx_file = os.path.join(scripts_folder, "sglx_multi_run_pipeline.py")

    # update file parameters
    update_sglx_file(sglx_file)

    # create json
    burst_input_json_path = os.path.join(burst_detector_path, "json_files", f"{runName}_g0.json")
    burst_output_json_path = os.path.join(burst_detector_path, "json_files", f"{runName}_g0-output.json")
    catgt_folder = os.path.join(npx_directory, f"{runName}_g0", f"catgt_{runName}_g0")
    imec_folder = os.path.join(catgt_folder, f"{runName}_g0_imec0")
    ks_folder = os.path.join(imec_folder, "imec0_ks2")
    create_burst_json(burst_input_json_path, imec_folder, ks_folder)

    # ecephys: quality_metrics
    quality_input_json = os.path.join(json_directory, f"{runName}_imec0-input.json")
    quality_output_json = os.path.join(json_directory, f"{runName}_imec0-output.json")
 
    generate_bash(sglx_file, burst_input_json_path, burst_output_json_path, quality_input_json, quality_output_json, ks_folder)
        
if __name__ == "__main__":
    main()


