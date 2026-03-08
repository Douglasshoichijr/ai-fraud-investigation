import json
from crewai.tools import tool


@tool("marketplace_search")
def marketplace_search(product_name: str) -> str:
    """
    Simula busca de anúncios de um produto em marketplaces.
    """

    with open("simulator/marketplace_data.json") as f:
        data = json.load(f)

    results = [item for item in data if item["product_name"] == product_name]

    return str(results)