# Installation of Python environment

We will use the Python environment [gds_env](https://darribas.org/gds_env/) throughout the course.

* Reserve at least 4 GB of free space on your laptop
* Download the installation files
* Follow these instructions: [Docker - Install | gds_env (darribas.org)](https://darribas.org/gds_env/guides/docker_install/) (you only need the gds_py for this course)
* Once the installations are complete, follow the guide for running the Docker container and run Jupyter in your browser
* Run the notebook test_gdspy_install.ipynb from the installation files to check that everything works
* If you have older versions of Windows, Docker might not work. In that case, try the guide using VirtualBox: Virtualbox - Install | gds_env (darribas.org)

If neither Docker nor VirtualBox works - try creating a conda environment with the required libraries:

**This is slow and only recommended as a last resort.**

* Navigate to the folder installation_files
* Run conda env create -f gds_py.yml
* Activate the environment
* Run pip install -r pip_requirements.txt
* Run the notebook test_gdspy_install.ipynb to check that everything works

*For OneDrive users: Please note that you usually need to navigate to your OneDrive-folder before running JupyterLab to access the files in OneDrive.
