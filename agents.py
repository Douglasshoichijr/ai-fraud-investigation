from crewai import Agent
from tools.firebase_refunds_tool import refunds_database_lookup
from tools.firebase_logistics_tool import delivery_status_lookup
from tools.marketplace_simulator_tool import marketplace_search


refund_agent = Agent(
    role="Especialista em Análise de Reembolsos",

    goal="""
    Identificar padrões suspeitos de reembolsos em pedidos
    de e-commerce.
    """,

    backstory="""
    Você trabalha no time de prevenção a fraude de uma
    grande empresa de e-commerce.

    Sua especialidade é identificar comportamentos
    suspeitos em sistemas de reembolso.
    """,

    tools=[refunds_database_lookup],

    verbose=True
)



logistics_agent = Agent(
    role="Investigador de Logística",

    goal="""
    Verificar inconsistências entre os registros de entrega
    e os pedidos que receberam reembolso.
    """,

    backstory="""
    Você é um especialista em auditoria logística.

    Seu trabalho é verificar se pedidos marcados como
    reembolsados realmente não foram entregues.
    """,

    tools=[delivery_status_lookup],

    verbose=True
)



pattern_agent = Agent(
    role="Especialista em Detecção de Padrões",

    goal="""
    Detectar clusters de fraude agrupando dados
    por produto, cidade e cliente.
    """,

    backstory="""
    Você é um cientista de dados especializado em
    análise de comportamento fraudulento em e-commerce.
    """,

    verbose=True
)




marketplace_agent = Agent(
    role="Investigador de Marketplace",

    goal="""
    Identificar possíveis revendas de produtos obtidos
    por fraude em marketplaces online.
    """,

    backstory="""
    Você investiga marketplaces para encontrar produtos
    revendidos com preços suspeitos.
    """,

    tools=[marketplace_search],

    verbose=True
)



report_agent = Agent(
    role="Auditor de Fraude",

    goal="""
    Consolidar todas as evidências e produzir
    um relatório final de investigação de fraude.
    """,

    backstory="""
    Você é responsável por escrever relatórios de
    investigação para o time executivo da empresa.
    """,

    verbose=True
)