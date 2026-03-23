# 🚗 AutoCare - Sistema de Gestão para Estética Automotiva

> 🚧 **Status:** Em desenvolvimento (Fase de aprimoramento de UI/UX e regras de negócio).

O **AutoCare** é uma aplicação web desenvolvida com Django (full-stack) para modernizar e gerenciar o fluxo de trabalho em centros de detalhamento automotivo e oficinas. 

O foco da arquitetura é resolver dois problemas reais do negócio: **segurança jurídica** (através do registro fotográfico no check-in do veículo) e **experiência do cliente** (rastreio do status do serviço em tempo real).

## 🛠️ Stack Tecnológica

**Atualmente em Desenvolvimento (MVP):**
* **Back-end:** Python 3, Django
* **Front-end:** HTML5, CSS3, Bootstrap 5 (Design Responsivo)
* **Banco de Dados:** SQLite (ambiente de desenvolvimento)
* **Manipulação de Mídia:** Pillow (Python Imaging Library)
* **Controle de Versão:** Git & GitHub

**Arquitetura Futura (Roadmap):**
* **Banco de Dados Relacional:** Migração estruturada para **PostgreSQL**.
* **Deploy Cloud:** Hospedagem em nuvem (Render/Heroku) e armazenamento de estáticos/mídia na AWS S3.
* **Automação:** Integração com API de mensageria (WhatsApp) para notificação automática de status aos clientes.

## ⚙️ Funcionalidades Já Implementadas

### 1. Motor de Busca Inteligente e Sanitização
* **UX à prova de falhas:** Implementação de algoritmo na *View* que ignora traços, espaços e formatações incorretas digitadas pelo usuário na busca de placas.
* **Defesa em Profundidade (Database):** Sobrescrita do método `save()` nos *Models* para garantir que os dados entrem no banco padronizados (maiúsculas, sem caracteres especiais), prevenindo corrupção de dados.
* **Validação de Front-end:** Uso de atributos HTML nativos (`maxlength`, `oninput`) para bloquear inputs inválidos na raiz.

### 2. Gestão de Avarias e Inspeção Visual
* Upload de múltiplas fotos no momento do check-in do veículo.
* Sistema acoplado à Ordem de Serviço via `InlineAdmin`, garantindo resguardo do prestador de serviço.

### 3. Modelagem de Dados Relacional
* Arquitetura de banco de dados conectando **Clientes**, **Veículos** (Relação 1:N) e **Serviços**.
* Integridade referencial utilizando `on_delete=models.CASCADE` para limpeza automática de registros órfãos.

### 4. Painel Administrativo Customizado
* Área de gestão customizada com filtros nativos, barras de pesquisa e localização total para PT-BR (Timezone e Language).

## 🚀 Como Executar o Projeto Localmente

```bash
# Clone o repositório
git clone https://github.com/LucasChimellii/AutoCare.git
cd AutoCare

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver

## 👨‍💻 Autor

**Lucas Vinicius Chimelli Corrêa**  
🔗 https://github.com/LucasChimellii
