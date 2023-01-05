from flask import Flask,render_template,jsonify,request
import config
from project_.utils import Iris


app =Flask(__name__)
## creating home api
@app.route("/")
def test_class():
    return render_template("index.html")


# api for  prediction
@app.route("/predict_length",methods=['POST',"GET"])
def test1_class():
    if request.method=="GET":
        print("we are running get method")

        data= request.form
        sepal_width   = int(data[4.3])
        petal_length  = eval(data[5.3])
        petal_width   = int(data[4.2])
        species       = data['species']
        find_lenght   = Iris(sepal_width,petal_length,petal_width,species)
        return jsonify({"Result":f'prediction of value {find_lenght}'})
    else:
        print("we are in post method")
        sepal_width   = int(request.args.get(4.3))
        petal_length  = int(request.args.get(5.3))
        petal_width   = int(request.args.get(4.2))
        species       = request.args.get('species')
        find_lenght   = Iris(sepal_width,petal_length,petal_width,species)
        return jsonify({"Result":f'prediction of value {find_lenght}'})


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NO)