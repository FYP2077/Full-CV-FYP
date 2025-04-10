import os
import shutil

# To make the images folder
try:
    os.mkdir('data/labels')
    os.mkdir('data/images')
except:
    pass

# To paste the required data from the data folder in the data/images folder
data_folder = os.listdir('data/')
for j,i in enumerate(data_folder):
    if not (i.endswith('.py') or i.startswith('ima') or i.startswith('lab')):
        images_path = os.path.join(i,'images')
        labels_path = os.path.join(i, 'labels')
        print(images_path)
        for image in os.listdir('data/' + images_path):
            print(image)
            print(j)
        # Moving images paths
        # shutil.move(images_path)