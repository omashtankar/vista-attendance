from pathlib import Path

import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home



def home_screen():


    style_background_home()
    style_base_layout()



    header_home()

    # For making Background box behind teacher-teacher_img-teacher_login
    c1, c2 =st.columns(2)
    with c1:

        st.header('Student')
        st.image(Path(__file__).resolve().parent.parent / "images" / "student1.png", width=900)
        if st.button('Student Registration', type='secondary'):
            st.session_state['login_type']='student'
            st.rerun()

    with c2:

        st.header('Teacher')
        st.image(Path(__file__).resolve().parent.parent / "images" / "teacher.png", width=200)
        if st.button('Teacher Registration', type='secondary'):
            st.session_state['login_type']='teacher'
            st.rerun()

