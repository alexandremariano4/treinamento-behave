# Treinamento de Selenium com Behave

Projeto de automação de testes BDD (Behavior-Driven Development) utilizando **Behave** e **Selenium WebDriver** para testar o fluxo de cadastro de entregadores na plataforma **Buger Eats**.

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução dos Testes](#execução-dos-testes)
- [Estrutura BDD](#estrutura-bdd)
- [Page Objects](#page-objects)
- [Selenium Grid](#selenium-grid)
- [Relatórios](#relatórios)

---

## 🎯 Visão Geral

Este projeto testa o fluxo de **cadastro de novos entregadores** na plataforma Buger Eats, validando:

✅ **Cadastro com sucesso** - Preenchimento correto do formulário
❌ **Validações de dados inválidos** - CPF, nome, endereço
⚠️ **Validações de campo** - Email com popup de validação

**URL da Aplicação:** `https://buger-eats.vercel.app/`

---

## 📁 Estrutura do Projeto

```
modulos-3-4/
├── features/
│   ├── frontend/
│   │   └── cadastro.feature          # Cenários BDD em português
│   ├── steps/
│   │   ├── cadastro_sucesso.py       # Steps para cenários de sucesso
│   │    └── cadastro_falha.py         # Steps para cenários de falha
│   └── environment.py                    # Hooks do Behave (setup/teardown)
├── pages/
│   ├── HomePage.py                   # Page Object da página inicial
│   └── DeliveryPage.py               # Page Object do formulário de entrega
├── fixtures/
│   ├── browser/
│   │   └── driver.py                 # Configuração do Selenium WebDriver
│   └── func/
│       └── functions.py              # Funções utilitárias de interação
├── docker/
│   └── docker-compose.yml            # Configuração do Selenium Grid
├── behave.ini                        # Configuração do Behave
├── requirements.txt                  # Dependências Python
└── README.md                         # Este arquivo
```

---

## 🔧 Pré-requisitos

- **Python 3.8+**
- **Git**
- **Docker** (para usar Selenium Grid)
- **Chrome/Chromium** (para execução local)

---

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/alexandremariano4/treinamento-behave.git

cd treinamento-behave
```

### 2. Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

**Principais dependências:**
- `behave==1.3.3` - Framework BDD
- `selenium==4.39.0` - Automação de testes
- `behavex==4.6.0` - Relatórios HTML para Behave
- `allure-python-commons==2.15.2` - Integração com Allure Reports

---

## ⚙️ Configuração

### 1. Arquivo `behave.ini`

Define configurações globais do Behave:

```ini
[behave.userdata]
BASE_URL = https://buger-eats.vercel.app/

[behave]
lang = pt                    # Idioma: português
color = True                 # Saída colorida no terminal
stop = False                 # Continua mesmo após falhas
quiet = True                 # Saída reduzida
summary = True               # Resumo ao final
log_capture = True           # Captura logs
show_timings = True          # Mostra tempo de execução
```

### 2. Arquivo `environment.py`

Define hooks (setup/teardown) do Behave:

```python
def before_all(context):
    # Inicializa driver do Selenium
    context.brw = get_driver()
    
    # Aliases para comandos frequentes
    context.click = commands.click
    context.type = commands.send_keys
    context.validate_text = commands.validate_text
    context.validate_popup = commands.validate_popup_message
    
    # Page Objects
    context.homePage = homePage
    context.deliveryPage = deliveryPage

def after_all(context):
    # Finaliza navegador
    context.brw.quit()

def after_step(context, step):
    # Captura screenshot em caso de falha
    if step.status.name != 'passed':
        # Salva em: screenshots/<nome_cenario>/<nome_step>.png
        context.brw.save_screenshot(...)
```

---

## 🚀 Execução dos Testes

### Rodar todos os testes

```bash
behave
```

### Rodar por tag

```bash
# Apenas testes de sucesso
behave --tags=@success

# Apenas testes de falha
behave --tags=@failure

# Testes de validação de email
behave --tags=@email

# Testes de popup
behave --tags=@popup
```

### Rodar cenário específico

```bash
behave features/frontend/cadastro.feature -n "Cadastro de um novo entregador na plataforma com sucesso"
```

---

## 🎭 Estrutura BDD

### Arquivo: `features/frontend/cadastro.feature`

Escrito em **Gherkin** com linguagem em **português**:

```gherkin
Funcionalidade: Cadastrar novo entregador para o Buger Eats

    @success
    Esquema do Cenário: Cadastro de um novo entregador com sucesso
        Dado Está na tela principal do sistema
        E Clicar no botão "Cadastre-se para fazer entregas"
        Quando Preenche o formulário de Cadastro
        E Envia a imagem da CNH
        Então Deve ser exibido uma mensagem de sucesso "<result>"
```

**Tags disponíveis:**
- `@success` - Fluxo feliz
- `@failure` - Validações de erro
- `@email` - Validação de email
- `@cpf` - Validação de CPF
- `@popup` - Popup de validação HTML5

---

## 📄 Page Objects

### HomePage.py

Encapsula elementos e ações da página inicial:

```python
def validate_title(context):
    """Acessa a URL base e valida título"""
    context.brw.get(context.config.userdata.get('BASE_URL'))

def signup_button(context, text):
    """Clica no botão de cadastro"""
    context.click(f'//strong[text()="{text}"]', 'xpath')
```

### DeliveryPage.py

Encapsula elementos do formulário de entrega:

```python
def fillForm(context):
    """Preenche todos os campos do formulário"""
    # nome, cpf, email, phone, cep, number, complement, delivery_method

def sendCnhImage(context):
    """Envia imagem da CNH"""

def successMessage(context, text):
    """Valida mensagem de sucesso"""

def alertError(context, text):
    """Valida mensagem de erro em alert"""

def validatePopUpMessage(context, text):
    """Valida popup de validação HTML5"""
```

---

## 🐳 Selenium Grid (Docker)

### Iniciar o Selenium Grid com Docker Compose

```bash
docker-compose -f docker/docker-compose.yml up -d
```

**Serviços iniciados:**
- **Selenium Hub** em `http://localhost:4444`
- **Chrome Node** para execução de testes

### Parar os serviços

```bash
docker-compose -f docker/docker-compose.yml down
```

### Configurar URL do Hub

O driver está configurado para conectar em `http://192.168.15.5:4444` ou via variável de ambiente:

```bash
set SELENIUM_HUB_URL=http://localhost:4444
behave
```

---

## 📊 Relatórios

### BehaveX (HTML Report)

Gerado automaticamente em `output/report.html`

```bash
behavex
```

### Estrutura de saída

```
output/
├── report.html              # Relatório principal
├── report.json              # Dados em JSON
├── overall_status.json      # Status geral
└── behave/                  # Arquivos auxiliares
    └── behave.tags          # Tags encontradas
```

### Screenshots de falhas

Capturados automaticamente em:

```
screenshots/
└── <Nome_Cenario>/
    └── <Step_que_falhou>.png
```

---

## 🛠️ Ferramentas e Dependências Principais

| Ferramenta | Versão | Propósito |
|-----------|--------|-----------|
| Selenium | 4.39.0 | Automação de navegador |
| Behave | 1.3.3 | Framework BDD |
| BehaveX | 4.6.0 | Relatórios HTML |
| Chrome Driver | - | Driver do Chrome |
| IPython | 9.8.0 | Debug interativo |

---

## 🐛 Troubleshooting

### Erro: "Could not start a new session"

**Causa:** Capabilities inválidas ou incompatíveis com o hub

**Solução:** Verificar arquivo `driver.py` - deve conter apenas `browserName: chrome`

### Erro: "Session not created"

**Causa:** Hub do Selenium não está rodando

**Solução:**
```bash
# Verificar se está rodando
docker ps | grep selenium

# Iniciar se parado
docker-compose -f docker/docker-compose.yml up -d
```

### Screenshots não aparecem

**Verificar:** Pasta `screenshots/` foi criada? Permissões de escrita?

---

## 📝 Exemplo de Execução

```bash
# Terminal 1: Inicia Selenium Grid
docker-compose -f docker/docker-compose.yml up

# Terminal 2: Executa testes
behave --tags=@success

# Resultado esperado:
# Feature: Cadastrar novo entregador para o Buger Eats
#   Scenario: Cadastro de um novo entregador com sucesso
#     Given Está na tela principal do sistema ... passed
#     And Clicar no botão "Cadastre-se para fazer entregas" ... passed
#     When Preenche o formulário de Cadastro ... passed
#     And Envia a imagem da CNH ... passed
#     Then Deve ser exibido uma mensagem de sucesso ... passed
```

---

## 📚 Referências

- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
- [Selenium Grid](https://www.selenium.dev/documentation/grid/)

---

**Desenvolvido por**: Alexandre Mariano

Última atualização: **29/12/2025**