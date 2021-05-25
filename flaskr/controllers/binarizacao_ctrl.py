from flask import render_template, jsonify, Blueprint
from PIL import ImageTk, Image
from datetime import date, timedelta
from flaskr.services.binarizacao_service import BinarizacaoSv

bp = Blueprint(
    'binarizacao',
    __name__,
    template_folder='templates' )

class BinarizacaoCtrl:
    @bp.route('/binarizar', methods=['GET', 'POST'])
    def binarizar():
        pillow_obj_inicial = Image.new("RGB", (100, 100))
        imagem_inicial     = pillow_obj_inicial.load()

        pillow_obj_final = Image.new("RGB", (100, 100))
        imagem_final     = pillow_obj_final.load()

        binarizacao = BinarizacaoSv(
            linha=100,
            coluna=100,
            imagem_original=imagem_inicial,
            imagem_final=imagem_final,
            limiar=80 )
        return jsonify({'status':'ok'})