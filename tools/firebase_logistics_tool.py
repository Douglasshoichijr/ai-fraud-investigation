from crewai.tools import tool
from database.firebase_client import get_collection


@tool("delivery_status_lookup")
def delivery_status_lookup(order_id: str) -> str:
    """
    Consulta no Firebase o status de entrega de um pedido específico.
    """

    deliveries = get_collection("deliveries")

    if not deliveries:
        return "Nenhuma entrega encontrada."

    # caso seja dict
    if isinstance(deliveries, dict):

        for key, delivery in deliveries.items():

            if delivery is None:
                continue

            if str(delivery.get("order_id")) == str(order_id):

                return str(delivery)

    # caso seja lista
    if isinstance(deliveries, list):

        for delivery in deliveries:

            if delivery is None:
                continue

            if str(delivery.get("order_id")) == str(order_id):

                return str(delivery)

    return "Entrega não encontrada."