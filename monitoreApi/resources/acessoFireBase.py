import pyrebase

def trata_registro(registros):
    cont = 1
    novos_registros = []
    for novo in registros:
        novos_registros.append({
            'id_register' : str(cont),
            'date' : novo['Data'],
            'hour' : novo['Hora'],
            'PH' : novo['PH']
            })
        cont+=1
    return novos_registros

class fireAcess():
    def __init__(self,config):
        self.config = config
        self.data = ''
        self.all_data = []
        self.last_data = []

    def inicialize(self):
        firebase = pyrebase.initialize_app(self.config)
        data = firebase.database()
        dados = data.child('Dados').get()
        self.data = dados
        return self.data

    def trata_dado(self):
        dados = []
        novos_dados = []
        for dado in self.data.each():
            dado_tratado = dado.val()
            dados.append(dado_tratado)
        
        for dado in dados:
            if dado != None:
                dado['Registros'] = dado['Registros'][1:]
                novos_dados.append(dado)
        dados = novos_dados
        novos_dados = []
        cont = 1
        for rio in dados:
            novos_registros = trata_registro(rio['Registros'])
            novos_dados.append({
                'id_river': str(cont),
                'adress' : rio['Endereco'],
                'river' : rio['Nome'],
                'registers': novos_registros
            })
            cont+=1
            
    
        self.all_data = novos_dados

    def return_all(self):
        return self.all_data

    def return_last(self):
        self.last_data = self.all_data[-1]
        return self.last_data 
        