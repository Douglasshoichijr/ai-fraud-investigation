# 🧠 AI Multi-Agent Fraud Investigation System

Sistema de **investigação de fraude em e-commerce utilizando agentes de Inteligência Artificial**.

Este projeto demonstra como uma **arquitetura multi-agent baseada em LLMs** pode investigar inconsistências entre **pedidos, reembolsos e entregas**, cruzando diferentes fontes de dados para identificar possíveis fraudes.

⚠️ **Importante:**  
Este projeto é um **MVP (Minimum Viable Product)** criado como **prova de conceito** para demonstrar como agentes de IA podem colaborar na investigação de fraudes em plataformas de e-commerce.  

A ideia pode ser expandida futuramente com:

- modelos de detecção de fraude
- análise estatística avançada
- integração com marketplaces reais
- dashboards de monitoramento
- pipelines de dados em produção

---

# 🚨 Problema Investigado

Uma empresa de **e-commerce** identificou um aumento de **35% nos reembolsos** com o motivo:


"produto não entregue"


Porém os dados internos mostram que:

- 📦 os registros logísticos indicam **entregas confirmadas**
- 📞 o número de reclamações no suporte **não aumentou**
- 📈 o volume de vendas **permaneceu estável**

Isso levanta uma hipótese de fraude:



# 🎯 Objetivo do Projeto

Criar um sistema que utilize **agentes de IA especializados** para:

- analisar reembolsos
- validar entregas
- detectar padrões de fraude
- investigar possíveis revendas
- gerar um relatório investigativo

Tudo isso utilizando **arquitetura multi-agent com CrewAI**.

---

# 🧠 Arquitetura Multi-Agent

O sistema utiliza **agentes especializados**, cada um responsável por uma etapa da investigação.

Fluxo da investigação:


Refund Analysis Agent

#        ↓

Logistics Validation Agent

#        ↓

Pattern Detection Agent

#        ↓

Marketplace Investigation Agent

#        ↓

Fraud Report Agent

# 
Cada agente recebe o **contexto da etapa anterior**, criando uma **investigação progressiva**.

---

# 🤖 Agentes Utilizados

## 1️⃣ Refund Analysis Agent

Responsável por analisar os dados de reembolsos.

Funções:

- consultar o banco de reembolsos
- identificar pedidos com motivo **"produto não entregue"**
- extrair `order_id` suspeitos

Output:


order_id
refund_value


---

## 2️⃣ Logistics Validation Agent

Responsável por validar os dados logísticos.

Funções:

- consultar banco de entregas
- verificar status de entrega

Critério de inconsistência:


refund_reason = produto não entregue
delivery_status = entregue


Quando isso ocorre, o pedido é marcado como **suspeito**.

---

## 3️⃣ Pattern Detection Agent

Responsável por detectar **clusters de fraude**.

Os dados são agrupados por:

- produto
- cidade
- cliente
- transportadora

Exemplo de cluster:


Produto: Tênis X
Cidade: Campinas
Pedidos suspeitos: 61


---

## 4️⃣ Marketplace Investigation Agent

Responsável por investigar **revenda de produtos**.

Busca anúncios simulados em marketplaces como:

- OLX
- Facebook Marketplace
- Mercado Livre

Critério suspeito:


preço < 60% do valor original
mesma cidade dos pedidos suspeitos


---

## 5️⃣ Fraud Report Agent

Responsável por consolidar todas as evidências e gerar um **relatório final**.

O relatório contém:

- produto mais afetado
- cidade com maior incidência
- número de pedidos suspeitos
- estimativa de prejuízo
- anúncios encontrados

---

# 🗄️ Banco de Dados

O projeto utiliza **Firebase Realtime Database** para simular os dados do e-commerce.

Estrutura do banco:

### Orders


order_id
client_id
product_id
product_name
price
city
order_date


---

### Refunds


refund_id
order_id
reason
refund_date
refund_value


Filtro principal:


reason = "produto não entregue"


---

### Deliveries


order_id
delivery_status
delivery_date
carrier
delivery_city


Status possíveis:


entregue
em_transito
falha


---

# 🛠 Tools Criadas

Para permitir que os agentes acessem os dados, foram criadas **tools customizadas**.

### refunds_database_lookup

Consulta reembolsos no Firebase.

---

### delivery_status_lookup

Consulta status de entrega de um pedido.

---

### order_lookup

Busca informações detalhadas de pedidos.

---

### marketplace_search

Simula busca de anúncios em marketplaces.

---


## 📂 Estrutura do Projeto

```
.
├── main.py
├── crew.py
├── tasks.py
├── config.py
├── agents.py
├── database
│   ├── firebase_client.py
│   └── ...
├── tools
│   ├── firebase_refunds_tool.py
│   ├── firebase_logistics_tool.py
│   ├── marketplace_simulator_tool.py
│   └── ...
├── requirements.txt
├── .env
└── ...
```

# 📄 Explicação dos Arquivos

### main.py

Arquivo principal que inicia o sistema.

Responsável por:

- iniciar a Crew
- executar as tasks
- iniciar a investigação.

---

### crew.py

Define a **orquestração dos agentes**.

Aqui é criado o objeto:


Crew(...)


que coordena:

- agentes
- tasks
- fluxo de execução.

---

### agents.py

Define todos os **agentes especializados**.

Cada agente possui:

- role
- goal
- backstory
- tools

---

### tasks.py

Define as **tarefas executadas pelos agentes**.

Cada task:

- possui descrição
- expected_output
- agente responsável
- contexto das tarefas anteriores.

---

### database/firebase_client.py

Responsável por conectar ao **Firebase Realtime Database**.

---

### tools/

Contém todas as **ferramentas utilizadas pelos agentes** para acessar dados.

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone <repo-url>

Entre na pasta do projeto:

cd ai-fraud-investigation

Crie ambiente virtual:

python -m venv venv

Ative o ambiente:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt
🔑 Configuração do .env

Crie um arquivo .env na raiz do projeto.

Exemplo:

OPENAI_API_KEY=your_openai_key

FIREBASE_DATABASE_URL=https://your-database.firebaseio.com

SERPER_API_KEY=optional
▶️ Executar o Projeto

Execute:

python main.py

O sistema irá:

1️⃣ analisar reembolsos
2️⃣ validar entregas
3️⃣ detectar padrões
4️⃣ investigar marketplaces
5️⃣ gerar relatório final

📊 Exemplo de Resultado
Fraude potencial detectada

Produto: Tênis X
Cidade: Campinas

Pedidos analisados: 83
Reembolsos suspeitos: 61

Perda estimada: R$ 27.450
🚀 Possíveis Evoluções

Este MVP pode evoluir para:

sistema de detecção de fraude em tempo real

dashboards de investigação

machine learning para classificação de fraude

integração com marketplaces reais

análise comportamental de clientes

📚 Tecnologias Utilizadas

Python

CrewAI

Firebase Realtime Database

OpenAI API

Multi-Agent Systems

👨‍💻 Autor: Douglas Shoichi

Projeto desenvolvido como prova de conceito de investigação de fraude utilizando agentes de IA.


Isso deixa o projeto **nível portfólio de AI Engineer mesmo**.
