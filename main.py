import requests
import streamlit as st
input_dish = st.text_input("Enter Dish name that's you want to know about their nutritions:")
clickbutton = st.button("Check")
if clickbutton:
	url = "https://dietagram.p.rapidapi.com/apiFood.php"

	querystring = {"name":input_dish,"lang":"pl"}

	headers = {
		"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
		"X-RapidAPI-Host": "dietagram.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)
	var1 = response.json()
	# final1 = var1["dishes"][2]["caloric"]
	# final2 = var1["dishes"][6]["protein"]
	# final3 = var1["dishes"][5]["carbon"]
	# print(final1)
	# print(final2)
	# print(final3)
	st.info("Calories")
	st.info(final1)
	st.info("Proteins")
	st.info(final2)
	st.info("Carbs")
	st.info(final3)