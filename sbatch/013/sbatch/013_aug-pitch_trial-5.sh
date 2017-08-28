# This shell script executes Slurm jobs for training
# Justin Salamon's ICASSP 2017 convolutional neural network
# on BirdVox-70k.
# Trial ID: 5.
# Augmentation kind: pitch.

sbatch 013_aug-pitch_unit01_trial-5.sbatch
sbatch 013_aug-pitch_unit02_trial-5.sbatch
sbatch 013_aug-pitch_unit03_trial-5.sbatch
sbatch 013_aug-pitch_unit05_trial-5.sbatch
sbatch 013_aug-pitch_unit07_trial-5.sbatch
sbatch 013_aug-pitch_unit10_trial-5.sbatch