from flask import render_template, jsonify, Blueprint
from datetime import date, timedelta
from flaskr.services.binarizacao_service import BinarizacaoSv

bp = Blueprint(
    'binarizacao',
    __name__,
    template_folder='templates' )

class BinarizacaoCtrl:
    @bp.route('/binarizar', methods=['GET', 'POST'])
    def binarizar():
        # BinarizacaoSv()
        return jsonify({'status':'ok'})