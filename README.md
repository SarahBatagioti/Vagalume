# 🌟 Vagalume
Vagalume é um agente inteligente que automatiza a busca e candidatura em vagas de emprego, iluminando novas oportunidades de forma rápida e eficiente.


> **vaga** + **lume** → clareza para quem busca recolocação no mercado ✨

## 🧠 Visão Geral
O Vagalume foi desenvolvido para facilitar a vida de quem está procurando emprego. Ele automatiza etapas essenciais do processo, economizando tempo e esforço para o usuário. O agente é capaz de:

- 🔍 Raspar dados do LinkedIn do usuário para obter informações profissionais.
- 🧭 Pesquisar vagas de emprego na internet de acordo com o cargo informado.
- 📝 Preencher automaticamente formulários de candidatura usando Selenium com os dados extraídos do LinkedIn.

## 🎨 Identidade Visual

O nome Vagalume surgiu da junção das palavras:

- Vaga (de emprego)
- Lume (luz, claridade)

Assim como o vagalume, o agente traz clareza e visibilidade para novas oportunidades no mercado de trabalho.

## 🗂️ Estrutura do Projeto
```
vagalume/
│
├── main.py               # Roda o agente Vagalume
├── Gradio_UI.py          # Interface com o usuário via Gradio
├── tools/                # Ferramentas principais
│   ├── linkedin_scraper.py    # Raspagem de dados do LinkedIn
│   ├── vaga_search.py         # Busca automatizada de vagas
│   ├── auto_apply.py          # Preenchimento automático de formulários
│   └── final_answer.py        # Geração da resposta final para o usuário
├── prompts.yaml          # Arquivo com prompts para o agente
├── README.md             # Este arquivo :)
```

## 🚀 Como usar
Clone este repositório:

```
git clone https://github.com/SarahBatagioti/Vagalume
```
```
cd vagalume
```

Instale as dependências:

```
pip install -r requirements.txt
```
Rode a interface:

```
python Gradio_UI.py
```
Siga as instruções da interface para iniciar sua busca por vagas.

## 📌 Requisitos

Python 3.8+
Selenium
Gradio
BeautifulSoup
YAML

## 🧑‍💻 Autoras
Feito com 💡 por **Sarah Montuani Batagioti** e **Marianne Valério Nunes** para matéria de **Interação Humano Computador** da **FATEC São José dos Campos - Prof. Jessen Vidal**.
