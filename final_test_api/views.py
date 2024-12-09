from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Producto, Cliente, Pedido, DetallePedido
from .serializers import ProductoSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
@api_view(['GET'])
def get_products_by_client(request, client_id):
    try:
        # Verifica si el cliente existe
        cliente = Cliente.objects.get(id=client_id)

        # Obtén todos los pedidos del cliente
        pedidos = Pedido.objects.filter(cliente=cliente)

        # Extrae los productos de los detalles de los pedidos
        detalles = DetallePedido.objects.filter(pedido__in=pedidos)
        productos = [detalle.producto for detalle in detalles]

        # Serializar los productos únicos
        productos_serializados = ProductoSerializer(set(productos), many=True)
        return Response(productos_serializados.data)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente no encontrado"}, status=404)