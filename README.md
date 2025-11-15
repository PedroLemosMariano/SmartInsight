# 🧠 GatsBI – Sistema Inteligente de Análise de Dados Empresariais

O **GatsBI** é uma plataforma interativa desenvolvida em **Python** que permite importar, visualizar e analisar dados empresariais de forma automatizada e inteligente.  
Com suporte a gráficos dinâmicos, relatórios automáticos e geração de *insights* com IA, o sistema auxilia analistas e gestores a tomarem decisões mais assertivas com base em dados reais.

---

## 🚀 Funcionalidades Principais

- 🔐 **Autenticação de usuários** – login e gerenciamento de dados individuais.  
- 📂 **Importação de dados** – upload de arquivos `.csv` ou `.xlsx`.  
- 📊 **Visualização interativa** – criação automática de gráficos com Plotly/Altair.  
- 🤖 **Geração de insights automáticos** – uso de IA para interpretar tendências e anomalias.  
- 📑 **Exportação de relatórios** – geração de relatórios em PDF ou Excel.  
- ⚙️ **Integração com banco de dados PostgreSQL** – armazenamento estruturado e seguro.  

---

## 🧩 Arquitetura do Projeto

| Diretório / Arquivo | Descrição |
|----------------------|------------|
| **SMTH/** | Diretório raiz do projeto |
| ├── **app/** | Contém os módulos principais da aplicação |
| │ ├── `main.py` | Ponto de entrada da aplicação (Flask) |
| │ ├── `dashboard.py` | Visualização de gráficos e relatórios |
| │ ├── `insights.py` | Geração automática de insights com IA |
| │ ├── `upload.py` | Upload e validação de datasets |
| │ ├── `export.py` | Exportação de relatórios em PDF/Excel |
| │ └── **utils/** | Funções auxiliares e utilitárias |
| │ &nbsp;&nbsp;&nbsp;&nbsp;├── `db.py` | Conexão e operações com PostgreSQL |
| │ &nbsp;&nbsp;&nbsp;&nbsp;├── `charts.py` | Criação de gráficos dinâmicos |
| │ &nbsp;&nbsp;&nbsp;&nbsp;└── `preprocess.py` | Limpeza e padronização dos dados |
| **data/** | Armazena datasets temporários |
| **requirements.txt** | Lista de dependências do projeto |
| **README.md** | Documentação principal do repositório |

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|------------|-------------|
| **Linguagem** | Python 3.11+ |
| **Interface** | Flask |
| **Banco de Dados** | PostgreSQL |
| **Análise de Dados** | Pandas, NumPy |
| **Visualização** | Plotly, Altair |
| **Relatórios** | ReportLab, Pandas ExcelWriter |
| **IA / NLP** | OpenAI API ou Transformers (opcional) |

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/PedroLemosMariano/SmartInsight.git
cd SmartInsight
```

### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados
DB_HOST=localhost
DB_NAME=smartinsight
DB_USER=postgres
DB_PASS=sua_senha
DB_PORT=5432

### 5️⃣ Executar o sistema
```bash
Flask run app/main.py
```

---

## 📈 Exemplo de Uso
1. Faça login no sistema.
2. Faça upload de um arquivo de vendas (vendas.csv).
3. O SmartInsight gera automaticamente gráficos de desempenho.
4. Clique em "Gerar Insights" para obter uma análise textual com IA.
5. Exporte o relatório completo em PDF ou Excel.

---

## 💡 Exemplos de Insights Automáticos

- "As vendas no setor Sul aumentaram 22% em setembro, impulsionadas pelo novo produto lançado no início do mês."
- "O faturamento total caiu 8% em outubro, principalmente devido à queda nas vendas da categoria eletrônicos."

---

## 🧠 Estrutura do Banco de Dados (modelo simplificado)

### Tabela usuarios
```
Campo	Tipo	Descrição
id	SERIAL PK	Identificador único
nome	VARCHAR(100)	Nome do usuário
email	VARCHAR(150)	Email para login
senha	TEXT	Senha criptografada
```

### Tabela datasets
```
Campo	Tipo	Descrição
id	SERIAL PK	Identificador do dataset
usuario_id	FK → usuarios.id	Dono do arquivo
nome_arquivo	VARCHAR(200)	Nome do arquivo enviado
caminho	TEXT	Caminho do arquivo armazenado
data_upload	TIMESTAMP	Data de envio
 ```

---

## 🧭 Roadmap

 - Estrutura inicial do projeto
 - Upload e leitura de dados
 - Visualização de gráficos
 - Geração de insights automáticos com IA
 - Exportação em PDF/Excel
 - Sistema de login completo
 - Dashboard multiusuário


---

## CONTATOS
📧 Email [pedro.lemosmariano@gmail.com]

🔗 LinkedIn [https://www.linkedin.com/in/pedrolemosmariano/]
