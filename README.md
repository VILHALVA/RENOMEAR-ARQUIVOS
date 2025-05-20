# RENOMEAR ARQUIVOS
🎈RENOMEIE OS ARQUIVOS GLOBALMENTE.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
Este projeto permite que você **renomeie arquivos de qualquer tipo** em um diretório selecionado, oferecendo múltiplos modos de renomeação para diferentes finalidades.
Com uma interface simples, você pode aplicar renomeações em lote com apenas alguns cliques.

## FUNCIONALIDADES:
### GERAL (NOME UNIVERSAL + NUMERAÇÃO SEQUENCIAL):
Renomeia todos os arquivos do diretório com um nome universal, seguido de numeração sequencial (`01`, `02`, etc).
Se os arquivos forem MP3 com metadados de faixa (tag `tracknumber`), a ordem da renomeação respeita esses dados automaticamente.

**Exemplo com arquivos diversos:**

```
Imagem1.png, ArquivoB.pdf, Outro.docx
→
ARQUIVO 01.png, ARQUIVO 02.pdf, ARQUIVO 03.docx
```

**Exemplo com músicas com tags ID3:**

```
Track B.mp3 (Faixa 1), Song A.mp3 (Faixa 2), Music C.mp3 (Faixa 3)
→
MUSICA 01.mp3, MUSICA 02.mp3, MUSICA 03.mp3
```

### 0 (ADICIONAR "0" NO INÍCIO DO NOME):
Adiciona a letra **"0" no início do nome de todos os arquivos**, sem verificar se já existe.
**Exemplo:**

```
nota.txt → 0nota.txt  
imagem.png → 0imagem.png
```

### UPPER (NOME EM MAIÚSCULAS):
Converte todos os nomes de arquivos para letras **maiúsculas**, mantendo espaços.
**Exemplo:**

```
meu documento.pdf → MEU DOCUMENTO.pdf
```

### LOWER (NOME EM MINÚSCULAS):
Converte todos os nomes de arquivos para letras **minúsculas**, mantendo espaços.
**Exemplo:**

```
Foto De Viagem.JPG → foto de viagem.JPG
```

## EXECUTANDO O PROJETO:
### 1. INSTALE AS DEPENDÊNCIAS:
Antes de iniciar o aplicativo, é necessário instalar as bibliotecas utilizadas no projeto. No terminal, execute:

```bash
pip install -r requirements.txt
```

> 💡 O arquivo `requirements.txt` está localizado dentro da pasta `./CODIGO`.

### 2. EXECUTE O APLICATIVO:
Acesse o diretório do código e inicie o programa com:

```bash
cd CODIGO
python CODIGO.py
```

### 3. USE O APLICATIVO:
Após a execução, uma janela chamada **"RENOMEAR ARQUIVOS"** será exibida. Siga os passos abaixo:

1. Clique em **"SELECIONAR"** para escolher a pasta onde estão os arquivos que deseja renomear.

2. No campo **"NOME UNIVERSAL"**, digite o nome base que será usado para renomear os arquivos (exemplo: `ARQUIVO`, `DOCUMENTO`, `MUSICA`, etc.).

3. Escolha um dos modos disponíveis:

   * `GERAL`: Renomeia todos os arquivos com o nome universal seguido de numeração sequencial (01, 02, ...).
     Se forem arquivos `.mp3`, e possuírem tags ID3 com `tracknumber`, a ordem será respeitada com base nessas faixas.

   * `0`: Adiciona o dígito **0** no início de todos os nomes de arquivos.

   * `UPPER`: Converte todos os nomes para **maiúsculo**.

   * `LOWER`: Converte todos os nomes para **minúsculo**.

4. Clique em **"RENOMEAR"** para iniciar o processo.

5. Após a renomeação, será exibida a mensagem:

```text
Renomeação concluída!
```

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO:
   - O instalador está disponível apenas para `Windows X64`. Para instala-lo, basta dar dois cliques e seguir as orientações na tela. 

   - O executável está disponível apenas para `Windows X64` (No diretório `APP`). Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

   - É importante explicar que ao executar o arquivo executável deste programa, é possível que o antivírus dispare um alerta de segurança. Isso ocorre porque o programa executa comandos do sistema operacional e pode abrir outros aplicativos ou acessar a rede.

   **Para lidar com isso, há 2 alternativas:**

   1. **Adicionar exceção ao antivírus:** Você pode optar por adicionar uma exceção ao antivírus para permitir que o programa execute comandos do sistema sem disparar alertas. Isso geralmente pode ser feito acessando as configurações do antivírus e adicionando o arquivo executável do programa à lista de exceções.

   2. **Executar apenas o `CODIGO.py`:** Uma alternativa é optar por executar apenas o arquivo de código-fonte Python (`CODIGO.py`). Isso evita que o antivírus dispare alertas, já que você e o sistema podem inspecionar o código fonte diretamente.

### 2. GERANDO O EXECUTAVEL:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O SCRIPT DO INSTALADOR:
1. **Abrir o Inno Setup**: Após a instalação, abra o Inno Setup.
2. **Novo Script**: Na tela inicial, clique em "New Script" e selecione "Next" no assistente que aparecer.
3. **Informações Básicas**:
   - **Application Information**: Preencha as informações da sua aplicação, como nome, versão, nome do publisher e website.
   - **Application Destination Base Folder**: Normalmente, você pode deixar como "{pf}\YourAppName" (para instalar no diretório de Program Files).
   - **Application Directory**: Selecione a pasta onde estão os arquivos da sua aplicação. Em `./CODIGO` desse repositório.
   - **Application Files**: Adicione todos os arquivos necessários para a instalação da sua aplicação (executáveis, DLLs, etc).
   - **Application Shortcuts**: Escolha se deseja criar atalhos no menu Iniciar, na área de trabalho, etc.
   - **Application Documentation**: Adicione arquivos de licença e outros documentos necessários.
4. **Output**: Escolha onde o arquivo de instalação (.exe) será salvo.
5. **Create Script**: Clique em "Finish" para gerar o script base.

#### PASSO 3: EDITAR O SCRIPT:
O Inno Setup irá abrir o script gerado automaticamente. Aqui, você pode fazer ajustes se necessário. O script terá uma estrutura básica como esta:

```pascal
[Setup]
AppName=Your Application Name
AppVersion=1.0
DefaultDirName={pf}\YourAppName
DefaultGroupName=YourAppName
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Path\To\YourApp\*"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\YourApp.exe"
Name: "{commondesktop}\YourAppName"; Filename: "{app}\YourApp.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YourApp.exe"; Description: "{cm:LaunchProgram,YourAppName}"; Flags: nowait postinstall skipifsilent
```

#### PASSO 4: COMPILAR O SCRIPT:
1. **Compilar**: Com o script aberto no Inno Setup, clique no botão "Compile" na barra de ferramentas.
2. **Verificar**: O Inno Setup irá compilar o script e criar o arquivo de instalação na pasta especificada.
3. **Testar**: Execute o instalador gerado para testar e verificar se tudo está funcionando corretamente.

#### PASSO 5: PERSONALIZAÇÕES ADICIONAIS (OPCIONAL):
Você pode adicionar customizações ao seu instalador, como adicionar telas personalizadas, verificações de pré-requisitos, etc. A documentação oficial do Inno Setup tem exemplos e explicações detalhadas para essas funcionalidades.

#### RECURSOS ÚTEIS:
- **Documentação Oficial**: [Inno Setup Documentation](http://www.jrsoftware.org/isinfo.php)
- **Exemplos de Scripts**: O Inno Setup inclui exemplos de scripts que podem ser muito úteis para entender como implementar certas funcionalidades.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)



