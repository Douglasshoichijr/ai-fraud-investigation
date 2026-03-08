from crewai.tools import tool
from database.firebase_client import get_collection


@tool("order_lookup")
def order_lookup(order_id: str) -> str:
    """
    Busca um pedido específico no banco de dados de pedidos (orders)
    utilizando o order_id.
    """

    orders = get_collection("orders")

    if not orders:
        return "Nenhum pedido encontrado."

    for key, order in orders.items():

        if str(order.get("order_id")) == str(order_id):

            return str({
                "order_id": order.get("order_id"),
                "product_name": order.get("product_name"),
                "price": order.get("price"),
                "city": order.get("city"),
                "client_id": order.get("client_id")
            })

    return "Pedido não encontrado."