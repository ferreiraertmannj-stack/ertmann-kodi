# Fluxo planejado para GitHub Actions

Nenhuma GitHub Action foi criada nesta etapa. Este documento define o fluxo
que será implementado após aprovação.

```text
Commit
  ↓
Tag
  ↓
Release
  ↓
ZIP
  ↓
Atualização do repositório
```

## Etapas futuras

1. Um commit aprovado atualiza um add-on ou a infraestrutura do repositório.
2. Uma tag assinada identifica a versão que será publicada.
3. A release do GitHub registra a versão, as notas e os artefatos.
4. A automação valida XML e versões, então gera o ZIP do add-on.
5. A automação atualiza `addons.xml`, gera `addons.xml.md5` e publica os ZIPs
   em hospedagem HTTPS oficial.

O workflow futuro não fará publicação sem uma tag válida, validação concluída
e credenciais de publicação configuradas explicitamente.
