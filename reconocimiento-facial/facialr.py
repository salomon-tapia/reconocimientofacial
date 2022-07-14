from deepface import DeepFace

obj = DeepFace.analyze(img_path = "/home/SALOMON TAPIA/Imágenes/lucia.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print(obj)