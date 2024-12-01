import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

with col2:

    basemap = st.selectbox("選擇您的基本底圖：", options, index)


with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    m.add_basemap(basemap)
    m.to_streamlit(height=720)
