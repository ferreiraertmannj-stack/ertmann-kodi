# Ertmann Media Center

Fork profissional do Kodi mantido pela Ertmann Tech. Este repositório contém o
código-fonte do Kodi com branding Ertmann, addons oficiais, skin
personalizada e ferramentas adicionais.

## Filosofia

- Reutilizar toda a infraestrutura do Kodi.
- Nunca reimplementar funcionalidades que o Kodi já oferece.
- Modificar o core apenas quando estritamente necessário.
- Toda funcionalidade nova deve ser implementada como addon, skin, script ou
  configuração.
- Preservar compatibilidade total com o ecossistema Kodi.

## Compatibilidade

- Kodi Omega (v21)
- Kodi Nexus (v20)
- Windows, Linux, Android, Android TV, Fire TV
- LibreELEC, CoreELEC
- Addons, skins e repositórios oficiais do Kodi

## Estrutura do projeto

```text
kodi-source/        Fork oficial do Kodi (upstream: xbmc/xbmc)
addons/             Addons Ertmann (Python)
skins/              Skins Ertmann
branding/           Assets visuais (splash, ícones, logos)
repository/         Metadados do repositório Kodi Ertmann
scripts/            Automação de build e empacotamento
build/              Configurações de build por plataforma
tools/              Ferramentas de desenvolvimento
docs/               Documentação de arquitetura e desenvolvimento
```

## Documentação

- [Estratégia do fork](FORK_STRATEGY.md)
- [Arquitetura](docs/architecture.md)
- [Desenvolvimento](docs/development.md)
- [Roadmap](ROADMAP.md)
- [Contribuição](CONTRIBUTING.md)
- [Versionamento](VERSIONING.md)
- [Segurança](SECURITY.md)

## Licença

O fork do Kodi é distribuído sob a
[GNU General Public License v2.0 or later](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html),
conforme a licença original do Kodi.

Os addons Python da Ertmann Tech são distribuídos sob a
[Licença MIT](LICENSE) quando não incorporam código GPL.
