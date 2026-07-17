# Arquitetura

## Princípios

- O Kodi não é alterado; os módulos usam somente APIs oficiais.
- Cada add-on é uma unidade independente, com identificador e manifesto
  próprios.
- Código compartilhado deve viver no Core SDK, dentro de `ertmann-kodi-core`.
- Dependências de execução devem ser declaradas no `addon.xml` do módulo que as
  utiliza.
- A compatibilidade mínima planejada é Kodi Nexus e Kodi Omega nas plataformas
  suportadas.

## Organização oficial

```text
Ertmann-Tech/
  ertmann-kodi-platform
  ertmann-kodi-core
  ertmann-kodi-repository
  ertmann-kodi-theme
  ertmann-kodi-wizard
  ertmann-kodi-maintenance
  ertmann-kodi-network
  ertmann-kodi-log-analyzer
```

## Responsabilidade da Platform

`ertmann-kodi-platform` mantém decisões de arquitetura, governança,
versionamento, contribuição e roadmap. Ele não deve receber implementação de
add-ons.

## Responsabilidade do Core

`script.ertmann.platform.core` pertence ao repositório `ertmann-kodi-core` e
fornece a biblioteca reutilizável para futuros add-ons.

## Regra de evolução

Antes de implementar qualquer módulo, confirme que o diretório local pertence
ao repositório oficial correspondente. Código não deve ser duplicado entre
repositórios.
