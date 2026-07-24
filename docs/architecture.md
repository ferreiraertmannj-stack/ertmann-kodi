# Arquitetura

## Visão geral

O Ertmann Media Center é um fork profissional do Kodi. A arquitetura consiste
em três camadas:

1. **Kodi core** — código C++ do Kodi, modificado apenas para branding.
2. **Addons Ertmann** — funcionalidades implementadas como addons Python.
3. **Infraestrutura** — repositório, branding, build e automação.

## Princípios

- O core do Kodi não é alterado além do branding.
- Toda funcionalidade nova é um addon, skin, script ou configuração.
- Compatibilidade com addons, skins e repositórios existentes é obrigatória.
- APIs do Kodi (Python, JSON-RPC, binary addons) nunca são modificadas.
- O fork deve ser atualizável para novas versões do Kodi com conflitos
  mínimos.

## Estrutura do fork

```text
ertmann-kodi-platatform/
├── kodi-source/                Fork do Kodi (upstream: xbmc/xbmc)
│   ├── version.txt             ★ Branding Ertmann
│   ├── media/                  ★ Assets visuais Ertmann
│   ├── system/addon-manifest   ★ Addons Ertmann bundled
│   └── (demais arquivos)       Inalterados
├── addons/                     Addons Python Ertmann
├── skins/                      Skins Ertmann
├── branding/                   Assets de branding
├── repository/                 Metadados do repositório Kodi
├── scripts/                    Automação
├── build/                      Configurações de build
├── tools/                      Ferramentas de desenvolvimento
└── docs/                       Documentação
```

## Camada Kodi core

O Kodi fornece toda a infraestrutura de reprodução de mídia, GUI, addons,
skins, protocolos de rede, banco de dados e multiplataforma. O fork modifica
apenas:

- `version.txt` — identidade da aplicação.
- `media/` — splash screen e ícones.
- `system/addon-manifest.xml` — addons pré-instalados.

## Camada Addons Ertmann

Cada addon Ertmann é um add-on Python padrão do Kodi com `addon.xml` próprio:

| Addon | Tipo | Função |
| --- | --- | --- |
| `repository.ertmann` | `xbmc.addon.repository` | Repositório oficial |
| `script.ertmann.wizard` | `xbmc.python.script` | Configuração guiada |
| `script.ertmann.maintenance` | `xbmc.python.script` | Manutenção |
| `script.ertmann.network` | `xbmc.python.script` | Diagnóstico de rede |
| `script.ertmann.loganalyzer` | `xbmc.python.script` | Análise de logs |
| `skin.ertmann` | `xbmc.gui.skin` | Skin personalizada |

## Camada Infraestrutura

- **Repositório**: hosting HTTPS de addons com `addons.xml` e checksums.
- **Build**: CMake do Kodi com branding Ertmann aplicado.
- **CI/CD**: GitHub Actions para validação, empacotamento e publicação.

## Regras de evolução

- Consulte `FORK_STRATEGY.md` antes de qualquer alteração no core.
- Addons devem usar somente APIs oficiais do Kodi.
- Novas dependências requerem justificativa e aprovação.
- Código Python deve ser compatível com Python 3.10 ou superior.
