Migrador de Planilhas (CSV / Excel) <br>
<br>
Projeto em Python para leitura, validação e migração de dados a partir de planilhas nos formatos CSV e XLSX, com foco em organização de dados e tratamento de erros comuns de entrada
Este projeto foi criado para praticar e demonstrar:
<br>
<br>
Manipulação de arquivos CSV e Excel <br>
Uso da biblioteca Pandas para leitura e estruturação de dados <br>
Validação de formato de arquivos de entrada <br>
Tratamento de erros de parsing e inconsistências nos dados <br>
Organização de código para scripts de migração de dados <br>
<br>
Tecnologias Utilizadas <br>
    Python 3 <br>
    Pandas <br>
    OpenPyXL (leitura de arquivos Excel) <br>
   <br>
   
Estrutura do Projeto <br>
  migrador_de_planilhas/ <br>
  │ <br>
  ├── venv/                 # Ambiente virtual <br>
  ├── main.py               # Script principal <br>
  ├── data/                 # Arquivos de entrada
  │   ├── produtos.csv         # Exemplo de arquivo CSV
  │   └── produtos.xlsx 		# Exemplo de arquivo XLSX
  └── README.md             # Documentação do projeto <br>
<br>
Como Executar o Projeto <br>
 Criar o ambiente virtual <br>
  python -m venv venv <br>
 Ativar o ambiente virtual (Windows) <br>
  venv\Scripts\activate <br>
 <br>
Após ativar, o terminal exibirá (venv) no início da linha. <br>
 <br>
 Instalar as dependências <br>
  pip install pandas openpyxl <br>
 Executar o script <br>
  python main.py <br>
   <br>
 
  Diferença entre erros de lógica e erros de parsing  <br>
    Ao tentar a migração, como arquivos do excel vem padrão PT-BR, e números decimais são separados por vírgulas no Brasil acontece um conflito com a biblioteca PANDAS, onde uma virgula é considerado um separdor de colunas para o panda. Consegui contornar o erro fazendo com que a biblioteca ignore linhas mal formatadas<br>
  <br>
  Importância da validação de dados de entrada <br>
  Uso do Pandas como ferramenta padrão para manipulação de dados <br> 
  Estruturação de scripts de automação em Python <br>
