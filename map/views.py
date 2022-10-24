import vincent, json
import numpy as np
from django.shortcuts import render
from folium import plugins, raster_layers
import folium



from django.shortcuts import render

import pandas as pd
# Create your views here.

def index(request):
    # creation of map comes here + business logic

    m = folium.Map(location=[33.886917, 9.537499], zoom_start=2, control_scale=True, min_zoom=2, min_lot=-179,
                   max_lot=179, min_lat=-65, max_lat=179, max_bounds=True)
    state_geo = f"geoFiles/Tunisia.geojson"
    df = pd.read_csv('https://raw.githubusercontent.com/wbg1230/datandvi/main/ndvidata.csv', encoding='utf-8',
                     na_values=None)
    d = df[(df['Date'] >= '2000-01-01') & (df['Date'] <= '2011-12-21') & (df['Province'] == 'Ariana')]
    a = d[['Data_long_term_Average']].stack().mean()
    datadate = d[['Date']].values.tolist()
    dataplot = d[['Data_long_term_Average']].values.tolist()
    def numpy_flat(a):
        return list(np.array(a).flat)
    k = numpy_flat(dataplot)
    k1 = numpy_flat(datadate)
    m.choropleth(
        geo_data=state_geo,
        data=df,
        columns=['Province', 'Data'],
        key_on='feature.properties.gov_name_f',
        fill_color='YlOrRd',
        fill_opacity=1,
        line_opacity=1,
        legend_name='NDVI per gov',
        smooth_factor=0)
    g = folium.GeoJson(state_geo, name="geojson").add_to(m)
    folium.Marker(fields=["gov_name_f"]).add_to(g)

    html = """
        
        <html>
This is a test
<h1>Gafsa Gov Data..</h1>

</html>
        """

    test = folium.Html(html, script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.Marker(location=[33.886917, 9.537499], popup=popup,max_width=450,min_width=450).add_to(m)
    m = m._repr_html_()  # updated
    context = {
        'm': m,'a':a,'k':k,'k1':k1

    }
    return render(request, 'index.html', context)