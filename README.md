# Net Checker — Branch Develop 🛠️

Este repositório contém a suíte de ferramentas de diagnósticos básicos de rede e validação de endereços escrita em **Python**.

Esta branch (`develop`) contém o código-fonte principal em desenvolvimento, estrutura de testes e guias de contribuição.

---

## 📋 Funcionalidades em Desenvolvimento

- [x] Validar formato de endereços IP (IPv4 e IPv6).
- [x] Testar resposta a comandos `ping` em lista de hosts.
- [x] Exibir tabela formatada com status (`ONLINE` / `OFFLINE`).

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.8+** instalado.
- Conexão de rede ativa.

### Passo a Passo

1. Garanta que está na branch `develop`:
   ```bash
   git checkout develop
   ```

2. Certifique-se de que o arquivo `hosts.txt` existe com a lista de IPs/domínios desejados:
   ```text
   8.8.8.8
   1.1.1.1
   google.com
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

---
