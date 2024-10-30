import streamlit as st
import base64
import os

import uuid
from datetime import datetime



@st.cache_data
def getBase64Image(path:str):
    with open(path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def displayInstructions(session):
   showExpand:bool = False
   if "expand" not in session:
        showExpand =True

   st.markdown(
        """
        <style>
        .streamlit-expanderHeader p {
            font-size: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
   with st.expander("Welcome to EstateSmart!", expanded=showExpand):
        st.markdown("""<p style="font-size:16px;color:black;margin-bottom:0.01px;">
                    This is a simple chatbot that uses a mock LLM model to generate responses.
                    """,unsafe_allow_html=True)
        st.markdown("""
            <p style="font-size:16px;margin-top:0rem;margin-bottom:0.05rem;color:black">
                    Examples of questions this chatbot can help you answer:
            <ul>
                <li style="font-size:16px;color:black"><b>Tell me</b> Give me details about client Daniel Johnson?</li>
                <li style="font-size:16px;color:black"><b>Tell me</b> Give me details about client Layla Brown?</li>                
            </ul>

        """,unsafe_allow_html=True)
    
def writeStyles():
    #st.write(st_theme)    
    st.markdown(
        """
        <style>
            [data-testid="stHeader"]{
                height:80px;
                border-bottom: 2px solid;
                background:black;
                color:white;
                z-index:1;
            }
            [data-testid="stDecoration"]{
                background-image: url("data:image/png;base64,"""+getBase64Image(os.path.join( os.path.dirname(__file__),'img','logo_buildings.png'))+"""");
                background-size:cover;
                background-position: center;
                height:50px;
                width:200px;
                margin:10px;
            }
            .stChatMessage{
             border:none;
             background:none
            }
            [data-testid="chatAvatarIcon-user"]{
                background-color: #6E62D3;
            }
            [data-testid="chatAvatarIcon-assistant"]{
                background-color: #30EA03;
            }
            .stChatInputContainer
            {
                background:none;
            }
           
            button[kind="primary"],button[kind="primary"]:hover
            {
                color: black;
                background-color: #30EA03;
                margin-top: 20px;
                width: 200px;
                font-family: verdana;
                border-color:black
            }
            details
            {
                background:#f0f2f6;
                border:none !important;
            }
            #sticky-bottom {
                position: sticky;
                bottom: 0;
            }
            button[data-testid="baseButton-secondary"]
            {
                width :200px;
                font-family: verdana;
                text-align:left
            }
            button[data-testid="baseButton-secondary"]:hover
            {
            
                background-color: #30EA03;
                border:1px solid;
                color:black
            }
            [data-testid="stSidebar"]
           {
                 width: 250px !important; # Set the width to your desired value                
            }
            section[data-testid="stSidebar"]
            {
               
                top:80px;
                overflow:scroll;
            }
            button[kind="header"],[data-testid="collapsedControl"]{
               display:none;
            }
            [data-testid="stSidebarUserContent"]
            {
                padding:1rem;
            }
            summary p{
                font-weight:bold;
                font-size:20px;
            }
            hr{
                    border-top : 1px dotted;
                    margin:0;
            }
             [data-testid="stHeader"]::after {
                content: "EstateSmart";
                position: absolute;
                left: 220px;
                top: 5px;
                font-size: 35px;
                font-weight: bold;
            }
            footer
            {
                position:fixed;
                color:red;
                font-size:12px;
                bottom:15px;
                z-index:9999!important
            }
            [data-baseweb="textarea"] {
                border: 1px solid rgba(49, 51, 63, 0.2);
            }
            summary,summary:hover
            {
                color:black !important
            }
            summary p
            {
                 font-size:20px !important;
            }
            .stDeployButton,#MainMenu,div[data-testid="stStatusWidget"], div[data-testid="stToolbar"]
            {
                display:none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

       
       
