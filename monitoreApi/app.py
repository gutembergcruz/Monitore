from flask import Flask
from flask_restful import Api
from resources.monitoramento import Monitoramento,River

app = Flask(__name__)
api = Api(app)

api.add_resource(Monitoramento,'/dados')
api.add_resource(River, '/dados/<string:id_river>')
if __name__ == '__main__':
    app.run(debug=True)
