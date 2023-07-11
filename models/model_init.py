import gdown
import zipfile
import os

# lp localization model
url = "https://drive.google.com/uc?id=1GvBu2Emf8nReEMuQ1VURRXXDsu8lrU4n"
output = "models/lp_detection.zip"
gdown.download(url, output, quiet=False)

# character segmentation model
url = 'https://drive.google.com/uc?id=1bwBbtnQmR4Kw3vo9Q1ymwhXauDOLblod'
output = 'models/char_segmentation.zip'
gdown.download(url, output, quiet=False)

# character recognition model
url = 'https://drive.google.com/uc?id=18qab2q_rVI9pjdJuCgEjobRH7arkp21Z'
output = 'models/char_recognition.zip'
gdown.download(url, output, quiet=False)

# extract the model
with zipfile.ZipFile("models/lp_detection.zip", "r") as zip_ref:
    zip_ref.extractall("models/lp_detection")

with zipfile.ZipFile('models/char_segmentation.zip', 'r') as zip_ref:
    zip_ref.extractall('models/char_segmentation')

with zipfile.ZipFile('models/char_recognition.zip', 'r') as zip_ref:
    zip_ref.extractall('models/char_recognition')

# remove zip files
zips = ['models/lp_detection.zip', 'models/char_segmentation.zip', 'models/char_recognition.zip']
for file in zips:
    if os.path.exists(file):
        # Remove the file
        os.remove(file)
        print(f'{file} has been removed')
    else:
        print(f'{file} not found')
