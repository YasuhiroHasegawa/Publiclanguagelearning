import streamlit as st
from st_pages import show_pages_from_config
# ページの設定
st.set_page_config(
page_title="Streamlit勉強会",
page_icon=":computer:",
layout="wide",
initial_sidebar_state="auto",
menu_items={
'Get Help': 'https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config',
'Report a bug': "https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config",
'About': "Streamlitで学習アプリ"
}
)
st.title('日本語学習アプリ')
st.write('Streamlitでアプリを作成')
show_pages_from_config()