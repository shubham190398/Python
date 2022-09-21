# Braille Detection
## Setting up:
1. Download and install Anaconda
2. Open cmd.exe prompt in Conda and navigate to your desired work directory where the models and data is stored.
3. In the command prompt, create a new environment from the environment.yml file using the command `conda env create -f environment.yml`
4. See if the environment has been installed correctly with `conda env list`. You should have an environment called Yoloenv in it.

## Running the code:
1. Activate Yoloenv with `conda activate Yoloenv` or whatever the environment path is stored as according to `conda env list`.
2. Use command `jupyter notebook` to open Jupyter notebook in the current directory.
3. Open the Braille Detection notebook and run the first cell for setting up the functions. Run the second cell with your desired arguments to test.

## Data Collection:
1. If you are using mode 2, ensure that the finger is detectable at all points of the video. Make sure that the tip of the finger can be seen at all times.
2. If you use mode 3, ensure that the finger is detectable for the first second (it essentially needs the first frame). In this mode you have to ensure that the relative position of the finger and the camera is roughly the same throughout the video.
3. Ensure that the characters aren't blurred. The model was trained in adequate ambient lighting with a phone flash and a torch providing the local lighting for the shadows instead of the provided LED due to the dispersed light. Any light source should work as long as it is focused and the dots are clearly distinguishable from the background.
