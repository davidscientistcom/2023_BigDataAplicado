import uuid
import datetime
from abc import ABC
import Fakeable

class WaterMeter(ABC,Fakeable):
    """Representa un medidor de agua con información de fabricación y capacidad de instalación."""

    def __init__(self, build_datetime, manufacture_datetime, trademark, type, size, model):
        """
        Inicializa una nueva instancia de WaterMeter con los detalles proporcionados.

        :param build_datetime: Fecha y hora de construcción del medidor.
        :param manufacture_datetime: Fecha y hora de fabricación del medidor.
        :param trademark: Marca comercial del medidor.
        :param type: Tipo de medidor.
        :param size: Tamaño del medidor.
        :param model: Modelo del medidor.
        """
        self.serial = str(uuid.uuid4())  # Serial único generado automáticamente.
        self.manufacture_datetime = manufacture_datetime
        self.trademark = trademark
        self.type = type
        self.size = size
        self.model = model

    def install(self, id_cliente, id_operator):
        """
        Registra la instalación del medidor de agua para un cliente específico y operador.

        :param id_cliente: Identificador del cliente.
        :param id_operator: Identificador del operador que realiza la instalación.
        """
        self.id_cliente = id_cliente
        self.id_operator = id_operator
        self.installation_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')  
