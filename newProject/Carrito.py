from .models import Vinilo
from django.http import JsonResponse

class Carrito:
    
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def agregar(self, vinilo):
        id = str(Vinilo.idVinilo)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "Vinilo_id": Vinilo.idVinilo,
                "Nombre_Artista": Vinilo.nombreArt,
                "Nombre_Disco":  Vinilo.idVinilo,
                "Acumulado":  Vinilo.idVinilo,
                "Cantidad": 1,
            }
        else:
            self.carrito[id]["Cantidad"] +=1
            self.carrito[id]["Acumulado"] += vinilo.valorDisco

        self.guardar_carrito()

    def eliminar(self, vinilo):
        id = str(vinilo.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, vinilo):
        id = str(vinilo.id)
        if id in self.carrito.keys():
            self.carrito[id]["Cantidad"] -= 1
            self.carrito[id]["Acumulado"] -= vinilo.valorDisco
            if self.carrito[id]["Cantidad"] <= 0: self.eliminar(vinilo)
            self.guardar_carrito

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

