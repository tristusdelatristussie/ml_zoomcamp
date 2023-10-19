from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

with open('model1.bin', 'rb')  as f_in:
    model = pickle.load(f_in)
f_in.close()

with open('dv.bin', 'rb')  as f_in:
    dv = pickle.load(f_in)
f_in.close()

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    #df_data = pd.DataFrame(data, index=[0])
    #df_data = pd.DataFrame.from_dict(data,  orient="index" )
    #df_data = data.to_dict(orient='records')
    #df_data = pd.DataFrame(data, index=[0]).values.reshape(1, -1)
    data_vect = dv.transform([data])

    prediction = model.predict_proba(data_vect)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9797) 



# 1 
# 2 
# 3
# 4 0.140
# 5
# 6
# 
#