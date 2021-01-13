from flask import Blueprint, jsonify, request
from flask_login import login_required
from ..models import Team
from app.models import db

team_routes = Blueprint('teams', __name__)


@team_routes.route('/')
# @login_required
def teams():
    teams = Team.query.all()
    return {"teams": [team.to_dict() for team in teams]}

@team_routes.route('/create-team', methods=['POST'])
# @login_required
def create_team():
    new_team = Team()

    new_team.name = request.get_json().get('name')
    new_team.user_id = request.get_json().get('user_id')
    # new_team.pokemons = request.get_json().get('pokemons')

    db.session.add(new_team)
    db.session.commit()

    return new_team.to_dict()
