Migrador de Planilhas (CSV / Excel) 

---

### Projeto em Python para leitura, validação e migração de dados a partir de planilhas nos formatos CSV e XLSX, com foco em organização de dados e tratamento de erros comuns de entrada
Este projeto foi criado para praticar e demonstrar:

* Manipulação de arquivos CSV e Excel 
* Uso da biblioteca Pandas para leitura e estruturação de dados 
* Validação de formato de arquivos de entrada 
* Tratamento de erros de parsing e inconsistências nos dados 
* Organização de código para scripts de migração de dados
---
### Tecnologias Utilizadas 
   * Python 3 <br>
   * Pandas <br>
   * OpenPyXL (leitura de arquivos Excel) 
    
  ---
   
### Estrutura do Projeto 

---
 
```text
migrador_de_planilhas/
│
├── venv/                 # Ambiente virtual
├── data/                 # Arquivos de entrada
│   ├── dados.csv         # Exemplo de arquivo CSV
│   └── dados.xlsx        # Exemplo de arquivo Excel
│
├── main.py               # Script principal
└── README.md             # Documentação do projeto     # Documentação do projeto <br> ```
```
---
### Como Executar o Projeto 
---
* Criar o ambiente virtual 
* python -m venv venv <br>
* Ativar o ambiente virtual (Windows) 
* venv\Scripts\activate <br>
 *Após ativar, o terminal exibirá (venv) no início da linha. 
* Instalar as dependências 
* pip install pandas openpyxl 
* Executar o script 
* python main.py 
---

### Insigths
  Diferença entre erros de lógica e erros de parsing <br>
  Ao tentar a migração, como arquivos do excel vem padrão PT-BR, e números decimais são separados por vírgulas no Brasil acontece um conflito com a biblioteca PANDAS, onde uma virgula é considerado um separdor de colunas para o panda. <br>
Consegui contornar o erro fazendo com que a biblioteca ignore linhas mal formatadas <br>
  * Importância da validação de dados de entrada 
  * Uso do Pandas como ferramenta padrão para manipulação de dados 
  * Estruturação de scripts de automação em Python 
