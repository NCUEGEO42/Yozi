import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)

st.title("互動式地圖-縣市人口(2024.12.2 V.1)")

with st.expander("顯示程式碼"):
    with st.echo():

        map = leafmap.Map(center=[23.5825, 120.5855], zoom=8)
        regions = 'https://github.com/NCUEGEO42/My-Tiff/raw/refs/heads/main/Population.shp'
        map.add_shp(regions, layer_name='縣市人口地圖')
        
map.to_streamlit(height=720)
