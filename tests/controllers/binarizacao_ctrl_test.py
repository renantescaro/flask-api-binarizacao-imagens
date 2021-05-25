import requests
import sys
sys.path.append('C:/Users/renan.tescaro/Desktop/flask/flask-api-binarizacao-imagens/')

class BinarizacaoCtrlTest:
    def __init__(self):
        self._url = 'http://localhost:5000'


    def binarizar(self):
        return requests.post(
            url     = str(self._url+'/binarizar'),
            params  = {
                'file':''
            }, 
            headers = {} )


BinarizacaoCtrlTest().binarizar()