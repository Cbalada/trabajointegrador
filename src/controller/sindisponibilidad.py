from domain.auricular_handler import Handler

class SindisponibilidadHandler(Handler):
    def handle(self,request):
        if request.marca.lower() !="genius" and request.marca.lower() !="logitech" and request.marca.lower() !="sony":
            print("La empresa maneja el pedido.")
            print(request)
        else:
            super().handle(request)