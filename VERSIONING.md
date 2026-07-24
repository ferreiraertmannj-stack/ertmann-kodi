# Versionamento

O Ertmann Media Center utiliza um modelo de versionamento baseado no Kodi upstream, combinado com um identificador de build interno.

## Formato

O formato oficial de versão para binários e releases é:

```text
MAJOR.MINOR.PATCH-ertmann.BUILD
```

- `MAJOR.MINOR.PATCH`: Reflete exatamente a versão do Kodi upstream que serve de base. (Ex: `21.3.0` para Omega).
- `-ertmann.`: Sufixo identificador do fork.
- `BUILD`: Número sequencial (incrementado a cada release da Ertmann Tech na mesma versão do Kodi).

**Exemplo:**
`21.3.0-ertmann.1` (Kodi Omega 21.3.0, primeiro build estável da Ertmann Tech).

## Versionamento de Addons

Cada addon Ertmann (em `addons/` ou `skins/`) possui seu próprio versionamento no formato Semantic Versioning (`MAJOR.MINOR.PATCH`), independente do release principal do media center.

A versão de cada addon é declarada em seu respectivo `addon.xml`.

## Ciclo de Release

1. **Alpha/Beta**: `21.3.0-ertmann.1-beta`
2. **Stable**: `21.3.0-ertmann.1`
3. **Hotfix**: `21.3.0-ertmann.2` (se o Kodi base não mudou) ou `21.3.1-ertmann.1` (se o Kodi upstream lançou uma minor).

Para as regras de sincronização e atualização de versão, consulte o documento [FORK_STRATEGY.md](FORK_STRATEGY.md).
