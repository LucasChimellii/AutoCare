# 🚗 AutoCare - Sistema de Gestão para Estética Automotiva

![Django](https://img.shields.io/badge/Django-6.x-green?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Python](https://img.shields.io/badge/Python-3.14.2-yellow?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)

---

## 📌 Visão Geral do Sistema

O **AutoCare** é um sistema web full-stack desenvolvido em Django com foco em digitalizar e estruturar o fluxo operacional de estéticas automotivas.

Ele funciona como um **ERP leve especializado no setor automotivo**, centralizando todo o ciclo de atendimento:

- Cadastro de clientes
- Gestão de veículos
- Abertura e acompanhamento de serviços
- Registro visual de avarias
- Controle de status operacional

O sistema transforma processos manuais em um fluxo **digital, rastreável e auditável**.

---

## 🧠 Problema Resolvido

Em estéticas reais, existem dois gargalos principais:

### ❌ Falta de histórico confiável

Não existe registro estruturado do estado do veículo no momento da entrada.

### ❌ Desorganização operacional

Serviços são controlados manualmente, sem padronização ou rastreio central.

---

## ⚙️ Fluxo do Sistema

```mermaid
graph TD
A[Cliente] --> B[Cadastro de Veículo]
B --> C[Abertura de Ordem de Serviço]
C --> D[Check-in do Veículo]
D --> E[Upload de Fotos de Avaria]
E --> F[Execução do Serviço]
F --> G{Status}
G --> H[Em Análise]
G --> I[Em Execução]
G --> J[Finalizado]
J --> K[Histórico do Cliente]
```

---

## 🏗️ Arquitetura do Sistema

### 🧱 Modelagem de Dados

O sistema segue uma arquitetura relacional normalizada:

```
Cliente (1) ──── (N) Veículos
Veículo (1) ──── (N) Ordens de Serviço
Ordem de Serviço (1) ──── (N) Imagens de Inspeção
```

### 🔐 Características da arquitetura:

- Integridade referencial via Django ORM
- Histórico completo por veículo
- Escalabilidade horizontal do modelo

---

## 🧠 Regras de Negócio

### 🔎 Normalização de dados

- Placas padronizadas (uppercase + sanitização)
- Prevenção de duplicidade de registros de clientes

### 🛡️ Validação em múltiplas camadas

- Front-end: validação básica
- Back-end: regras no `Model.save()`
- Banco de dados: constraints e integridade relacional

### 📸 Registro de evidências

- Upload de múltiplas imagens no check-in
- Associação direta com a Ordem de Serviço

---

## 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** como banco principal.

### Por que PostgreSQL?

- Relacionamentos complexos (1:N, N:N)
- Alta confiabilidade de dados
- Escalabilidade para produção
- Compatibilidade com cloud (AWS, Render)

---

## 🌍 Ambiente Atual

⚠️ O sistema está em execução **100% local (ambiente de desenvolvimento)**.

Não há deploy em produção no momento.

---

## 🔐 Configuração do Ambiente

⚠️ O projeto depende de variáveis de ambiente **e requer PostgreSQL instalado e rodando localmente** antes da execução.

Sem o PostgreSQL configurado, o sistema não irá iniciar corretamente.

### 📌 Requisitos obrigatórios:

- Python 3.14+
- PostgreSQL instalado e em execução local
- Banco de dados criado (ex: `autocare`)
- Usuário configurado no PostgreSQL com permissões no banco

### 📄 `.env.example`

```env
DB_NAME=CHANGE ME
DB_USER=CHANGE ME
DB_PASSWORD=CHANGE ME
DB_HOST=CHANGE ME
DB_PORT=CHANGE ME
SECRET_KEY=CHANGE ME (SECRET KEY USE LINK: https://djecrety.ir/)
```

## 🚀 Execução Local

```bash
# Clonar repositório
git clone https://github.com/lucasvchimelli
cd AutoCare

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Rodar servidor
python manage.py runserver

abas: home (Cliente) e admin (Gerenciamento)
```

---

## 🧱 Arquitetura Técnica (Visão Sistema)

### 🔹 Backend

- Django (Monólito modular)
- ORM para abstração de banco
- Regras de negócio centralizadas no servidor

### 🔹 Banco de Dados

- PostgreSQL
- Modelo relacional normalizado

### 🔹 Frontend

- Django Templates
- UI responsiva para operação

---

## 📊 Possível evolução (arquitetura futura)

```mermaid
graph LR
A[Django Backend] --> B[API REST]
B --> C[Frontend Mobile]
B --> D[Dashboard Analytics]
A --> E[PostgreSQL]
A --> F[AWS S3 Storage]
A --> G[WhatsApp API]
```

---

## 📷 Screenshots do Sistema

Abaixo estão as principais telas do sistema AutoCare, demonstrando o fluxo completo de gestão.

---

### 🏠 Dashboard Administrativo

![Dashboard](docs/screens/admin_dashboard.png)

---

### 👤 Clientes

#### ➕ Cadastro de Cliente

![Add Client](docs/screens/admin_client_add.png)

#### 📋 Lista de Clientes

![Clients](docs/screens/admin_clients.png)

---

### 🚗 Veículos

#### ➕ Cadastro de Veículo

![Add Car](docs/screens/admin_car_add.png)

#### 📋 Lista de Veículos

![Cars](docs/screens/admin_cars.png)

---

### 🧾 Serviços

#### ➕ Cadastro de Serviço

![Add Service](docs/screens/admin_services_add.png)

#### 📋 Lista de Serviços

![Services](docs/screens/admin_services.png)

---

### 👤 Portal do Cliente 

#### 🏠 Tela do Cliente (consulta de status)

![Client Home](docs/screens/client_home.png)
