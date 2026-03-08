from crewai.tools import tool
from database.firebase_client import get_collection


@tool("refunds_database_lookup")
def refunds_database_lookup(reason: str) -> str:
    """
    Busca no Firebase todos os reembolsos cujo motivo seja o informado
    e retorna os pedidos associados.
    """

    refunds = get_collection("refunds")

    if not refunds:
        return "Nenhum reembolso encontrado."

    results = []

    for key, refund in refunds.items():

        if refund.get("reason") == reason:

            results.append({
                "order_id": refund.get("order_id"),
                "refund_value": refund.get("refund_value"),
                "reason": refund.get("reason")
            })

    return str(results)