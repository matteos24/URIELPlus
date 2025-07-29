import numpy as np
from pyproj import Geod
import ot

geod = Geod(ellps="WGS84")


def build_distributions(df):
    lang_distributions = {}
    for iso, grp in df.groupby("glottocode"):
        centroid = grp[["Centroid_Lon","Centroid_Lat"]].to_numpy(dtype="f8")
        weights   = grp["weight"].to_numpy(dtype="f8")
        lang_distributions[iso] = (centroid, weights)
    return lang_distributions


def geodesic_distance(lon1, lat1, lon2, lat2):
    az12, az21, dist = geod.inv(lon1, lat1, lon2, lat2, radians = False)
    return dist/1000

DISTANCE_MAX = geodesic_distance(0, 90, 0, -90)

def cost_matrix_calculate(iso1, iso2, lang_distributions):
    ptsA, w1 = lang_distributions[iso1]
    ptsB, w2 = lang_distributions[iso2]
    lonA, latA = ptsA[:, 0], ptsA[:, 1]
    lonB, latB = ptsB[:, 0], ptsB[:, 1]

    cost_matrix = np.zeros((len(lonA), len(lonB)))

    for i in range(len(lonA)):
        for j in range(len(lonB)):
            cost_matrix[i, j] = geodesic_distance(lonA[i], latA[i], lonB[j], latB[j])

    return cost_matrix

def w1_distance_language(iso1, iso2, lang_distributions):
    cost_matrix = cost_matrix_calculate(iso1, iso2, lang_distributions)

    ptsA, wA = lang_distributions[iso1]
    ptsB, wB = lang_distributions[iso2]

    return ot.emd2(wA, wB, cost_matrix)


def normalized_w1_distance(iso1, iso2, lang_distributions):
    lang_dist = w1_distance_language(iso1, iso2, lang_distributions)
    return lang_dist / DISTANCE_MAX