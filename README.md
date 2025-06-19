<h1 align="center">🤖 Discord Bot Experiments - Projeto de Aprendizado em Python</h1>

<p align="center">
  <strong>Bem-vindo ao repositório do Discord Bot Experiments</strong>, um projeto pessoal desenvolvido para praticar programação com <strong>Python</strong> e a biblioteca <code>discord.py</code>. Neste repositório, exploro comandos, eventos e interações com bots no Discord de maneira divertida
</p>

<p align="center">
  <a href="https://shields.io"><img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue?style=flat-square" alt="Status: Em Desenvolvimento"></a>
</p>

<div align="center">

[![GitHub last commit](https://img.shields.io/github/last-commit/ruandd9/discord-bot-experiments?style=flat-square)](https://github.com/ruandd9/discord-bot-experiments/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/ruandd9/discord-bot-experiments?style=flat-square)](https://github.com/ruandd9/discord-bot-experiments)
</div>

---

<h2 align="center">📖 Sobre o Projeto</h2>

Este bot é um experimento pessoal para aprender a criar aplicações interativas com Python, usando a biblioteca <code>discord.py</code>. Ele inclui comandos básicos, eventos e interações modernas (slash commands), além de recursos como embeds e tarefas agendadas.

---

<h2 align="center">⚙️ Funcionalidades</h2>

- ✅ Comandos de texto (prefix `.`):
  - `.falar`: O bot repete o que você disser
  - `.somar`: Retorna a soma entre dois números
  - `.enviar_embed`: Envia uma embed com imagem e texto

- ✅ Slash Commands:
  - `/ola`: Envia uma mensagem privada de boas-vindas
  - `/selecionar_membro`: Menciona o membro escolhido com um comando interativo
---

<h2 align="center">💻 Tecnologias Utilizadas</h2>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/discord.py-5865F2?style=flat-square&logo=discord&logoColor=white" alt="discord.py"></a>
  <a href="#"><img src="https://img.shields.io/badge/dotenv-333333?style=flat-square&logo=dotenv&logoColor=white" alt="python-dotenv"></a>
</p>

- 🐍 **Python**: Linguagem principal do projeto
- 🧩 **discord.py**: Biblioteca para interação com a API do Discord
  
---

<h2 align="center">🛡️ Segurança</h2>

> ⚠️ **Importante:** Nunca inclua seu token de bot diretamente no código.  
> Este projeto utiliza um arquivo `.env` para armazenar o token de forma segura.

Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:

```env
DISCORD_TOKEN=seu_token_aqui
