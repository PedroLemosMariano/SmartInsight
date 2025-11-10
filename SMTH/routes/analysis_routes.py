from flask import Blueprint, jsonify, request
from SMTH.backend import analysis, dataset, insights

analysis_bp = Blueprint("analysis_bp", __name__)

@analysis_bp.route("/<int:dataset_id>", methods=["GET"])
def analisar_dataset(dataset_id):
    try:
        df = dataset.carregar_dataset(dataset_id)
        resumo = analysis.gerar_resumo_estatistico(df)
        texto = insights.gerar_insights(df)

        return jsonify({
            "resumo": resumo.to_dict(),
            "insights": texto
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
