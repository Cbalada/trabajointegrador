from service.auricular_builder import AuricularBuilder
from controller.logitech import LogitechHandler
from controller.genius import GeniusHandler
from controller.sony import SonyHandler
from controller.sindisponibilidad import SindisponibilidadHandler

def controller(marca,modelo,color):
    logitech_handler=LogitechHandler()
    sony_handler=SonyHandler()
    genius_handler=GeniusHandler()
    sindisponibilidad_handler=SindisponibilidadHandler()

    logitech_handler.set_next(sony_handler)
    sony_handler.set_next(genius_handler)
    genius_handler.set_next(sindisponibilidad_handler)

    auricular=AuricularBuilder().with_marca(marca)\
                                .with_modelo(modelo)\
                                .with_color(color)\
                                .build()
    logitech_handler.handle(auricular)