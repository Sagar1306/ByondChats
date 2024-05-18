import streamlit as st
import requests
import json 
import re

url = requests. get(' https://devapi.beyondchats.com/api/get_message_with_sources')
File = json.loads(url.text)


Main=File['data']['data']
All_responses=[Main[response]['response'] for response in range(len(Main)) ]


# Streamlit's selectbox for user to choose a response
option = st.selectbox('Navigate through The responses ',
   (All_responses),
   index=0, 
   placeholder="Select Your Reponse")

# selecting the index of particular response
response = All_responses.index(option)

Citations=[] #Preparations for citations for a particular response

for contexts in range(len(Main[response]['source'])):
    Temp_id = Main[response]['source'][contexts]['id']
    Temp_link = Main[response]['source'][contexts]['link']
    Temp_context = Main[response]['source'][contexts]['context']
    
    if not Temp_link:
        # Finding link in context if link is empty
        link = re.findall(r'https?://\S+', Temp_context)
        if link: 
            # If you want multiple links for same Id you can set link[0] to link
            Citations.append({"id": Temp_id, "link": link[0]}) 
    else:
        Citations.append({"id": Temp_id, "link": Temp_link})

#Displaying the Final Citation
st.write('Citations :', Citations)


