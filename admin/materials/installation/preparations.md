# Installation instructions for Geospatial Data Science

## 1. Install Pixi on your machine

Follow the installation guideline
at: <https://pixi.prefix.dev/latest/installation/>  
Pixi is a package management tool like conda, but *much* faster.

## 2. Create Pixi workspace and environment for the course

Navigate to whatever directory you want to use for the course. Place the [`gds_py.yml`](gds_py.yml)
file there. Open a terminal window in that directory and execute `pixi init \--import gds_py.yml`. This sets up a Pixi workspace and environment in that directory, with all the dependencies that you need for the course.

## 3. Install dependencies and start Jupyter Lab

In the same terminal window, execute `pixi run jupyter lab`. The first time you do this, it may take several minutes, since Pixi has to install all the dependencies. After Pixi is finished, an instance of Jupyter lab is automatically going to open in your browser. 

Pixi will place a `pixi.lock` and a `pixi.toml` file in that folder. Keep those files, as they will allow you to restart the environment fast next time you need it, via `pixi run jupyter lab`.

If you prefer to use an IDE, rather than Jupyter Lab, please find documentation how to connect your IDE to the Pixi environment here:  
VSCode: <https://pixi.prefix.dev/latest/integration/editor/vscode/>  
PyCharm: <https://pixi.prefix.dev/latest/integration/editor/jetbrains/>

## 4. Test requirements

Try to run all of the
[`test_gdspy_install.ipynb`](test_gdspy_install.ipynb)
notebook. There could be a bunch of warnings thrown, for example in red cells, but as long as you arrive at the last cell without interruption you are good to go!

## 5. Issues?

We are sorry to hear. Our TA will use the first exercise to help with installations: Jan 28th from 12:20 in room 4A58. If you have any issues left *after* that session, please contact our TA to get it resolved.
