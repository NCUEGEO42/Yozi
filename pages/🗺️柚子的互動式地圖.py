import streamlit as st
import leafmap.foliumap as leafmap

# 側欄內容
st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("選擇底圖來探索地圖功能。")

# 顯示主標題
st.title("柚子的互動式地圖")

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
col1, col2 = st.columns([1, 1])  # 定義兩欄布局
with col1:
    m = leafmap.Map(latlon_control=True, draw_export=True, minimap_control=show_minimap)
    m.add_basemap(selected_basemap)
    m.to_streamlit(height=960)
