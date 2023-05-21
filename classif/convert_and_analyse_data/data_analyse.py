import os
import pandas

path_to_data = "/content/drive/MyDrive/sets_above30/crop"

count = {}
for folder in os.listdir(path_to_data):
    nb = len(os.listdir(os.path.join(path_to_data, folder)))
    count[folder] = nb

#on veut convertir ce dict en dataframe

df = pandas.DataFrame.from_dict(count, orient='index', columns=['nb_images'])
print(df)
df.to_csv("/content/lepinoc-detection_for_collab/classif/convert_data/nb_image_specie.csv", index=True, header=True, sep=',')