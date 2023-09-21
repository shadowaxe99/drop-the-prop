
from flask import Flask, render_template
from .models import db
from .services import order_processing, inventory_management, customer_support, decision_making, data_collection, data_preprocessing
from .ai import nlu, ml_model, agent_actions
from .ui import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    app.register_blueprint(main_blueprint)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
