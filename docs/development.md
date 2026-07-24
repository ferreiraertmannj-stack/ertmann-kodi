# Desenvolvimento

## Pré-requisitos

- Kodi Nexus ou Omega instalado para testes de addons.
- Python 3.10 ou superior para ferramentas de qualidade.
- Git 2.30 ou superior.
- CMD (Command Prompt) para comandos Git.
- Visual Studio (Windows) ou GCC/Clang (Linux) para build do Kodi.

## Ambiente local

Crie o ambiente Python para ferramentas de qualidade:

```cmd
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
```

## Estrutura de trabalho

O workspace contém o fork do Kodi e os componentes Ertmann:

```text
kodi-source/    O código do Kodi. Não modifique além do branding.
addons/         Addons Ertmann. Desenvolvimento principal aqui.
skins/          Skins Ertmann.
branding/       Assets visuais.
```

## Validação

### Addons Python

```cmd
python -m py_compile addons\script.ertmann.maintenance\default.py
.venv\Scripts\ruff check addons\
```

### Manifesto XML

Valide `addon.xml` de cada addon antes do commit.

### Build do Kodi

Consulte a documentação oficial do Kodi para build por plataforma. O build
do fork utiliza o mesmo CMake, apenas com `version.txt` alterado.

## Convenções

- Siga PEP 8 para Python. Use type hints quando aplicável.
- Mantenha XML no formato oficial do Kodi.
- Código Python deve funcionar com Python 3.10 (Kodi Nexus).
- Não inclua dependências externas sem justificativa.
- Nunca modifique o core do Kodi sem aprovação e documentação.
- Nunca execute `git push` automaticamente.
- Use commits pequenos no formato: `tipo(escopo): resumo`.

## Git

Utilize CMD para todos os comandos Git:

```cmd
git add .
git commit -m "tipo(escopo): resumo"
git status
```

Nunca utilize PowerShell para Git neste projeto.
