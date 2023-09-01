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

## Specify data in a config file

Follow the [patient_reviewer_input_template.yaml](https://github.com/getzlab/PatientReviewer/tree/master/example_notebooks/patient_reviewer_input_template.yaml) to format your data

## Pass data in through a jupyter notebook and launch your dashboard

- [UserPatientReviewer.ipynb](https://github.com/getzlab/PatientReviewer/tree/master/example_notebooks/UserPatientReviewer.ipynb): Example notebook showing how to pass in a config file and create custom components 
- [SimulatedDataReviewer.ipynb](https://github.com/getzlab/PatientReviewer/tree/master/example_notebooks/SimulatedDataReviewer.ipynb): Example notebook running the AnnoMate simulated data 

See `PatientReviewer/Reviewers` to see available pre-built reviewer options.

# Custom and advanced usage

For customizing annotations, adding new components, and other features, see [Intro_to_Reviewers.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Intro_to_Reviewers.ipynb).

For creating your own prebuilt reviewer, see [Developer_Jupyter_Reviewer_Tutorial.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Developer_Jupyter_Reviewer_Tutorial.ipynb).
