# Barber-shop-terminal-bot
MVP de bot pra barbearia em Python. Agenda horários, mostra preços e valida lógica antes da API.
# 💈 Bot Barbearia - MVP Terminal

> Lógica de autoatendimento pra barbearia. Agenda horários, mostra preços e não deixa cliente no vácuo.

[[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

## 🎯 Sobre o Projeto

MVP funcional da lógica de um chatbot de barbearia. Simula atendimento no terminal pra validar o fluxo antes de integrar com WhatsApp API.

**Problema que resolve:** Testar toda regra de negócio sem gastar com API ou servidor. O barbeiro consegue validar se o fluxo atende antes de investir.

## ⚔️ Funcionalidades

1. **Menu Automático**: Responde "oi" e inicia conversa
2. **Agendamento Inteligente**: Mostra horários, confirma e remove da lista pra evitar conflito duplo
3. **Consulta de Preços**: Responde valor de corte R$15, barba R$30, combo R$45
4. **Tratamento de Erro**: Não quebra se cliente digitar besteira ou pedir horário inexistente
5. **Loop de Atendimento**: Fica 24h rodando até digitar "sair"
6. Feito 100% no Celular usando Acode.

## 🚀 Como Executar

```bash
python bot_barbeiro.py
