import os

def folder_formatting(folder_path:str):
    folder_path = folder_path

    images_path = os.listdir(folder_path)

    folder_path = os.path.join(folder_path)

    for i,image_path in enumerate(images_path):
        name = image_path.split('.')[0]
        type = image_path.split('.')[1]
        os.rename(folder_path + image_path,folder_path + str(i) + '.' + 'jpg')

folder_formatting('disgust/')