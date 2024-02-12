from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

from src.errors.error_handler import handle_errors

from src.validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validade_and_create_tag(http_request)
    except Exception as error:
        response = handle_errors(error)

    return jsonify(response.body), response.status_code