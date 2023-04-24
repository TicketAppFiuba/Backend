from src.schemas.coordinate import CoordinateSchema
import math

def distance(a: CoordinateSchema, b: CoordinateSchema):
    rad = math.pi/180
    dlat = b.latitude - a.latitude
    dlon = b.longitude - a.longitude
    R = 6372.795477598
    arg =(math.sin(rad*dlat/2))**2 + math.cos(rad*a.latitude)*math.cos(rad*b.latitude)*(math.sin(rad*dlon/2))**2
    distancia = 2*R*math.asin(math.sqrt(arg))
    return distancia