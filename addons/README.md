# Ertmann Addons

Add-ons oficiais da Ertmann Tech para o Kodi. Cada subdiretório contém um
add-on Python independente, instalável pelo repositório Ertmann ou bundled no
fork.

## Estrutura planejada

```text
addons/
  repository.ertmann/           Repositório oficial Ertmann
  script.ertmann.maintenance/   Ferramentas de manutenção
  script.ertmann.wizard/        Configuração guiada
  script.ertmann.network/       Diagnóstico de rede
  script.ertmann.loganalyzer/   Análise de logs
```

## Convenções

- Cada add-on possui seu próprio `addon.xml` com `id`, `version` e `requires`.
- Use somente APIs oficiais do Kodi (`xbmc`, `xbmcgui`, `xbmcaddon`, `xbmcvfs`).
- Compatibilidade mínima: Kodi Nexus (v20) e Omega (v21).
- Código Python 3.10+ (baseline do Kodi Nexus).
