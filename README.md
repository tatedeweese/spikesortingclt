# spikesortingclt

### Initial Setup
1. Add the following code to the top of create_input_json.py and comment out the definition of those variables in the code.
   ```python 
   from spikesortingclt.parameters import ecephys_directory, kilosort_repository, KS2ver, npy_matlab_repository, catGTPath, tPrime_path, cWaves_path
   ```
1. Add the following code to the top of sglx_multi_run_pipeline.py and comment out the definition of those variables in the code
   ```python 
   from spikesortingclt.parameters import logName, npx_directory, run_specs, catGT_dest, run_CatGT, runTPrime, modules, json_directory
   ```

### Each Curation
1. Update parameters.py
1. Run in terminal. Note: works in base probably because of `eval "$(conda shell.bash hook)"` line
   ```bash
   conda activate base
   cd spikesortingclt
   python create_bash.py
   bash run.sh
   ```
