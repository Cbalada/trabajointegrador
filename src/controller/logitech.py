from domain.auricular_handler import Handler

class LogitechHandler(Handler):
    def handle(self,request):
        if request.marca.lower()== "logitech":
            print("la empresa logitech maneja el pedido.")
            print(request)
        else:
            super().handle(request)