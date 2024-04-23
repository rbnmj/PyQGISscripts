# gives info about the feature size of the selected features in the 
# current layer or in an input layer
def featuresize(layername=None):
    if layername is None:
        layer = qgis.utils.iface.mapCanvas().currentLayer()
    else:
        layer = QgsProject.instance().mapLayersByName(layername)[0]
    if layer is None: 
         return print("Layer not found.")
    selected_features = layer.selectedFeatures()
    if len(selected_features) == 0:
        return print("No features selected.")
    areas = {}
    # Check the geometry type of the layer and calculate the size for each selected feature
    if layer.geometryType() == QgsWkbTypes.PolygonGeometry:
        for feature in selected_features:
            area = feature.geometry().area()
            areas[feature.id()] = area
        for feature_id, area in areas.items():
            print(f"Feature ID {feature_id}: {area/10000:.2f} ha")
        print(f"Area sum: {round(sum(areas.values())/10000,2)} ha")
    else:
        return print("Unsupported geometry type.")