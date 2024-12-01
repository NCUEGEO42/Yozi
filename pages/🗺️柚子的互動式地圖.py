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

col1, col2 = st.columns([5, 1])
options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

# 底圖選項命名為中文
# 將底圖選項轉換為中文
translated_options = {
    "SATELLITE": "衛星圖",
    "ROADMAP": "道路圖",
    "HYBRID": "混合圖",
    "TERRAIN": "地形圖",
    "FWS NWI Wetlands": "美國濕地圖",
    "FWS NWI Wetlands Raster": "美國濕地圖(網格)",
    "NLCD 2021 CONUS Land Cover": "美國2021年土地覆蓋圖",
    "NLCD 2019 CONUS Land Cover": "美國2019年土地覆蓋圖",
    "NLCD 2016 CONUS Land Cover": "美國2016年土地覆蓋圖",
    "NLCD 2013 CONUS Land Cover": "美國2013年土地覆蓋圖",
    "NLCD 2011 CONUS Land Cover": "美國2011年土地覆蓋圖",
    "NLCD 2008 CONUS Land Cover": "美國2008年土地覆蓋圖",
    "NLCD 2006 CONUS Land Cover": "美國2006年土地覆蓋圖",
    "NLCD 2004 CONUS Land Cover": "美國2004年土地覆蓋圖",
}
translated_keys = [translated_options.get(opt, opt) for opt in options]

with col2:

    basemap = st.selectbox("選擇您的基本底圖：", options, index)


with col1:

    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    m.add_basemap(basemap)
    m.to_streamlit(height=720)
