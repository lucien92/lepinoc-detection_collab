import os
import pandas as pd
path_to_hierarchy = "/content/lepinoc-detection_for_collab/classif/convert_and_analyse_data/Liste_especes_IA_Lepi_noc_.csv"
path_to_data = "/content/drive/MyDrive/sets_above30/cleaned_data_above30"
try:
    os.mkdir("/content/drive/MyDrive/sets_above30/final_cleaned_data")
except:
    pass

df = pd.read_csv(path_to_hierarchy, delimiter = ";")
espece = list(df["Espece"])

for espece in os.listdir(path_to_data):
    if espece in espece:
        os.system('cp -r "' + path_to_data + '/' + espece + '" "/content/drive/MyDrive/sets_above30/final_cleaned_data"')

#on veut supprimer le dossier path_to_data

os.system("rm -r " + path_to_data)