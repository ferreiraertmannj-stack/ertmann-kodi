# Desenvolvimento

## Pré-requisitos

- Kodi Nexus ou Omega para testes manuais futuros.
- Python 3 para ferramentas locais de qualidade quando houver código Python.
- CMD (Command Prompt) para comandos Windows.

## Ambiente local

Quando Python estiver instalado, crie o ambiente local usando CMD:

```cmd
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
```

## Validação atual

Este repositório não deve conter implementação funcional de add-ons. A validação
normal é documental e estrutural:

```cmd
git diff --check
git status
```

Nos repositórios com Python, execute os testes e validações do próprio módulo.
Exemplo para o Core:

```cmd
python -m unittest discover -s tests
python -m compileall script.ertmann.platform.core tests
```

## Convenções

- Siga PEP 8 em código Python.
- Use tipagem quando a API do Kodi e o contexto permitirem.
- Não inclua dependências de execução sem justificativa e declaração no
  manifesto do módulo.
- Evite comentários que apenas repitam o código.
- Nunca execute `git push` automaticamente.
