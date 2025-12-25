# 📄 Gerador de Currículo em PDF no Padrão ABNT

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![FPDF](https://img.shields.io/badge/FPDF-PDF%20Generator-green.svg)
![License](https://img.shields.io/github/license/Mateus-Caique-Py/Gerador_Curriculo)
![Last Commit](https://img.shields.io/github/last-commit/Mateus-Caique-Py/Gerador_Curriculo)
![Repo Size](https://img.shields.io/github/repo-size/Mateus-Caique-Py/Gerador_Curriculo)
![Stars](https://img.shields.io/github/stars/Mateus-Caique-Py/Gerador_Curriculo?style=social)

Este projeto é um **gerador automático de currículos profissionais em formato PDF**, estruturado de acordo com as **normas ABNT**, desenvolvido em **Python** utilizando a biblioteca **FPDF**.

O objetivo é fornecer um modelo de currículo limpo, profissional, padronizado e facilmente customizável, ideal para uso acadêmico ou profissional.

---

## ✨ Funcionalidades

- Geração automática de currículo em **PDF**
- Layout formatado conforme **normas ABNT**
  - Margem superior e esquerda: **3 cm**
  - Margem inferior e direita: **2 cm**
- Cabeçalho centralizado com nome e contatos
- Seções bem definidas:
  - Resumo Profissional
  - Formação Acadêmica
  - Experiência Profissional
  - Especializações e Competências
  - Habilidades Técnicas
  - Cursos e Certificações
  - Informações Adicionais
- Rodapé com **numeração automática de páginas**
- Código documentado com **Docstrings padrão PEP 257**
- Estrutura simples e de fácil manutenção

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **FPDF** — biblioteca para geração de arquivos PDF

---

## 📦 Requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado e instale a dependência necessária:

```bash
pip install fpdf
```

## ▶️ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/Mateus-Caique-Py/Gerador_Curriculo.git

```
2. Acesse o diretório do projeto:

```bash
cd SEU_REPOSITORIO

```
3. Execute o script:

```bash
cd SEU_REPOSITORIO

```
4. O currículo será gerado automaticamente:

```text
curriculo_petshop_exemplo.pdf

```
## 🧩 Personalização do Currículo

Toda a personalização pode ser feita diretamente no arquivo curriculo_abnt.py.

Você pode alterar facilmente:

  Nome e informações de contato

  Resumo profissional

  Formação acadêmica

  Experiência profissional

  Habilidades, cursos e certificações

Cada seção está claramente separada no código, tornando a manutenção simples e intuitiva.

## 📚 Padrões e Boas Práticas

  Docstrings seguindo o PEP 257

  Código organizado e bem documentado

  Separação lógica das seções do currículo

  Tratamento de caracteres especiais usando codificação latin-1

  Classe personalizada estendendo FPDF para rodapé e paginação

## 👤 Autor

Desenvolvido por Mateus Caique

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório!

