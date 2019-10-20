from resources.acessoFireBase import fireAcess

config = {
  "apiKey": "AIzaSyBZTK3RLOVVEpT3Z_p5GE_joZSGwvgy6_A",
  "authDomain": "acaizeirosnasaspace.firebaseapp.com",
  "databaseURL": "https://acaizeirosnasaspace.firebaseio.com",
  "projectId": "acaizeirosnasaspace",
  "storageBucket": "acaizeirosnasaspace.appspot.com",
  "messagingSenderId": "442327396125",
  "appId": "1:442327396125:web:675adba42aaf8c74c2fbf4",
  "measurementId": "G-M40Q8SF2BL"
}

def requisicaoFireBase():
  banco = fireAcess(config)
  banco.inicialize()
  banco.trata_dado()
  data_all = banco.return_all()
  return data_all
