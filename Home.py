import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

# 側欄內容
st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("選擇底圖來探索地圖功能。")

# 標題
title = """
<div style="text-align: center; font-size: 32px; font-weight: bold; color: green; background-color: #e9ffc2;">
    柚子的家（基本底圖）
</div>
"""
st.markdown(title, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

markdown = """
<div style="text-align: center; font-size: 18px;">
    歡迎來到柚子的家，在您眼前的是基本底圖，功能在左下角，請慢慢享用。
</div>
"""
st.markdown(markdown, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

# 中心點設在南投埔里
center_lat, center_lon = 23.5825, 120.5855

# 指定要顯示的底圖及其翻譯名稱
basemap_translations = {
    "SATELLITE": "衛星圖",
    "ROADMAP": "道路圖",
    "TERRAIN": "地形圖",
    "OpenStreetMap": "開放街圖",
    "HYBRID": "混合圖"
}

# 提取底圖關鍵字
selected_basemaps = list(basemap_translations.keys())
translated_names = [basemap_translations[bm] for bm in selected_basemaps]

# 介面選擇底圖（顯示翻譯名稱）
selected_translated = st.sidebar.selectbox("請選擇底圖：", translated_names)

# 回應原始底圖名稱
selected_basemap = selected_basemaps[translated_names.index(selected_translated)]

# 顯示小地圖的選項
show_minimap = st.sidebar.checkbox("顯示小地圖", value=True)

# 建立地圖並應用所選底圖
map = leafmap.Map(center=[center_lat, center_lon], zoom=8, latlon_control=True, draw_export=True, minimap_control=show_minimap)
map.add_basemap(selected_basemap)

map.to_streamlit(height=720)

