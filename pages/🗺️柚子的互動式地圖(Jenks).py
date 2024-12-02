import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import geopandas as gpd
import folium
from folium import Choropleth, Popup

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
    柚子的互動式地圖-縣市總人口數量
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

        # 初始化地圖
        map = leafmap.Map(center=[23.5825, 120.5855], zoom=8)
        
        # 讀取shp文件
        regions = 'https://github.com/NCUEGEO42/My-Tiff/raw/refs/heads/main/Population.shp'
        gdf = gpd.read_file(regions)
        
        # 將 P_CNT 欄位轉換為數字，無效值轉為 NaN
        gdf['P_CNT'] = pd.to_numeric(gdf['P_CNT'], errors='coerce')
        
        # 確保 COUNTYCODE 欄位存在且是正確的
        if 'COUNTYCODE' not in gdf.columns:
            raise ValueError("COUNTYCODE 欄位缺失，無法繼續處理。")

        # 定義顏色分層，這裡使用 P_CNT 欄位
        choropleth = Choropleth(
            geo_data=gdf.__geo_interface__,  # 使用 GeoDataFrame 的 geo_interface 來獲取 GeoJSON 格式
            data=gdf,
            columns=['COUNTYCODE', 'P_CNT'],  # COUNTYCODE 匹配 P_CNT
            key_on='feature.properties.COUNTYCODE',  # 依據COUNTYCODE來匹配資料
            fill_color='YlOrRd',   # 使用漸層顏色
            fill_opacity=0.65,
            line_opacity=0.5,
            legend_name='縣市總人口數量',
            scheme='Jenks'
        ).add_to(map)

        # 點擊事件：顯示縣市訊息
        def on_click(event):
            county_name = event['properties']['COUNTYNAME']  # COUNTYNAME 是包含縣市名稱的欄位
            population = event['properties']['P_CNT']  # 擷取人口數量index
            popup_content = f"<b>縣市名稱:</b> {county_name}<br><b>縣市總人口數量:</b> {population}"
            popup = Popup(popup_content, max_width=300)
            popup.add_to(event.target)  # 為點擊的區域添加小視窗

        # 使每個區域可以點擊顯示詳細資料
        choropleth.geojson.add_child(folium.GeoJsonPopup(fields=['COUNTYNAME', 'P_CNT'], labels=True))

        # 顯示地圖
        map.to_streamlit(height=720)

#st.markdown("<br>", unsafe_allow_html=True)

        # 置中顯示屬性資料表格
#st.markdown(
            """
            <div style="text-align: center;">
                <h3>縣市人口數量資料表</h3>
            </div>
            """, unsafe_allow_html=True
        )
#st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <div style="width: 60%;">
            """, unsafe_allow_html=True
        )
#st.dataframe(gdf[['COUNTYNAME', 'P_CNT']], use_container_width=True)
#st.markdown("</div></div>", unsafe_allow_html=True)
