from PIL import Image
import os
dataTrainingDamaged = os.listdir('../data/validation/damaged')
for img in dataTrainingDamaged:
    image = Image.open('../data/validation/damaged/{}'.format(img))
    image= image.resize((256,256))
    image.save('../preprocessed_data/test/damaged/{}'.format(img))




