import pandas as pd

# SAPS
# GEOID doesn't load in right so use a 0 instead
saps = pd.read_csv('AllThemesTablesSA.csv', encoding="utf-8-sig", usecols=[0,"GEOGTYPE","GEOGDESC", "T1_1AGETM", "T1_1AGETF", "T1_1AGETT"])

#Settlements - AllThemesTablesST.csv
sts = pd.read_csv('AllThemesTablesST.csv', encoding="utf-8-sig", usecols=[0,"GEOGTYPE","GEOGDESC", "T1_1AGETM", "T1_1AGETF", "T1_1AGETT"])
sts1000 = sts[sts.T1_1AGETT>1000]

#write to csv
sts1000.to_csv('sts_gt_1000.csv')

# read the filtered file from qgis csv
qsts = pd.read_csv('qgis_sts_gt_1000.csv')

# merge the data between the two dataframes discarding non matches
test = pd.merge(sts1000, qsts, on='GEOGID', how='right')
test.to_csv('study_area_gt_1000.csv', encoding="utf-8-sig")