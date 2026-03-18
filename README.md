AutoCare - Sistema de Gestão para Estética Automotiva

O **AutoCare** é uma aplicação web desenvolvida em Python/Django para gerenciar o fluxo de trabalho em centros de detalhamento automotivo. O foco do projeto é a organização de ordens de serviço e a segurança jurídica através do registro de inspeção visual.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python 3+
- **Framework:** Django 6.0
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Manipulação de Imagens:** Pillow (Python Imaging Library)
- **Versionamento:** Git & GitHub

## Estrutura do Projeto
O sistema utiliza uma arquitetura relacional para conectar as entidades principais:
- **Clientes:** Cadastro de proprietários.
- **Veículos:** Vinculados aos clientes (Relação 1:N).
- **Serviços:** Controle de status, valores e datas.
- **Inspeção Visual:** Sistema de fotos de avarias acoplado à Ordem de Serviço via `InlineAdmin`.

## Funcionalidades Implementadas
- [x] **Gestão de Avarias:** Upload de múltiplas fotos no check-in do veículo.
- [x] **Painel Administrativo:** Customizado com filtros, buscas e tradução para PT-BR.
- [x] **Integridade de Dados:** Uso de `on_delete=models.CASCADE` para limpeza automática de registros órfãos.
- [x] **Localização:** Configuração de Timezone para registros precisos de entrada e saída.

## 🚀 Como Executar o Projeto
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv myenv`.
3. Ative o ambiente e instale o Django e o Pillow: `pip install django pillow`.
4. Execute as migrações: `python manage.py migrate`.
5. Inicie o servidor: `python manage.py runserver`.

---
*Projeto desenvolvido por Lucas Vinicius Chimelli] como parte dos estudos de Desenvolvimento.*
