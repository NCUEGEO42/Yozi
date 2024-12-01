import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(
    page_title="柚子的作業", #網頁名稱
    page_icon="🍐", #網頁icon
    layout="wide", #內容顯示在頁面中央
    initial_sidebar_state="collapsed" #側邊欄預設收起
)

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("關於") #側欄標題名稱
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True) #側欄文字背景顏色
#預設情況下，Streamlit 禁止 HTML，需設定 unsafe_allow_html=True 來啟用 HTML 標籤。

title = """
<div style="text-align: center; font-size: 32px; font-weight: bold; color: green; background-color: #e9ffc2;">
    您好，歡迎來到「柚子的作業」官網。
</div>
"""
st.markdown(title, unsafe_allow_html=True)
#Streamlit的st.header不支援內建文字置中，因此必須改用title。

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

markdown = """
<div style="text-align: center; font-size: 18px;">
    在這邊，我們為您準備了精美的作業。請您慢慢享用。
</div>
"""

st.markdown(markdown, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

map = leafmap.Map(minimap_control=True)
map.add_basemap("SATELLITE")
map.to_streamlit(height=720)
