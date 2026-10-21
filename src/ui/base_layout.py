import streamlit as st


def style_background_home():
    st.markdown("""
                <style>

                    .stApp {
                            background: #D3D3FF !important;
                            }


                    .stApp div[data-testid="stColumn"]{
                        background-color:#80A8FF!important;
                        padding:2.5rem !important;
                        border-radius: 5rem !important;
                    }
                </style>
                """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
                <style>

                    .stApp {
                                background: #80A8FF !important;
                            }
                
                </style>
                """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""

                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
                    @import url('https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&display=swap');

                    #MainMenu, footer, header{
                        visibility: hidden;
                    }

                    .block-container{
                        padding-top:1.5rem
                    }

                    h1{
                        font-family: 'Archivo Black' !important;
                        font-style: normal !important;
                        font-size: 3.5rem !important;
                        line-height: 1.1 !important;
                        margin-top: 0rem !important;
                        font-weight: 400 !important;
                        color: #80A8FF !important;
                        
                    }
                    h2{
                        font-family: 'Archivo Black' !important;
                        font-style: normal !important;
                        font-size: 2rem !important;
                        line-height: 1.1 !important;
                        margin-top: 0rem !important;
                        font-weight: 400 !important;
                        color: white !important;
                        
                    }
                    h3, h4, p{
                        font-family: 'Figtree' !important;
                        color: black !important;

                    }
                    div.stButton > button{
                        background: #EAF4FF !important;
                        color: #1D49A6 !important;
                        border: 1px solid #BFD9FF !important;
                    } 
                    div.stButton > button[kind="secondary"]{
                        background: #CEB5FF !important;
                        color: #1D49A6 !important;
                        border: 1px solid #BFD9FF !important;
                        border-radius: 1.5rem !important;
                        padding: 10px 20px !important;
                        transition: transform 0.25s ease-in-out !important;
                    }
                    div.stButton > button[kind="tertiary"]{
                            background: pink !important;
                            color: #1D49A6 !important;
                            border: 1px solid #BFD9FF !important;
                    }
                    div.stButton > button:hover{
                        transform: scale(1.05) !important;
                    }



                </style>

        """, unsafe_allow_html=True)