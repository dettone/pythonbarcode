from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''
    def validade_and_create_tag(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]
        print(product_code)
        #logica de regra de negocio
        return HttpResponse(status_code=200, body={"tag_path": "path_from_tag"})
