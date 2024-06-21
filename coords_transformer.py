from qgis.core import QgsProject, QgsCoordinateTransform, QgsPointXY
from qgis.gui import QgsMapCanvas
from qgis.utils import iface

# Get project CRS
crs = QgsProject.instance().crs()
print(f"Project CRS: {crs.authid()}")

# Set target CRS
target_crs = QgsCoordinateReferenceSystem("EPSG:4326")

# Get current map canvas
canvas = iface.mapCanvas()

# Setup coordinate grabber
def get_coords():
    point = canvas.mouseLastXY()
    qgs_point = canvas.getCoordinateTransform().toMapCoordinates(point.x(), point.y())
    
    return(qgs_point.x(), qgs_point.y())

# Setup coordinate transformer
def transform_coords(x, y, source_crs):
    transform = QgsCoordinateTransform(source_crs, target_crs, QgsProject.instance())
    point = transform.transform(QgsPointXY(x, y))
    return point.y(), point.x()

# Tranform coordinates
x, y = get_coords()
lat, long = transform_coords(x, y, crs)

print(f"Original Coordinates: (X: {x}, Y: {y})")
print(f"Transformed Coordinates: (Latitude: {lat}, Longitude: {long})")