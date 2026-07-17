# Contributing

Obrigado por contribuir com a Ertmann Kodi Platform. A plataforma é construída
sobre o Kodi e não modifica seu código-fonte. Toda contribuição deve usar
somente APIs oficiais e preservar compatibilidade com Kodi Nexus e Omega.

## Branches

Crie branches curtas a partir de `main` e use um prefixo descritivo:

- `docs/` para documentação.
- `chore/` para infraestrutura e manutenção do repositório.
- `feature/` para funcionalidades aprovadas.
- `fix/` para correções aprovadas.

Exemplo: `chore/repository-metadata`.

## Commits

Mantenha commits pequenos, coesos e reversíveis. Use mensagens no formato:

```text
tipo(escopo): resumo objetivo
```

Exemplo: `docs(repository): explain release flow`.

Explique no corpo do commit quando houver decisão de compatibilidade, segurança
ou mudança de arquitetura.

## Code style

- Use UTF-8, LF e newline final conforme `.editorconfig`.
- Siga PEP 8 para Python e use type hints quando aplicável.
- Mantenha XML no formato oficial do Kodi.
- Evite dependências externas sem justificativa e aprovação.
- Não implemente funcionalidades fora do escopo aprovado.

## Review

Abra um pull request com escopo limitado. Preencha o template, descreva a
validação realizada e aguarde a revisão do code owner antes do merge.

## Releases

Releases usam Semantic Versioning e tags Git assinadas. Consulte
`VERSIONING.md`, `CHANGELOG.md` e `repository/docs/github-actions.md` antes de
preparar artefatos de distribuição.
