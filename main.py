import streamlit as st

from streamlit_option_menu import option_menu

import statistic_studient, homepage, giaodiendiemdanh

st.set_page_config(
    page_title = "Ứng dụng điểm danh"
)

class MultiApp:
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    # def run():
    #     with st.sidebar:
    #         with st.sidebar:        
    #             app = option_menu(
    #                 menu_title='Side bar',
    #                 options=['Home page','Thong ke','Diem danh'],
    #                 icons=['house-fill','person-circle','trophy-fill'],
    #                 menu_icon='chat-text-fill',
    #                 default_index=1,
    #                 styles={
    #                     "container": {"padding": "5!important","background-color":'black'},
    #         "icon": {"color": "white", "font-size": "23px"}, 
    #         "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    #         "nav-link-selected": {"background-color": "#02ab21"},}
    #             )
    #     if app == "Home page":
    #         homepage.app()
    #     if app == "Thong ke":
    #         statistic_studient.app()
    #     if app == "Diem danh":
    #         giaodiendiemdan.giaodien()
    def run():
        if 'refresh_flag' not in st.session_state:
            st.session_state.refresh_flag = False
        with st.sidebar:
            with st.sidebar:
                app = option_menu(
                    menu_title='Side bar',
                    options=['Trang Chu','Thong ke','Diem danh'],
                    icons=['house-fill','person-circle','trophy-fill'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important","background-color":'black'},
                        "icon": {"color": "white", "font-size": "23px"}, 
                        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                    }
                )
        if st.session_state.refresh_flag:
            # Thực hiện làm mới ứng dụng
            statistic_studient.app()
            st.session_state.refresh_flag = False
        else:
            
            if app == "Trang Chu" :
                homepage.app()
            if app == "Thong ke":
                statistic_studient.app()
            if app == "Diem danh":
                giaodiendiemdanh.giaodien()

        
           
             
          
             
    run()            