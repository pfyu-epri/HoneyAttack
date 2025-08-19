import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pyrosm import OSM

# 读取 Foursquare 数据集
foursquare_file_path = 'data/dataset_TSMC2014_NYC.csv'
try:
    foursquare_data = pd.read_csv(foursquare_file_path)
    print('Foursquare 数据集基本信息：')
    foursquare_data.info()

    # 绘制 Foursquare 数据集中某列的直方图（假设使用第一列）
    first_column = foursquare_data.columns[0]
    foursquare_data[first_column].hist()
    plt.title('Foursquare dataset {} histgram'.format(first_column))
    plt.xlabel(first_column)
    plt.ylabel('frequence')
    plt.show()
except FileNotFoundError:
    print('未找到 Foursquare 数据集文件，请检查路径。')

# 读取 OpenStreetMap 数据集
osm_file_path = 'data/new-york-latest.osm.pbf'
try:
    osm = OSM(osm_file_path)
    pois = osm.get_pois()
    print('OpenStreetMap POI basic information：')
    pois.info()

    # 绘制 OpenStreetMap 兴趣点的分布散点图
    pois.plot(markersize=1)
    plt.title('OpenStreetMap POI scatter')
    plt.show()
except FileNotFoundError:
    print('未找到 OpenStreetMap 数据集文件，请检查路径。')