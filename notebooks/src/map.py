#!/usr/bin/env python
# coding: utf-8
import sys
sys.path.append("..") 

from src.cluster import *
from src.colors import *

label_colors ={'Crosswalk':'#FABF1C',
               'CurbRamp':'#90C31F',
               'NoCurbRamp':'#E679B6',
               'NoSidewalk':'#BE87D8',
               'Obstacle' :'#78B0EA',
               'Occlusion':'#B3B3B3',
               'Other':'#B3B3B3',
               'Signal':'#63C0AB',
               'SurfaceProblem':'#F68D3E'}

def map_clusters(label_data,i):
    df = cluster_label_type_at_index(label_data,i)[2]
    df["clustered"] = df.duplicated(subset="cluster_id", keep=False)
    df1 = df[df['clustered'] == True]
    df2 = df[df['clustered'] != True]
    m = df2.explore(
        tiles="CartoDb DarkMatter",
        marker_type="circle",
        tooltip=["label_type", 'username', 'label_id','cluster_id','severity'],
        popup=["label_type", 'username', 'label_id','cluster_id','severity'],
        color = "#FFFFFF",
        marker_kwds={"radius":1.5, "fill":True},
        style_kwds={"stroke":True,"fillOpacity":0.2,"weight": 2}
    )
    
    return df1.explore(m=m,
                       tiles="CartoDb DarkMatter",
                       marker_type="circle",
                       tooltip=["label_type", 'username','label_id','cluster_id','severity'],
                        popup=["label_type", 'username', 'label_id','cluster_id','severity'],
                       cmap=get_label_colors(df1),
                       column="label_type",
                       marker_kwds={"radius":1.5, "fill":True},
                       style_kwds={"stroke":True,"fillOpacity":0.6,"weight": 2},
                      )





