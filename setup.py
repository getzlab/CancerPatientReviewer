import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PatientReviewer",
    version="0.0.2",
    author="Conor Messer",
    author_email="cmesser@broadinstitute.org",
    description="A tool to view integrated patient data using JupyterReviewer Plotly dashboard",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/getzlab/PatientReviewer",
    project_urls={
        "Bug Tracker": "https://github.com/getzlab/PatientReviewer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires = ['JupyterReviewer==0.0.7',
                        'firecloud-dalmatian',
                        'pyyaml']
)   

