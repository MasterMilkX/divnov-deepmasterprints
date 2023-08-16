### SETUP

1. Unzip the '.zip' files

2. Put the folders in the following Verifinger path:
`Verifinger_[VERSION]\Tutorials\Biometrics\CPP\`

1. The executables in each file should already have been built, but if not, run the following command in each folder
`$ make all`

### CODE DESCRIPTION

`sub_verifinger.py` - Python wrapper to call and extract information about fingerprint matching from the Verifinger framework. Used in the original DeepMasterPrints and Diversity/Novelty MasterPrint experiments.

`utils.py` - Helper code for the `sub_verifinger.py` code

`Verifinger SDK Test.ipynb` - Tests the `sub_verifinger.py`, custom Verifinger framework scripts, and generator networks (broken, since it is missing older versions of verifinger.py wrappers)

