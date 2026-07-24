# Changelog

Todos os arquivos de changelog aderem ao formato [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
O versionamento deste fork é explicado em `VERSIONING.md`.

## [Unreleased]

### Changed
- Reestruturação arquitetural completa: transição de plataforma multi-repo para monorepo focado em fork oficial do Kodi.
- Nova estrutura de diretórios acomodando `kodi-source/`, `addons/`, `skins/`, `branding/`.
- Atualização da documentação (`README.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `FORK_STRATEGY.md`) para alinhar com a política de "modificação zero do core".

### Added
- Documento `FORK_STRATEGY.md` estabelecendo regras de sync, merge e modificação sobre o Kodi upstream.
- Scaffolding de repositórios para novos addons de manutenção, wizard, rede e log analyzer.

### Removed
- Referências e dependências à arquitetura do antigo "Core SDK" autônomo.
