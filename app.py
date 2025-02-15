import streamlit as st
from streamlit_option_menu import option_menu

# files imports
from home.config import config_set
from login.auth import login_st_interface, signup_st_interface, forget_st_interface
from home.home import home
from home.UsageGuide.usage_guide import usage_guide_interface

if "st_config_set" not in st.session_state:
    config_set()
    st.session_state["st_config_set"] = True
    
# Session Management
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

hide_menu ="""
    <style>
    #MainMenu{
        //visibility:hidden;
    }
    //.stAppToolbar{
    //    visibility:hidden;

    //}
    .stToolbarActions{
        visibility:hidden;
        color:red;
    }
    .stStatusWidget{
        visibility:hidden;
    }
    </style>
    """
st.markdown(hide_menu,unsafe_allow_html=True)

# Routing
if st.session_state["logged_in"]:
    home()
else:
    with st.sidebar:
        menu = option_menu(
            menu_title='AI-PrepMaster',
            options=['Login', 'Signup', 'Forget password', 'Usage guide'],
            icons=['person-circle', 'person-add', 'key-fill', 'info-circle-fill','book'],
            menu_icon='list',
            # menu_icon=None,
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if menu == "Signup":
        signup_st_interface()
    elif menu == "Login":
        login_st_interface()
    elif menu == "Forget password":
        forget_st_interface()
    elif menu == "Usage guide":
        st.title("Welcom to Ai-prprMaster")
        # st.subheader("How to use")
        login_time_guide = """    

###     🔐 Sign Up / Login
- **New users**: Click on the **Sign Up** button on the homepage.
  - Enter your **name, email, and password**.
  - Verify your email via the confirmation link sent to your inbox.
  - Once verified, log in with your credentials.
- **Existing users**: Click **Login**, enter your credentials, and proceed.


    
    """
        st.markdown(login_time_guide,unsafe_allow_html=True)     
        usage_guide_interface()