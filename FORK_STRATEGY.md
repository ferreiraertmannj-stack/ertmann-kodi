# Fork Strategy

Documento de referência oficial do fork Ertmann Media Center sobre o Kodi.

## Objetivos do fork

Criar uma distribuição profissional do Kodi com branding, configurações
otimizadas e ferramentas adicionais da Ertmann Tech, mantendo máxima
compatibilidade com o ecossistema oficial do Kodi.

O que o fork oferece:

- Identidade visual própria (splash, ícones, skin).
- Repositório Ertmann pré-configurado.
- Wizard de configuração inicial.
- Ferramentas de manutenção, diagnóstico e backup.
- Configurações padrão otimizadas.
- Atualizador integrado.

O que o fork **não faz**:

- Não reimplementa funcionalidades existentes do Kodi.
- Não altera APIs públicas (Python, JSON-RPC, binary addons).
- Não quebra compatibilidade com addons, skins ou repositórios existentes.

## O que modificar no core

Modificações no código-fonte do Kodi devem ser absolutamente mínimas e
restritas a:

| Arquivo | Alteração | Justificativa |
| --- | --- | --- |
| `version.txt` | APP_NAME, COMPANY_NAME, WEBSITE, APP_PACKAGE, ADDON_REPOS | Identidade do fork |
| `media/splash.jpg` | Substituir por splash Ertmann | Branding visual |
| `media/icon*.png` | Substituir por ícones Ertmann | Branding visual |
| `media/banner.png` | Substituir por banner Ertmann | Branding visual |
| `media/vendor_*.png` | Substituir por logos Ertmann | Branding visual |
| `system/addon-manifest.xml` | Adicionar addons Ertmann bundled | Pré-instalação |

Total previsto: menos de 15 arquivos modificados em mais de 9.000.

## O que nunca modificar

As seguintes áreas do Kodi não devem ser alteradas em nenhuma circunstância:

- **VideoPlayer** e codecs (FFmpeg, DVDCodecs, DVDDemuxers).
- **Python API** (SWIG bindings em `xbmc/interfaces/python/`).
- **JSON-RPC schema** (`xbmc/interfaces/json-rpc/`).
- **GUIlib** (engine de rendering em `xbmc/guilib/`).
- **Database schemas** (`xbmc/dbwrappers/`, `xbmc/video/`, `xbmc/music/`).
- **Windowing backends** (`xbmc/windowing/`).
- **InputStream API** e binary addon interfaces.
- **PVR framework**.
- **CMake build system** (exceto variáveis derivadas de `version.txt`).

## Estratégia para acompanhar novas versões do Kodi

### Configurar upstream

```cmd
cd kodi-source
git remote add upstream https://github.com/xbmc/xbmc.git
```

### Atualizar para nova versão

```cmd
git fetch upstream
git checkout main
git merge upstream/Omega
```

Conflitos ocorrerão apenas nos arquivos de branding listados acima. Quanto
menos arquivos modificarmos, mais limpo será o merge.

### Mudar de branch do Kodi

Quando uma nova versão estável do Kodi for lançada (ex.: Piers, v22):

```cmd
git fetch upstream
git merge upstream/Piers
```

Testar todos os addons Ertmann antes de publicar a nova versão.

## Como minimizar conflitos

1. Nunca editar arquivos do core além dos listados.
2. Implementar features como addons Python separados.
3. Manter skin como addon fora do tree do Kodi.
4. Usar `advancedsettings.xml` para configurações ao invés de editar
   `settings.xml`.
5. Manter patches isolados e documentados em `build/patches/`.

## Como distribuir releases

### Versionamento do fork

```text
MAJOR.MINOR.PATCH-ertmann.BUILD
```

Onde `MAJOR.MINOR.PATCH` segue a versão do Kodi base e `BUILD` é o
incremental Ertmann.

Exemplo: `21.3.0-ertmann.1` (Kodi Omega 21.3.0, primeiro build Ertmann).

### Artefatos de release

- Binário Windows (instalador ou portable).
- APK Android.
- Imagens LibreELEC e CoreELEC (futuro).
- ZIPs de addons no repositório Ertmann.

### Repositório de addons

O repositório Ertmann (`repository.ertmann`) publica addons via HTTPS:

- `addons.xml` — índice de addons disponíveis.
- `addons.xml.md5` — checksum para detecção de mudanças.
- ZIPs individuais por addon.

## Como manter compatibilidade com addons

1. Nunca alterar `ADDON_API` em `version.txt` sem aprovação.
2. Nunca alterar IDs de addons bundled do Kodi.
3. Manter `repository.xbmc.org` funcional no fork.
4. Testar addons populares antes de cada release.
5. Nunca remover extension points da API.

## Política de branches

| Branch | Uso |
| --- | --- |
| `main` | Branch estável do fork |
| `develop` | Integração de features |
| `feature/*` | Features aprovadas |
| `fix/*` | Correções |
| `release/*` | Preparação de releases |
| `upstream/*` | Tracking do Kodi upstream |

## Política de patches

Patches sobre o Kodi devem ser:

1. Mínimos e cirúrgicos.
2. Documentados com justificativa.
3. Isoláveis em arquivos `.patch` quando possível.
4. Testados contra merge com upstream.
5. Nunca aplicados sem revisão.

## Checklist antes de atualizar o Kodi

- [ ] Fetch e review das mudanças upstream.
- [ ] Identificar conflitos potenciais com patches Ertmann.
- [ ] Merge em branch `upstream/sync-VERSAO`.
- [ ] Resolver conflitos nos arquivos de branding.
- [ ] Build completo em pelo menos uma plataforma.
- [ ] Testar addons Ertmann (wizard, maintenance, network, log).
- [ ] Testar skin Ertmann.
- [ ] Testar reprodução de mídia (vídeo, áudio, streams).
- [ ] Testar compatibilidade com addons populares.
- [ ] Atualizar CHANGELOG.
- [ ] Criar tag de release.
- [ ] Nunca executar `git push` sem revisão.
