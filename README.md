📑 Análise de Fidelidade e Segmentação RFM (Dataset Olist)

<img width="1425" height="797" alt="dashboard de segmentacao estrategica e saude da base rfm" src="https://github.com/user-attachments/assets/9406dfd7-9ae0-475b-87f6-382cebe19b16" />

<img width="1424" height="799" alt="dashboard rfm - 2017" src="https://github.com/user-attachments/assets/6f3e6bc7-217f-4977-9fbb-d8fc61fa4a26" />

<img width="1427" height="800" alt="dashboard rfm - 2018" src="https://github.com/user-attachments/assets/7fddbbb2-3126-4748-99f7-6d420ced5aed" />

Este projeto apresenta um pipeline de dados completo — da extração à visualização — utilizando o dataset público da Olist. O objetivo é aplicar a metodologia RFM (Recency, Frequency, Monetary) para segmentar clientes e gerar insights estratégicos sobre retenção e churn.


Tecnologias e Ferramentas

  Banco de Dados: SQL Server Express (Armazenamento e carga)
  
  Linguagem: Python 3.x

  Principais Bibliotecas:
  
    Pandas (Tratamento e lógica de scores)
    SQLAlchemy & PyODBC (Integração SQL)
    python-dotenv (Segurança e variáveis de ambiente)
    

Processamento de Dados (ETL com Python)

Para garantir a precisão estatística, desenvolvi um motor de processamento em Python que automatiza a inteligência do projeto.


Destaques Técnicos:

  Cálculo Estatístico Equilibrado: Uso da função qcut do Pandas para dividir a base em quintis, garantindo que os scores (1 a 5) sejam distribuídos de forma homogênea, evitando distorções.

  Segurança e Portabilidade: Implementação de python-dotenv para gerenciar as credenciais do servidor SQL, mantendo o código seguro e fácil de configurar em diferentes ambientes.

  Tratamento de Exceções: Uso de blocos try-except e validações com pd.to_numeric para garantir a integridade do pipeline.
  
  Resolução de Bugs: Implementação de reset_index() para solucionar conflitos de índice no SQL Server durante a exportação.

Modelagem e Dashboard (Power BI)

A camada de visualização foi construída para responder a perguntas críticas de negócio.

  Modelagem Star Schema: Implementação de tabela Calendário e relacionamentos otimizados.
  
  Métricas DAX: Inteligência de tempo e cálculos de segmentação dinâmica.
  
  Limpeza Visual: Ajuste de layout com foco em UX (User Experience), removendo eixos redundantes e utilizando histogramas para análise de distribuição de Recência e Frequência.


Como executar

  1. Configuração do Banco:

  Execute o script em scripts_sql/schema.sql no seu SQL Server.


  3. Ambiente Python:

  Crie seu ambiente virtual: python -m venv venv
  
  Ative o ambiente e instale as dependências: pip install -r requirements.txt
  
  Crie um arquivo .env baseado no .env.example com os dados do seu servidor local.
  

  5. Processamento:
     
   Rode o script: python scripts_python/processar_rfm.py


  7. Visualização:
     
  Abra o arquivo em dashboard/ e atualize a fonte de dados.


Sobre o Autor

Desenvolvido por Fabrício Felipe, graduando em Ciência da Computação na Anhanguera.


📈 Evolução e Melhorias Futuras

Este projeto está em constante desenvolvimento. Como parte do meu aprendizado em Engenharia de Dados, UX Design e programação em python.
