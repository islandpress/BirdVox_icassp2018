# This shell script executes Slurm jobs for thresholding
# predictions of NTT-like convolutional
# neural network on BirdVox-70k full audio
# with logmelspec input.
# Augmentation kind: none.
# Test unit: unit07.
# Trial ID: 3.

sbatch 042_aug-none_test-unit07_predict-unit07_trial-3.sbatch
sbatch 042_aug-none_test-unit07_predict-unit03_trial-3.sbatch
sbatch 042_aug-none_test-unit07_predict-unit05_trial-3.sbatch
