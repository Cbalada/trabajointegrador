from service.auricular import Auricular
from domain.clases import AbstractAuricularBuilder

class AuricularBuilder(AbstractAuricularBuilder):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuricularBuilder, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.marca = None
        self.modelo = None
        self.color = None

    def with_marca(self, marca):
        self.marca = marca
        return self

    def with_modelo(self, modelo):
        self.modelo = modelo
        return self

    def with_color(self, color):
        self.color = color
        return self

    def build(self):
        return Auricular(self)



