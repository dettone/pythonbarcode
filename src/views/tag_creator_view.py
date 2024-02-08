from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController
class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''
    def validade_and_create_tag(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        
        body = http_request.body
        product_code = body["product_code"]
       
        formatted_response = tag_creator_controller.create(product_code)
        
       
        #logica de regra de negocio
        return HttpResponse(status_code=200, body=formatted_response)
