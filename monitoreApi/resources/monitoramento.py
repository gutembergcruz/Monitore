from resources.conexcoesFirebase import requisicaoFireBase
from flask_restful import Resource



class Monitoramento(Resource):
    def get(self):
        datas = requisicaoFireBase()
        if type(datas) == list:
            return {'data': [datas]}
        else:
            return {'message': 'Data not found.'}
class River(Resource):
    def get(self, id_river):
        datas = requisicaoFireBase()
        rivers = datas
        for river in rivers:
            if river['id_river'] == id_river:
                return river
        return {'message': 'River not found.'}, 404