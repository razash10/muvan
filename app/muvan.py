from app.utils.logger import logger_decorator
from flask import Flask, jsonify
from app.app_state import state

def create_app():
    app = Flask(__name__)

    @app.route('/properties_of_leases_about_to_expire/<int:days>', methods=['GET'])
    @logger_decorator
    def properties_of_leases_about_to_expire(days):
        properties = state.insight_properties_of_leases_about_to_expire(days=days)
        return jsonify({"properties": properties})

    @app.route('/top_units_with_long_vacancies/<int:count>', methods=['GET'])
    @logger_decorator
    def top_units_with_long_vacancies(count):
        top_units = state.insight_top_units_with_long_vacancies(count=count)
        return jsonify({"units": top_units})

    return app
