import numpy as np
import os
import sys

sys.path.append("../src")
import localmodule


# Define constants.
aug_kinds = ["all", "all-but-noise", "none"]
units = localmodule.get_units()
script_name = "058_evaluate-pcen-addntt-convnet-full-audio.py"
script_path = os.path.join("..", "..", "..", "src", script_name)
dataset_name = localmodule.get_dataset_name()
n_trials = 10


# Create folder.
script_dir = script_name[:-3]
os.makedirs(script_dir, exist_ok=True)
sbatch_dir = os.path.join(script_dir, "sbatch")
os.makedirs(sbatch_dir, exist_ok=True)
slurm_dir = os.path.join(script_dir, "slurm")
os.makedirs(slurm_dir, exist_ok=True)


for aug_kind_str in aug_kinds:
    file_path = os.path.join(sbatch_dir, "058_aug-" + aug_kind_str + ".sh")

    # Open shell file
    with open(file_path, "w") as f:
        # Print header
        f.write(
            "# This shell script executes Slurm jobs for evaluating\n" +
            "# PCEN NTT convolutional neural network with adaptive threshold\n" +
            "# on " + dataset_name + " full audio.\n")
        f.write("# Augmentation kind: " + aug_kind_str + ".\n")
        f.write("\n")

        # Loop over test units.
        for test_unit_str in units:

            # Loop over trials.
            for trial_id in range(n_trials):

                # Define job name.
                job_name = "_".join([
                    script_name[:3],
                    "aug-" + aug_kind_str,
                    "test-" + test_unit_str,
                    "trial-" + str(trial_id)])
                sbatch_str = "sbatch " + job_name + ".sbatch"
                f.write(sbatch_str + "\n")
            f.write("\n")


    # Grant permission to execute the shell file.
    # https://stackoverflow.com/a/30463972
    mode = os.stat(file_path).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(file_path, mode)
