from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = load_model('sign_language.h5')

dic = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H',8 : 'I', 9 : 'K',
       10 : 'L', 11 : 'M', 12 : 'N', 13 : 'O', 14 : 'P', 15 : 'Q', 16 : 'R', 17 : 'S', 18 : 'T', 19 : 'U',
       20 : 'V', 21 : 'W', 22 : 'X', 23 : 'Y'}

model.make_predict_function()

@app.route('/')
def home():
	render_template('index.html')

@app.route('/predict',methods=['GET','POST'])


def upload():
       if request.form == 'POST':
              f = request.files('file')
              basepath = os.path.dir_name(__file__)
              filepath = os.path.join(basepath,'uploads', f.filename)
              f.save(filepath)

              img = image.load_img(filepath, target_size=(28, 28))
              x = image.img_to_array(img)
              x = np.expand_dims(x, axis=0)

              pred = model.predict_classes(x)
              index = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
              result = str(index[pred[0]])
              return result
       return None

if __name__ == '__main__':
	app.run(debug = True)

