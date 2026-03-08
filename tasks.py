# ==========================================
# importando classe e agentes 
from crewai import Task
from agents import (
    refund_agent,
    logistics_agent,
    pattern_agent,
    marketplace_agent,
    report_agent
)


# ==========================================
# Task de análise de reembolsos
refund_analysis_task = Task(
    description="""
    Analise o banco de dados de reembolsos.

    Identifique todos os registros onde o motivo do
    reembolso é 'produto não entregue'.

    Extraia os order_id associados.
    """,

    expected_output="""
    Lista de pedidos suspeitos contendo:

    order_id
    refund_value
    """,

    agent=refund_agent
)


# ==========================================
# task de logística
logistics_validation_task = Task(

    description="""
    Receba a lista de pedidos suspeitos da etapa anterior.

    Para cada order_id:

    consulte o banco logístico e verifique o delivery_status.

    Se encontrar:

    refund_reason = produto não entregue
    delivery_status = entregue

    marque o pedido como inconsistência suspeita.
    """,

    expected_output="""
    Lista de pedidos onde existe inconsistência
    entre reembolso e entrega confirmada.
    """,

    agent=logistics_agent,

    context=[refund_analysis_task]
)


# ==========================================
# Task de detecção de padrões
pattern_detection_task = Task(

    description="""
    Receba os pedidos com inconsistência.

    Agrupe os dados por:

    produto
    cidade
    cliente
    transportadora

    Identifique clusters suspeitos.
    """,

    expected_output="""
    Lista de clusters contendo:

    produto
    cidade
    quantidade de pedidos suspeitos
    """,

    agent=pattern_agent,

    context=[logistics_validation_task]
)


# ==========================================
# Task final de relatório
marketplace_investigation_task = Task(

    description="""
    Receba os produtos suspeitos identificados nos clusters.

    Busque anúncios no marketplace.

    Compare:

    preço
    cidade
    produto

    Se o preço estiver abaixo de 60% do valor original,
    marque como possível revenda fraudulenta.
    """,

    expected_output="""
    Lista de anúncios suspeitos encontrados.
    """,

    agent=marketplace_agent,

    context=[pattern_detection_task]
)



report_task = Task(

    description="""
    Consolide todos os resultados da investigação.

    Gere um relatório contendo:

    produto mais afetado
    cidade com maior incidência
    número de pedidos suspeitos
    estimativa de prejuízo
    anúncios encontrados
    """,

    expected_output="""
    Relatório final de investigação de fraude.
    """,

    agent=report_agent,

    context=[
        refund_analysis_task,
        logistics_validation_task,
        pattern_detection_task,
        marketplace_investigation_task
    ]
)
