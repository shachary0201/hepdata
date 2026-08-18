For quick production, I have shared the YAML files along with the image files for the ADD model.

The images should be provided in both thumbnail and original PNG formats.

The submission.yaml file contains all the input YAML files, including the information for the figures.

For the above file to work, please comment out Lines 27–427 (before Figure 11) and then comment out Line 439 through the end.

This will ensure that there is only one input corresponding to Figure 11, which I have added here.

After changing the folder path in hepdata_SUS23016.py to the location of your YAML and image files, run:

"python3 hepdata_SUS23016.py"

This will create:

"submission_SUS_23_016.tar.gz"

Then run the local HEPData validation:

"hepdata-validate -a submission_SUS_23_016.tar.gz"

If the local validation is successful, upload the .tar.gz file to the HEPData sandbox and submit it.
