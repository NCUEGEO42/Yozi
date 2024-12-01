import streamlit as st
import leafmap.foliumap as leafmap

st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("選擇底圖來探索地圖功能。")

st.title("Interactive Map")

col1, col2 = st.columns([5, 1])
options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

# 將底圖選項轉換為中文
basemap_translations = {
    "SATELLITE": "衛星圖",
    "ROADMAP": "道路圖",
    "TERRAIN": "地形圖",
    "OpenStreetMap": "開放街圖",
    "HYBRID": "混合圖"
}

# 列出清單並找出關鍵字
selected_basemaps = list(basemap_translations.keys())
translated_keys = [basemap_translations[bm] for bm in selected_basemaps]

# 用戶界面選擇底圖（顯示翻譯名稱）
selected_translated = st.sidebar.selectbox("選擇底圖", translated_keys)

# 回應原始底圖名稱
selected_basemap = selected_basemaps[translated_keys.index(selected_translated)]

with col2:
    selected_basemap = st.selectbox("選擇您的基本底圖：", translated_keys, index)
    basemap = options[translated_keys.index(selected_basemap)]  # 獲取原始鍵值

with col1:
    show_minimap = st.sidebar.checkbox("顯示小地圖", value=True)
    map = leafmap.Map(locate_control=False, latlon_control=True, draw_export=True, minimap_control=show_minimap)
    try:
        map.add_basemap(basemap)
    except KeyError:
        st.error("無法加載所選底圖，請選擇其他底圖。")
    map.to_streamlit(height=720)
