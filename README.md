# Streamlit Tutorial

A draft tutorial for deploying any model via streamlit.

## Exercises 

These exercises use the conda environment `deploy_st` included in `binder/environment.yml` and the simulation code included in `main.py`

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
