import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle
# import pyautogui # for reset button: pip install pyautogui

# -- Set page config
apptitle = 'DSSI'
st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")

@st.cache_resource
def load_model():
	with open("https://github.com/scarletpeony/toyapp1/blob/main/modelHeart.pkl", "rb") as f:
		model = pickle.load(f)
	return model
model = load_model()

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache_data()
def prediction(age, currentSmoker, prevalentStroke, prevalentHyp, diabetes, sysBP):
	# Making predictions
	prediction = model.predict([[age, currentSmoker, prevalentStroke, prevalentHyp, diabetes, sysBP]])
	if prediction == 0:
		pred = 'Healthy heart'
	else:
		pred = 'Heart disease'
	return pred


# putting the app related codes in main()
def main():
	# give a title to your app
	st.title('Heart Disease Predictor')

	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A loan application assessment app</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)

	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar

	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	age = st.sidebar.slider('age', 0, 120, 35)
	st.write('age', age)

	currentSmoker = st.sidebar.slider('currentSmoker', 0, 1, 0)
	st.write('currentSmoker', currentSmoker)

	prevalentStroke = st.sidebar.slider('prevalentStroke', 0, 1, 0)
	st.write('prevalentStroke', prevalentStroke)

	prevalentHyp = st.sidebar.slider('prevalentHyp', 0, 1, 0)
	st.write('prevalentHyp', prevalentHyp)

	diabetes = st.sidebar.slider('diabetes', 0, 1, 0)
	st.write('diabetes', diabetes)

	annual_inc = st.sidebar.slider('sysBP', 80, 300, 132)
	st.write('sysBP', sysBP)

	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(age, currentSmoker, prevalentStroke, prevalentHyp, diabetes, sysBP)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
