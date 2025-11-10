from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from SMTH.utils.config import DB_CONFIG

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuração do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "chave_super_secreta"

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa rotas
    from SMTH.routes.auth_routes import auth_bp
    from SMTH.routes.dataset_routes import dataset_bp
    from SMTH.routes.analysis_routes import analysis_bp


    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dataset_bp, url_prefix="/datasets")
    app.register_blueprint(analysis_bp, url_prefix="/analysis")

    return app
