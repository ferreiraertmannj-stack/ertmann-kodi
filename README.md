# Ertmann Kodi Platform

Repositório de governança, arquitetura e documentação da Ertmann Kodi
Platform.

## Escopo atual

Este repositório define as regras compartilhadas da plataforma construída sobre
o Kodi, sem modificar seu núcleo. Implementações funcionais devem viver nos
repositórios oficiais dedicados da organização Ertmann-Tech.

## Compatibilidade planejada

- Kodi Nexus (v20)
- Kodi Omega (v21)
- Windows
- Linux
- Android
- Android TV
- Fire TV
- LibreELEC
- CoreELEC

## Repositórios oficiais

```text
ertmann-kodi-platform        Governança e arquitetura da plataforma
ertmann-kodi-core            Core SDK reutilizável
ertmann-kodi-repository      Repositório oficial Kodi
ertmann-kodi-theme           Tema futuro
ertmann-kodi-wizard          Wizard futuro
ertmann-kodi-maintenance     Maintenance futuro
ertmann-kodi-network         Network Toolkit futuro
ertmann-kodi-log-analyzer    Log Analyzer futuro
```

## Estrutura local

```text
docs/                         Documentação de arquitetura e desenvolvimento
repository/                   Scaffold declarativo já criado, sem lógica
```

## Desenvolvimento

Consulte [a arquitetura](docs/architecture.md) e o
[guia de desenvolvimento](docs/development.md) antes de alterar qualquer
repositório.

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).
