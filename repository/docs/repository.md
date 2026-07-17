# Repositório oficial Kodi

## Funcionamento

Um repositório Kodi é distribuído como um add-on próprio. Seu `addon.xml`
declara o ponto de extensão `xbmc.addon.repository` e informa os endereços
HTTPS do índice, do checksum e dos pacotes publicados.

`addons.xml` é o índice mestre. Em cada release, ele envolverá os manifestos
completos dos add-ons publicados dentro do elemento raiz `<addons>`. O Kodi
consulta primeiro `addons.xml.md5`; quando seu conteúdo mudar, o Kodi busca o
índice atualizado e descobre as versões disponíveis.

## Publicação futura de ZIPs

Quando um add-on for aprovado para publicação, seu pacote seguirá esta forma:

```text
<addon-id>/<addon-id>-<versão>.zip
```

Os ZIPs, o índice e o checksum serão hospedados em endereço HTTPS oficial. O
`datadir` do manifesto apontará para a raiz que contém os diretórios dos
add-ons. Nenhum arquivo de distribuição é criado nesta etapa.

## Versionamento

Os add-ons usarão `MAJOR.MINOR.PATCH`:

- `MAJOR`: mudança incompatível.
- `MINOR`: funcionalidade compatível.
- `PATCH`: correção compatível.

A versão do `addon.xml`, o nome do ZIP e a entrada correspondente em
`addons.xml` deverão ser idênticos. A versão de `repository.ertmann` mudará
somente quando o próprio manifesto ou seus metadados precisarem mudar.

## Assinatura e integridade de releases

As futuras releases usarão tags Git assinadas (GPG ou SSH) e verificáveis no
GitHub. A automação também produzirá hashes SHA-256 para os ZIPs publicados.

Essas assinaturas fornecem procedência no GitHub; elas não substituem os
mecanismos de atualização do Kodi. A distribuição usará HTTPS, `hashes` com
SHA-256 no manifesto e validação do ZIP antes da publicação.
