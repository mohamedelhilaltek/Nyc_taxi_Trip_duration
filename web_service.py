from flask import Flask,jsonify,request
import pickle
import numpy as np

with open('model.bin','rb') as model:
    model=pickle.load(model)


with open('dv.bin','rb') as dv :
    dv=pickle.load(dv)

app=Flask('model')

@app.route('/model',methods=['POST'])
def predict():
    data=request.get_json()
    data=dv.transform([data])
    y_pred=model.predict_proba(data)[0,1]
    yes=y_pred>=.5
    result={
      'y_pred':float(y_pred),
      'result':bool(yes)
    }

    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)


