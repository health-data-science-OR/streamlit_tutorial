[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100+/)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19003074.svg)](https://doi.org/10.5281/zenodo.19003074)

# Streamlit Live Coding Tutorial

A short live tutorial for deploying any predictive or simulation model via streamlit.  

> The tutorial is designed to be done live where the lecturer starts with `main.py` and working through the exercises below demonstrating `streamlit` functionality.

## Dependencies

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend install [mini-conda](https://docs.conda.io/en/latest/miniconda.html); navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

```
conda env create -f binder/environment.yml
```

Activate the conda environment using the following command

```
conda activate deploy_st
```

## Case study model

**This example is based on exercise 13 from Nelson (2013) page 170.**

> *Nelson. B.L. (2013). [Foundations and methods of stochastic simulation](https://www.amazon.co.uk/Foundations-Methods-Stochastic-Simulation-International/dp/1461461596/ref=sr_1_1?dchild=1&keywords=foundations+and+methods+of+stochastic+simulation&qid=1617050801&sr=8-1). Springer.* 

> The model is implemented in the pypi package `treat_sim`. The model code can be found [here](https://github.com/pythonhealthdatascience/stars-treat-sim)

We adapt a textbook example from Nelson (2013): a terminating discrete-event simulation model of a U.S based treatment centre. In the model, patients arrive to the health centre between 6am and 12am following a non-stationary Poisson process. On arrival, all patients sign-in and are triaged into two classes: trauma and non-trauma. Trauma patients include impact injuries, broken bones, strains or cuts etc. Non-trauma include acute sickness, pain, and general feelings of being unwell etc. Trauma patients must first be stabilised in a trauma room. These patients then undergo treatment in a cubicle before being discharged. Non-trauma patients go through registration and examination activities. A proportion of non-trauma patients require treatment in a cubicle before being discharged. The model predicts waiting time and resource utilisation statistics for the treatment centre. The model allows managers to ask question about the physical design and layout of the treatment centre, the order in which patients are seen, the diagnostic equipment needed by patients, and the speed of treatments. For example: “what if we converted a doctors examination room into a room where nurses assess the urgency of the patients needs.”; or “what if the number of patients we treat in the afternoon doubled” 

## Instruction to run the model from the command line

Ensure you are in the `deploy_st` environment. A script to run the model is contained in `main.py`.  From a terminal issue the following command:

```bash
python main.py
```

## Licensing, reuse and citation of materials

The code is MIT licensed. Please feel free to reuse and adapt.  I would be grateful for a fork and a citation.  The repo is deposited at zenodo and be cited as follows:

> Monks, T. (2024). Streamlit Live Coding Tutorial (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.10827816

```bibtex
@software{monks_2024_10827816,
  author       = {Monks, Thomas},
  title        = {Streamlit Live Coding Tutorial},
  month        = mar,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v3.0.0},
  doi          = {10.5281/zenodo.10827815},
  url          = {https://doi.org/10.5281/zenodo.10827815}
}
```

## Exercises 

1. Create a a basic streamlit app with a title and information.

* Create a new file called `my_streamlit_app.py`; copy and paste in the code from main.py
* Begin to convert this into a streamlit app
    * Import `streamlit`
    * Add a streamlit title (e.g. "Treatment Simulation model") 
    * Read in and display the markdown text from `resources/overview.md`
    * Run the app as follows `streamlit run my_streamlit_app.py`

2. Update parameters and run the simulation model via the app

* Convert the hard coded parameter values into streamlit sliders
* Set the script up to that streamlit run the simulation only when a `Run Simulation` button is clicked
* Using `st.table` display the results of the simulation model to a user


3. Add in a side bar that display the sliders to a user

* Create a side bar section in your app and add in the slider.
* Run your model and check it still works

4. Research streamlit pages 

* Read the documentation on streamlit pages. 
* Add in an "about page".
