#! /bin/bash
eval "$(conda shell.bash hook)"
echo "conda activate ece_pyks2"
conda activate ece_pyks2
echo 'python "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\ecephys_spike_sorting\scripts\sglx_multi_run_pipeline.py"'
python "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\ecephys_spike_sorting\scripts\sglx_multi_run_pipeline.py"
echo "conda activate burst-detector"
conda activate burst-detector
echo 'python "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\burst_detector\plot_units.py" --input "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\json_files\012223_INS10_DT3_rec_g0.json" --output "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\json_files\012223_INS10_DT3_rec_g0-output.json"'
python "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\burst_detector\plot_units.py" --input "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\json_files\012223_INS10_DT3_rec_g0.json" --output "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\json_files\012223_INS10_DT3_rec_g0-output.json"
echo "conda activate ece_pyks2"
conda activate ece_pyks2
echo 'python -m ecephys_spike_sorting.modules.quality_metrics --input "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\json_files\012223_INS10_DT3_rec_imec0-input.json" --output "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\json_files\012223_INS10_DT3_rec_imec0-output.json"'
python -m ecephys_spike_sorting.modules.quality_metrics --input "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\json_files\012223_INS10_DT3_rec_imec0-input.json" --output "C:\Users\tdeweese\Documents\SpikeSorting\ecephys_spike_sorting\json_files\012223_INS10_DT3_rec_imec0-output.json"
echo "conda activate burst-detector"
conda activate burst-detector
echo 'python "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\burst_detector\custom_metrics.py"'
python "C:\Users\tdeweese\Documents\SpikeSorting\burst-detector\burst_detector\custom_metrics.py"
echo 'cd "C:\Users\tdeweese\Documents\test-data\012223_INS10_DT3_rec_g0_out\catgt_012223_INS10_DT3_rec_g0\012223_INS10_DT3_rec_g0_imec0\imec0_ks2"'
cd "C:\Users\tdeweese\Documents\test-data\012223_INS10_DT3_rec_g0_out\catgt_012223_INS10_DT3_rec_g0\012223_INS10_DT3_rec_g0_imec0\imec0_ks2"
echo 'conda activate phy2'
conda activate phy2
echo 'phy template-gui params.py'
phy template-gui params.py
