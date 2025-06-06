# RENOMEAR ARQUIVOS
🎈RENOMEIE OS ARQUIVOS GLOBALMENTE.

<img src="FOTO.png" align="center" width="500"> <br> 

## DESCRIÇÃO:
Este projeto permite que você **renomeie arquivos de qualquer tipo** em um diretório selecionado, oferecendo múltiplos modos de renomeação para diferentes finalidades.
Com uma interface simples, você pode aplicar renomeações em lote com apenas alguns cliques.

## FUNCIONALIDADES:
### GERAL (NOME UNIVERSAL + NUMERAÇÃO SEQUENCIAL)
Renomeia todos os arquivos do diretório com um **nome universal opcional** seguido de numeração sequencial (`01`, `02`, etc).

* Para arquivos `.mp3`, a ordenação respeita a tag `tracknumber` (se existir).
* Para outros formatos, a ordenação é alfabética simples.
* Se o nome universal terminar com número, a numeração sequencial inicia a partir desse número, preservando os zeros à esquerda (ex: `FAIXA 05` → `FAIXA 05`, `FAIXA 06`, ...).

**Exemplos:**

* Nome universal preenchido sem número:

  ```
  ARQUIVO 01.pdf, ARQUIVO 02.png, ARQUIVO 03.docx
  ```

* Nome universal vazio:

  ```
  01.pdf, 02.png, 03.docx
  ```

* Arquivos diversos com nome universal:

  ```
  Imagem1.png, ArquivoB.pdf, Outro.docx
  → RELATORIO 01.png, RELATORIO 02.pdf, RELATORIO 03.docx
  ```

* Arquivos `.mp3` com tag `tracknumber`:

  ```
  Track B.mp3 (Faixa 1), Song A.mp3 (Faixa 2), Music C.mp3 (Faixa 3)
  → MUSICA 01.mp3, MUSICA 02.mp3, MUSICA 03.mp3
  ```

* Nome universal com número `05` no final:

  ```
  FAIXA 05 → FAIXA 05.ext, FAIXA 06.ext, FAIXA 07.ext, ...
  ```

* Nome universal apenas com número `05`:
  ```
  05 → 05.ext, 06.ext, 07.ext, ...
  ```

### 0 (ZERAR NUMERAÇÃO):
Detecta números no final dos nomes e os formata com **mais dígitos**, adicionando um zero à esquerda.
Ideal para padronizar faixas ou itens numerados.

**Exemplo:**

```
FAIXA 1 → FAIXA 01  
FAIXA 2 → FAIXA 02  
FAIXA 10 → FAIXA 010
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

### MISTO (PRIMEIRA LETRA MAIÚSCULA):
Converte somente a **primeira letra do nome** do arquivo para maiúscula, deixando o restante como está.

**Exemplo:**

```
FAIXA 01 → Faixa 01  
documento importante.txt → Documento importante.txt
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

   * `GERAL`: Renomeia todos os arquivos com um **nome universal opcional** seguido de numeração sequencial (`01`, `02`, ...).
   Se o campo de nome universal estiver vazio, renomeia apenas com os números sequenciais.
   Para arquivos `.mp3`, a ordenação usa a tag ID3 `tracknumber` quando disponível.
   Se o nome universal terminar com um número, por exemplo: `FAIXA 05 → FAIXA 05.ext, FAIXA 06.ext, FAIXA 07.ext, ...`
   Se o nome universal for apenas um número, por exemplo: `05 → 05.ext, 06.ext, 07.ext, ...`

   * `0`: Zera a numeração dos nomes, adicionando um zero à esquerda (ex: `FAIXA 1` → `FAIXA 01`).

   * `UPPER`: Converte todos os nomes para **maiúsculo**.

   * `LOWER`: Converte todos os nomes para **minúsculo**.

   * `MISTO`: Deixa **apenas a primeira letra maiúscula**, mantendo o restante do nome como está.

4. Clique em **"RENOMEAR"** para iniciar o processo.
5. Após a renomeação, será exibida a mensagem:
```text
Renomeação concluída!
```

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO:
   * O instalador está disponível  em `./APP`. Para instala-lo, basta dar dois cliques e seguir as orientações na tela. 

### 2. GERANDO O EXECUTAVEL:
   **1. Instalação do PyInstaller:**
   * Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   * No diretório `./CODIGO`, utilize o comando abaixo para gerar o executável:

   ```bash
   pyinstaller EXECUTAVEL.spec
   ```

   * O executável `COPY PASTAS.exe` será criado na pasta `./CODIGO/dist`.
   * Após a geração, você pode excluir a pasta `./CODIGO/build`.

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O INSTALADOR:
1. **Editar o arquivo do instalador**
   No diretório `./CODIGO`, abra o arquivo `INSTALADOR.iss` e atualize os seguintes trechos:

   * **Ícone do instalador:**
     Substitua o caminho atual da linha `SetupIconFile=` pelo caminho correto do seu ícone:

     ```ini
     SetupIconFile=C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\RENOMEAR ARQUIVOS\CODIGO\imagem.ico
     ```

   * **Caminho do executável a ser empacotado:**
     Atualize a seção `[Files]` com o caminho do executável gerado:

     ```ini
     [Files]
     Source: "C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\RENOMEAR ARQUIVOS\CODIGO\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
     ```

2. **Gerar o instalador no Inno Setup:**
   * Abra o arquivo `./CODIGO/INSTALADOR.iss` com o **Inno Setup**.
   * Clique em **"Compile"** para gerar o instalador.

3. **Limpar arquivos temporários:**
   * Após a criação do instalador, você pode excluir o executável temporário:

     ```
     ./CODIGO/dist/RENOMEAR ARQUIVOS.exe
     ```

4. **Instalando o Aplicativo:**
   * Execute o instalador gerado, localizado em:

   ```
   ./APP/RENOMEAR ARQUIVOS.exe
   ```

   * O assistente de instalação será iniciado e, por padrão, o aplicativo será instalado em:

   ```
   C:\Program Files\RENOMEAR ARQUIVOS
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [DOCUMENTAÇÃO OFICIAL DO PYINSTALLER](https://pyinstaller.org/en/stable/)
* [DOCUMENTAÇÃO OFICIAL DO INNO SETUP](http://www.jrsoftware.org/isinfo.php)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)



