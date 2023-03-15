'''
Script to complete a basic run of the model and display a table of
results.

The model is imported from a pypi package 'treat_sim'

Full documentation and source code for `treat_sim` is available as 
* Jupyter Book: https://tommonks.github.io/treatment-centre-sim/
* github: https://github.com/TomMonks/treatment-centre-sim

A conda environment has been provided locally, but the model can be pip installed
`pip install treat_sim==0.1.0`

This will be adapted into a basic streamlit app
'''
from treat_sim.model import Scenario, multiple_replications
import streamlit as st
import glob
import os

INTRO_FILE = 'resources/overview.md'

def read_file_contents(file_name):
    ''''
    Read the contents of a file.

    Params:
    ------
    file_name: str
        Path to file.

    Returns:
    -------
    str
    '''
    with open(file_name) as f:
        return f.read()

# give the page a title
st.title('Treatment Centre Simulation Model')

# show the introductory markdown
st.markdown(read_file_contents(INTRO_FILE))

# set the variables for the run.
# these are just a subset of the total available for this example...
triage_bays = 1
exam_rooms = 3
treat_rooms = 1

# examination mean
exam_mean = 16.0

# runs
replications = 10

# Setup scenario using supplied variables
args = Scenario()
args.n_triage = triage_bays
args.n_exam = exam_rooms
args.n_cubicles_1 = treat_rooms
args.exam_mean = exam_mean

# in this example run a single replication of the model.
results = multiple_replications(args, n_reps=replications)

print(results.mean().round(1))

