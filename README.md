# TCC - Desenvolvimento de Sistemas  
**Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Sul – Campus Pelotas Visconde da Graça**

## 📌 Sobre o Projeto

Este repositório contém o Trabalho de Conclusão de Curso (TCC) apresentado como requisito para a conclusão do curso técnico em Desenvolvimento de Sistemas.  
O projeto tem como objetivo analisar o desempenho de métricas de avaliação de código em algoritmos genéticos, além da produção da ferramenta **ACE**, que se categoriza como um **AG (algoritmo genético)**.

## 🎯 Objetivos

- Desenvolver um AG que gere código e evolua com base em métricas e métodos de seleção dinâmicos  
- Aplicar princípios de desenvolvimento ágil e boas práticas de programação  
- Implementar uma solução real com potencial de uso no mercado  
- Demonstrar competências técnicas adquiridas durante o curso  

## 🧰 Tecnologias Utilizadas

- **Linguagem de Programação:** Python  
- **Frameworks/Bibliotecas:** Flask, Peewee  
- **Banco de Dados:** PostgreSQL  
- **Outras Ferramentas:** Git, Figma, GitHub, VS Code  

## 🧱 Estrutura do Projeto

```plaintext
/database               → Banco de dados
  /models               → Tabelas
    geracao.py          → Histórico populacional
    pedido.py           → Histórico de pedidos
  database.py           → Configurações do ORM

/routes                 → Código-fonte principal (rotas Flask)
  documentacao.py       → Rota da página de documentação e funções associadas
  home.py               → Rota da página inicial e funções associadas
  pedido.py             → Rota da página de pedido e funções associadas
  sobre.py              → Rota da página sobre e funções associadas

/static                 → Arquivos estáticos
  /css
    styles.css          → Classes CSS
  /img
    *                   → Backgrounds das interfaces web
  /scripts              → Códigos do algoritmo genético
    ACE.py              → Core do AG (gerenciamento das rotinas)
    ai.py               → Consumo de API LLM
    genoma.py           → Geração de trechos de código
    keywords.py         → Dicionário de sintaxe com placeholders
    placeholder.py      → Suporte a placeholders temporários

/templates              → Interface do usuário (HTML)
  documentacao.html     → Documentação do sistema
  index.html            → Landing page e dashboard de resultados
  pedido.html           → Entrada de parâmetros para geração de código
  sobre.html            → Descrição do projeto

main.py                 → Core do projeto (execução do app Flask)  
config.py               → Configurações do servidor  
ACE.db                  → Banco de dados local  
README.md               → Este arquivo
````
📄 Documentação
A documentação técnica e o relatório completo estão disponíveis clicando aqui, incluindo:

Introdução e justificativa do projeto

Fundamentação teórica

Metodologia

Especificação técnica

Resultados e testes

Conclusão e trabalhos futuros

👨‍💻 Autor
Vinicius Armendaris Leal
Estudante do curso técnico em Desenvolvimento de Sistemas
IFRS – Campus Pelotas Visconde da Graça
