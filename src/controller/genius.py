from domain.auricular_handler import Handler

class GeniusHandler(Handler):
    def handle(self,request):
        if request.marca.lower()=="genius":
            print("La empresa genius maneja el pedido.")
            print(request)
        else:
            super().handle(request)