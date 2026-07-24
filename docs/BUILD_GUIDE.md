# Ertmann Media Center — Build Guide (Windows)

Este documento detalha as etapas necessárias para compilar o núcleo C++ modificado do Kodi na plataforma Windows, permitindo testar a **Skin Oficial**, **Setup Wizard** e os **Utilitários Avançados** em ambiente nativo.

## Pré-requisitos Obrigatórios

A compilação do core (kodi-source) exige bibliotecas pesadas e um ambiente de desenvolvimento robusto. Certifique-se de ter instalado em seu sistema:

1. **Visual Studio 2022** (Edição Community, Professional ou Enterprise)
   - *Cargas de Trabalho necessárias*: "Desenvolvimento para desktop com C++" e "Desenvolvimento com a Plataforma Universal do Windows (UWP)".
2. **Git para Windows**
3. **CMake** (v3.24 ou superior)
4. **NASM** (Adicionado à variável de ambiente `PATH`)

## Configurando o Ambiente de Compilação

Para não poluirmos nosso repositório `ertmann-kodi-platatform`, é altamente recomendado construir as dependências em uma pasta paralela de build.

1. Abra o prompt de comando nativo do Windows (NUNCA utilize PowerShell, conforme nossas regras de governança) ou a linha de comando do Visual Studio (`Developer Command Prompt for VS 2022`).
2. Navegue até o repositório original do Kodi (`kodi-source`):
   ```cmd
   cd c:\Users\ferre\ertmann-kodi-platatform\kodi-source
   ```

3. Configure o CMake para gerar os arquivos da solução (`.sln`):
   ```cmd
   mkdir build
   cd build
   cmake -G "Visual Studio 17 2022" -A x64 ..
   ```

4. Após a geração da solução, o arquivo `kodi.sln` será criado dentro da pasta `build`.

## Compilando o Projeto

Você pode abrir o `kodi.sln` com o Visual Studio 2022 e clicar em **Compilar (Build)** ou prosseguir pela linha de comando:

```cmd
cmake --build . --config Release
```

*Atenção: A primeira compilação do sistema baixará dezenas de dependências (ffmpeg, curl, etc.) e pode levar desde alguns minutos até mais de uma hora dependendo da sua CPU.*

## Testando Nossos Addons (Instalação)

Ao finalizar a compilação, o executável `kodi.exe` estará pronto na pasta `build\Release`.

Ao abrir o aplicativo pela primeira vez:
1. Vá até a seção de Addons (ou navegue nas configurações).
2. Nossa versão (modificada no `version.txt`) identificará a plataforma como **Ertmann Media Center**.
3. Adicione nossos plugins zipados (`repository/zips`) usando a opção *Install from zip file*. 
4. Nossa Skin (`skin.ertmann`) será carregada, chamando imediatamente o Setup Wizard.

## Troubleshooting

Se encontrar erros referentes a falta de bibliotecas durante o CMake:
- Verifique se executou o arquivo `download_dependencies.bat` disponibilizado nativamente pela documentação do Kodi (`tools/buildsteps/windows`).
- Revise as permissões de gravação de arquivos na unidade C:\.
