from flaskr.utils.debug import Debug
from flask import request, jsonify, Blueprint
from PIL import ImageTk, Image
from datetime import date, timedelta
from flaskr.services.binarizacao_service import BinarizacaoSv

bp = Blueprint(
    'binarizacao',
    __name__,
    template_folder='templates' )

class BinarizacaoCtrl:
    @bp.route('/binarizar', methods=['POST'])
    def binarizar():
        imagem = request.files['file']
        if imagem.filename != '':
            imagem.save('static/uploads/'+imagem.filename)

        # abre imagem salva
        imagem_original = Image.open('static/uploads/'+imagem.filename)
        largura, altura = imagem_original.size

        binarizacao = BinarizacaoSv(
            linha           = altura,
            coluna          = largura,
            imagem_original = imagem_original,
            limiar          = 80 )
        binarizacao.processar()
        return jsonify({'status':'ok'})