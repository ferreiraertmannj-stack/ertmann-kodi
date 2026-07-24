# Contributing

Obrigado por contribuir com o Ertmann Media Center. Nosso projeto é um fork profissional do Kodi, mantido em um monorepo que contém o código-fonte upstream do Kodi (`kodi-source/`) e nossos addons, skins e ferramentas.

## Regras de Ouro

1. **Nunca modifique o core do Kodi** além do estritamente necessário para branding (ver [FORK_STRATEGY.md](FORK_STRATEGY.md)).
2. Toda nova funcionalidade deve ser implementada como um **addon Python**, skin ou script independente.
3. Preservamos compatibilidade total com o ecossistema Kodi (Nexus e Omega).

## Branches

Crie branches curtas a partir de `main` e use um prefixo descritivo:

- `docs/` para documentação.
- `chore/` para infraestrutura, build e manutenção.
- `feature/` para novas funcionalidades em addons Ertmann.
- `fix/` para correções.
- `upstream/` reservado para sincronização com o Kodi upstream.

Exemplo: `feature/wizard-language-selection`.

## Commits

Mantenha commits pequenos, coesos e reversíveis. Use mensagens no formato:

```text
tipo(escopo): resumo objetivo
```

Exemplo: `fix(wizard): resolve language selection error`.

Explique no corpo do commit quando houver decisão de compatibilidade ou mudança arquitetural.

## Code style

- Use UTF-8, LF e newline final conforme `.editorconfig`.
- Siga PEP 8 para Python e use type hints quando aplicável. (Baseline: Python 3.10).
- Mantenha XML no formato oficial do Kodi.
- O código do `kodi-source/` deve seguir as regras de estilo do próprio Kodi (C++).

## Review

Abra um pull request com escopo limitado. Preencha o template, descreva a validação realizada e aguarde a revisão do code owner antes do merge.

## Releases

Releases usam Semantic Versioning modificado para alinhar com a versão do Kodi base. Consulte `VERSIONING.md` e `CHANGELOG.md` antes de preparar artefatos de distribuição.
