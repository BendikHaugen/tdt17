#!/bin/bash
#SBATCH --job-name="yoloV7 road damage detection"   # Sensible name for the job
#SBATCH --account=bendihh   # Account for consumed resources
#SBATCH --nodes=1            # Allocate 1 nodes for the job
#SBATCH -c28                  # Number of cores (can vary)
#SBATCH --time=00-15:30:00    # Upper time limit for the job (DD-HH:MM:SS)
#SBATCH --partition=CPUQ
#SBATCH --mail-user=Bendik_haugen@hotmail.com
#SBATCH --mail-type=ALL


ipython -c "run yolov7training.ipynb"

