from pathlib import Path

import streamlit as st

def header_home():
    
    st.markdown("""
                <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
                <h1 style="text-align:center; color:#80A8FF;margin-top:0px;padding:0px;;">ATTENDANCE SYSTEM</h1>
                <div>   
                """,unsafe_allow_html=True)


def header_dashboard():

    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        st.image(Path(__file__).resolve().parent.parent / "images" / "VISTA.svg", width=100)

    with c2:
        if c2.button("Go back Home", width="stretch", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()
        

