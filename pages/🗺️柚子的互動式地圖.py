import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import geopandas as gpd
from folium import Choropleth

st.set_page_config(layout="wide")

st.sidebar.title("關於")
st.sidebar.markdown("""
<div style="background-color: #e9ffc2; padding: 12px; border-radius: 6px;"> 
    <b>關於柚子作業的更多資訊</b>，<br>請點擊右方連結：<a href="https://youtu.be/dQw4w9WgXcQ?feature=shared" target="_blank">點我</a>
</div>
""", unsafe_allow_html=True)

# 標題
title = """
<div style="text-align: center; font-size: 32px; font-weight: bold; color: green; background-color: #e9ffc2;">
    柚子的互動式地圖-人口
</div>
"""
st.markdown(title, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

markdown = """
<div style="text-align: center; font-size: 18px;">
    版本：2024.12.01　V.2
</div>
"""
st.markdown(markdown, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # 添加空白區域

with st.expander("顯示程式碼與地圖"):
    with st.echo():

        # 建立地圖
        map = leafmap.Map(center=[23.5825, 120.5855], zoom=8)
        
        # 讀取shp內容
        regions = 'https://github.com/NCUEGEO42/My-Tiff/raw/refs/heads/main/Population.shp'
        gdf = gpd.read_file(regions)
        
        # 將 P_CNT 欄位轉換為數字，無效值轉為 NaN
        gdf['P_CNT'] = pd.to_numeric(gdf['P_CNT'], errors='coerce')
        
        # 檢查 gdf 內的欄位名稱
        print(gdf.columns)  # 確認地理資料是否包含 COUNTYCODE 或適合的字段
        
        # 定義顏色分層，這裡使用 P_CNT 欄位
        choropleth = Choropleth(
            geo_data=gdf.__geo_interface__,  # 使用 GDF 的 geo_interface 來獲取 GeoJSON 格式
            data=gdf,
            columns=['COUNTYCODE', 'P_CNT'],  # 假設 COUNTYCODE 是要匹配的字段
            key_on='feature.properties.COUNTYCODE',  # 根據 'COUNTYCODE' 來匹配資料
            fill_color='YlOrRd',   # 使用漸層顏色
            fill_opacity=0.65,
            line_opacity=0.5,
            legend_name='人口數量'
        ).add_to(map)

        # 顯示地圖
        map.to_streamlit(height=720)
