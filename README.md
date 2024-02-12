# spikesortingclt

### Initial Setup
1. cd into spikesortingclt and install the python package into conda base environment
   ```bash 
   conda activate base
   pip install .
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

### Errors
* If sglx_run_multi_pipeline.py cannot find your meta file, you may have to change permissions of your data folder. For example if the data lies in the D: Drive try running the code below
  ```bash
  chmod 777 D:/
  ```
