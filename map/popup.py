from django.shortcuts import render
from folium import plugins, raster_layers
import folium
import branca
from django.shortcuts import render

import pandas as pd
# Create your views here.
def popup_html(row):
    data = f"geoFiles/data.csv"
    df = pd.read_csv(data)
    d = df.iloc[578:972]
    i = row
    gov= df['Province'].iloc[i]
    ndvi= df['Data'].iloc[i]
    ndviavg = df['Data_long_term_Average'].iloc[i]
    Date = df['Date'].iloc[i]
    a = d[['Data_long_term_Average']].stack().mean()

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(gov) + """

</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Institution Type</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(ndviavg) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Institution URL</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(ndvi) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">City and State</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(Date) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Highest Degree Awarded</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(a) + """
</tr>
</tbody>
</table>
</html>
"""
    return html