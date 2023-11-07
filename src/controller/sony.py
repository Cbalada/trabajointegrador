from domain.auricular_handler import Handler

class SonyHandler(Handler):
    def handle(self,request):
        if request.marca.lower()=="sony":
            print("La empresa sony maneja el pedido.")
            print(request)
        else:
            super().handle(request)