# PatientReviewer

A package for using and creating interactive dashboards for reviewing integrated Patient data interactively.

Demo: Coming soon!

# Install

## Activate or Set up Conda Environment

This is **_highly_** recommended to manage different dependencies required by different reviewers.

See [Set up Conda Environment](https://github.com/getzlab/JupyterReviewer/blob/master/README.md#set-up-conda-environment) for details on how to download conda and configure an environment.
    
## Install PatientReviewer

Clone
```
git clone git@github.com:getzlab/PatientReviewer.git

# or in an existing repo
git submodule add git@github.com:getzlab/PatientReviewer.git
```

Install
```
cd PatientReviewer
conda activate <your_env>
pip install -e .
```

# Basic usage

See [UserPatientReviewer.ipynb](https://github.com/getzlab/PatientReviewer/tree/master/example_notebooks/UserPatientReviewer.ipynb) for basic examples and demos of the patient reviewers.

See `PatientReviewer/Reviewers` to see available pre-built reviewer options.

See `PatientReviewer/DataTypes` to see pre-built data configurations for patient review.


# Custom and advanced usage

See `PatientReviewer/AppComponents` for pre-built components and their customizable parameters, and additional utility functions. 

For customizing annotations, adding new components, and other features, see [Intro_to_Reviewers.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Intro_to_Reviewers.ipynb).

For creating your own prebuilt reviewer, see [Developer_Jupyter_Reviewer_Tutorial.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Developer_Jupyter_Reviewer_Tutorial.ipynb).
