# This shell script executes Slurm jobs for training
# NTT convolutional neural network
# on BirdVox-70k.
# Trial ID: 0.
# Augmentation kind: all-but-noise.

sbatch 035_aug-all-but-noise_unit01_trial-0.sbatch
sbatch 035_aug-all-but-noise_unit02_trial-0.sbatch
sbatch 035_aug-all-but-noise_unit03_trial-0.sbatch
sbatch 035_aug-all-but-noise_unit05_trial-0.sbatch
sbatch 035_aug-all-but-noise_unit07_trial-0.sbatch
sbatch 035_aug-all-but-noise_unit10_trial-0.sbatch
