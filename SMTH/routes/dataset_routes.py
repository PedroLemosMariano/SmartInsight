from flask import Blueprint, request, jsonify
from SMTH.backend import dataset
from flask import current_app as app
from SMTH.backend import db

dataset_bp = Blueprint("dataset_bp", __name__)

@dataset_bp.route("/upload", methods=["POST"])
def upload_dataset():
    usuario_id = request.form.get("usuario_id")
    nome = request.form.get("nome")
    file = request.files.get("file")

    if not file:
        return jsonify({"erro": "Arquivo não enviado."}), 400

    try:
        df = dataset.validar_dataset(file)
        novo = dataset.salvar_dataset(usuario_id, nome, df)
        return jsonify({"mensagem": "Dataset salvo com sucesso!", "id": novo.id})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
