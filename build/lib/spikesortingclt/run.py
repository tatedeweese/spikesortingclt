from parameters import *
import os

# create empty folder npx_directory/run_name_g0_out




burst_detector_json_path = os.path.join(burst_detector_path, "json_files", f"{runName}_g0")
catgt_folder = os.path.join(catGT_dest, f"catgt_{runName}_g0")
imec_folder = os.path.join(catgt_folder, f"{runName}_g0_imec0")
ks_folder = os.path.join(imec_folder, "imec0_ks2")
# create json file
burst_dir = {
    "data_filepath": os.path.join(imec_folder, f"{runName}_g0_tcat.imec0.ap.bin"),
    "KS_folder": ks_folder
}

