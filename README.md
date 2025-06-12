TCC - Desenvolvimento de Sistemas
Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Sul – Campus Pelotas Visconde da Graça

📌 Sobre o Projeto
Este repositório contém o Trabalho de Conclusão de Curso (TCC) apresentado como requisito para a conclusão do curso técnico em Desenvolvimento de Sistemas. 
O projeto tem como objetivo analisar o desempenho de metricas de avaliação de codigo em algoritmos geneticos e produção da ferramenta ACE que se categoriza com ag 
🎯 Objetivos
 Desenvolver um ag que gere codigo e evolua dependendo de metricas e metodos de seleção dinamicos

 Aplicar princípios de desenvolvimento ágil e boas práticas de programação

 Implementar uma solução real com potencial de uso no mercado

 Demonstrar competências técnicas adquiridas durante o curso

🧰 Tecnologias Utilizadas
Linguagem de Programação: python

Frameworks/Bibliotecas: Flask peewee
Banco de Dados: PostgreSQL

Outras Ferramentas: Git, Figma, Github vscode

🧱 Estrutura do Projeto
/database           → Banco de dados
  /models              → Tabelas
    geracao.py           → Historico populacional
    pedido.py            → Historico de pedidos
  database.py          → Configurações do orm
/routes             → Código-fonte principal
  documentacao.py      → Rota da pagina referente a documentação e funções agregadas
  home.py              → Rota da pagina referente a index e funções agregadas
  pedido.py            → Rota da pagina referente a pedido e funções agregadas
  sobre.py             → Rota da pagina referente a sobre e funções agregadas
/static       → Lógica de negócio e API
  /css                 → diretorio de textos css
    styles.css           → Classes CSS 
  /img                 →
    *                    → Backgrounds das intefaces web do projeto
  /scripts             → Codigos responsaveis pelo funcionamento do ag
   ACE.py                → Core do ag responsavel pelo gerencimento de rotinas
   ai.py                 → Consumo de api de llm
   genoma.py             → Responsavel pela elaboração direta dos trechos de codigo
   keywords.py           → Dicionarios de Sintaxe em formato placeholder para uso
   placeholder.py        → sistema auxiliar o placeholder temporario
/templates      → Interface do usuário
  documentacao.html    →documentação sobre o funcionamento do sistema
  index.html           →landpage e dashboard de resultados
  pedido.html          →entrada de parametos para geração de codigo
  sobre.html           →descrição sobre o projeto
main.py           →Core do projeto
config.py        →Configuração referentes ao servidor
ACE.db        → banco de dados
README.md        → Este arquivo
📄 Documentação
A documentação técnica e o relatório completo estão disponíveis na pasta /docs, incluindo:

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
