# RENOMEADOR DE ARQUIVOS
👨‍🏫RENOMEIE OS ARQUIVOS GLOBALMENTE.

<img src="FOTO.png" align="center" width="500"> <br> 

## DESCRIÇÃO:
Este projeto é uma **ferramenta gráfica avançada para renomeação em massa de arquivos**, desenvolvida com a biblioteca `customtkinter`. Ele permite que você **renomeie arquivos de qualquer tipo** em um diretório selecionado, de forma rápida, segura e personalizável.

Com este aplicativo, você pode:

* Escolher entre **vários modos de renomeação**, como:

  * Nomeação sequencial com número automático.
  * Conversão de letras para **maiúsculas**, **minúsculas** ou **capitalização mista**.
  * Padronização de números com **zeros à esquerda**.

* Definir um **nome base universal** que será usado como padrão em todos os arquivos.

* Aplicar **diferentes critérios de ordenação** antes da renomeação:

  * Por nome atual do arquivo.
  * Por metadado de **título** (especialmente útil para músicas).
  * Pelo número da faixa (`tracknumber`) de arquivos `.mp3`.
  * Pela data de **criação** ou de **modificação** do arquivo.

* Controlar a **direção da ordenação** (CRESCENTE ou DESCRESCENTE) com um botão de alternância intuitivo.

Além disso, o sistema ignora arquivos ocultos ou de sistema automaticamente, garantindo que apenas os arquivos visíveis e relevantes sejam renomeados.

É ideal para organizar coleções de músicas, documentos, imagens, vídeos ou qualquer outro conjunto de arquivos com eficiência e precisão.

## FUNCIONALIDADES:
### MODO DE RENOMEAÇÃO:
#### GERAL (NOME UNIVERSAL + NUMERAÇÃO SEQUENCIAL):
Renomeia todos os arquivos do diretório com um **nome universal opcional** seguido de numeração sequencial (`01`, `02`, etc).

* A ordem de renomeação respeita o critério de ordenação escolhido (NOME, CRIAÇÃO, MODIFICAÇÃO ou NÚMERO).
* Para arquivos `.mp3`, a ordenação por **NÚMERO** usa a tag `tracknumber` dos metadados (como exibido no Explorador de Arquivos do Windows).
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

* Arquivos `.mp3` com tag `tracknumber` e ordenação "NÚMERO":

  ```
  Track B.mp3 (Faixa 2), Song A.mp3 (Faixa 1), Music C.mp3 (Faixa 3)
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
#### 0 (ZERAR NUMERAÇÃO):
Detecta números no final dos nomes e os formata com **mais dígitos**, adicionando zeros à esquerda.

**Exemplo:**

```
FAIXA 1 → FAIXA 001  
FAIXA 2 → FAIXA 002  
FAIXA 10 → FAIXA 010
```

#### UPPER (NOME EM MAIÚSCULAS):
Converte todos os nomes de arquivos para letras **maiúsculas**, mantendo espaços.

**Exemplo:**

```
meu documento.pdf → MEU DOCUMENTO.pdf
```

#### LOWER (NOME EM MINÚSCULAS):
Converte todos os nomes de arquivos para letras **minúsculas**, mantendo espaços.

**Exemplo:**

```
Foto De Viagem.JPG → foto de viagem.JPG
```

#### MISTO (PRIMEIRA LETRA MAIÚSCULA):
Converte somente a **primeira letra do nome** do arquivo para maiúscula, deixando o restante como está.

**Exemplo:**

```
FAIXA 01 → Faixa 01  
documento importante.txt → Documento importante.txt
```

### ORDEM DE RENOMEAÇÃO:
#### NOME:
* **Ordenar por NOME:**
  - Ordena os arquivos em ordem alfabética pelo nome do arquivo (padrão simples).

#### NÚMERO:
* **Ordenar por NÚMERO:**
  - Ordena os arquivos com base no **número da faixa** obtido dos metadados, por exemplo, da tag `tracknumber` em arquivos `.mp3`.
  - Para outros arquivos que não têm essa informação, usa uma ordenação alfabética simples.
  - Essa ordenação é útil para organizar faixas de música ou arquivos numerados conforme o número embutido nos metadados.

#### CRIAÇÃO:
* **Ordenar por DATA DE CRIAÇÃO:**
  - Ordena os arquivos pela data/hora em que foram criados no sistema de arquivos.

#### MODIFICAÇÃO:
* **Ordenar por Data de Modificação:**
  - Classifica os arquivos com base na **última data e hora em que foram alterados**.
  - Pode organizar do **mais antigo para o mais recente** ou vice-versa, dependendo da direção de ordenação escolhida (`CRESCENTE` ou `DESCRESCENTE`).

### BOTÃO CRESCENTE/DESCRESCENTE:
Esse botão de **"CRESCENTE/DESCRESCENTE"** controla a ordem em que os arquivos são organizados antes de serem renomeados:

* **CRESCENTE** (ativado): ordena do menor para o maior — por exemplo, do nome "A" para "Z", do número 1 para 10, ou da data mais antiga para a mais recente.
* **DESCRESCENTE** (desativado): faz o contrário — do maior para o menor.

Essa ordem afeta todos os botões de ordenação: **NOME, TÍTULO, NÚMERO, CRIAÇÃO e MODIFICAÇÃO**.

## EXECUTANDO O PROJETO:
### 1. INSTALE AS DEPENDÊNCIAS:
Antes de iniciar o aplicativo, é necessário instalar as bibliotecas utilizadas no projeto. No terminal, execute:

```bash
pip install -r requirements.txt
```

> 💡 O arquivo `requirements.txt` está localizado dentro da pasta `./CODIGO`.

### 2. EXECUTE O APLICATIVO:
Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python CODIGO.py
```

### 3. USE O APLICATIVO:
Após abrir a janela chamada **"RENOMEADOR DE ARQUIVOS"**, siga os passos abaixo:

1. Clique em **"SELECIONAR"** para escolher a pasta onde estão os arquivos que deseja renomear.

2. No campo **"NOME UNIVERSAL"**, digite o nome base que será usado para renomear os arquivos (exemplo: `ARQUIVO`, `DOCUMENTO`, `MUSICA`, etc.).
   *Este campo é utilizado apenas no modo GERAL.*

3. Escolha um dos modos disponíveis:

   * `GERAL`: Renomeia todos os arquivos com um **nome universal opcional** seguido de numeração sequencial (`01`, `02`, ...).

     * Se o campo de nome universal estiver vazio, renomeia apenas com os números sequenciais.
     * Para arquivos `.mp3`, a ordenação usa a tag ID3 `tracknumber` (número da faixa) quando disponível.
     * Para outros formatos, a ordenação padrão será a escolhida nos botões de ordenação.
     * Se o nome universal terminar com um número, por exemplo:
       `FAIXA 05 → FAIXA 05.ext, FAIXA 06.ext, FAIXA 07.ext, ...`
     * Se o nome universal for apenas um número, por exemplo:
       `05 → 05.ext, 06.ext, 07.ext, ...`

   * `0`: Ajusta os números no final dos nomes para terem zeros à esquerda, padronizando a numeração (ex: `FAIXA 1` → `FAIXA 001`, `FAIXA 10` → `FAIXA 010`).

   * `UPPER`: Converte todos os nomes para letras **maiúsculas**.

   * `LOWER`: Converte todos os nomes para letras **minúsculas**.

   * `MISTO`: Deixa **apenas a primeira letra maiúscula** de cada nome, mantendo o restante como está.

4. Escolha a forma de ordenação dos arquivos antes da renomeação:

   * `NOME`: Ordenação alfabética com base no nome atual do arquivo (renomeado manualmente).
   * `TÍTULO`: Ordenação com base no campo de **metadados "TÍTULO"** dos arquivos (comum em músicas `.mp3`).
   * `NÚMERO`: Ordena pelos **números das faixas** extraídos dos metadados dos arquivos `.mp3`.
   * `CRIAÇÃO`: Ordena pela **data de criação** dos arquivos.
   * `MODIFICAÇÃO`: Ordena pela **data da última modificação** dos arquivos.

5. Use o botão **CRESCENTE/DESCRESCENTE** para definir a direção da ordenação:

   * Quando **ativado (CRESCENTE)**: ordena do menor para o maior (ex: `A → Z`, `1 → 10`, mais antigo → mais novo).
   * Quando **desativado (DESCRESCENTE)**: faz o contrário (ex: `Z → A`, `10 → 1`, mais novo → mais antigo).

6. Clique em **"RENOMEAR"** para iniciar o processo.

7. Após a renomeação, será exibida a mensagem:

```text
Renomeação concluída!
```

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO O INSTALADOR:
  * O instalador está localizado no diretório `./APP` e está disponível apenas para sistemas **Windows x64**. Para realizar a instalação, basta **dar dois cliques no arquivo** e seguir as instruções exibidas na tela.

### 2. GERANDO O EXECUTAVEL:
> **IMPORTANTE:** Antes de criar o instalador, é necessário gerar o arquivo `RENOMEADOR DE ARQUIVOS.exe`. Para isso, siga os passos abaixo:

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

   * O executável `RENOMEADOR DE ARQUIVOS.exe` será criado na pasta `./CODIGO/dist`.
   * Após a geração, você pode excluir a pasta `./CODIGO/build`.

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O INSTALADOR:
> **IMPORTANTE:** Antes de criar o novo instalador, certifique-se de excluir o arquivo `./APP/RENOMEADOR DE ARQUIVOS.exe`.

1. **Editar o arquivo do instalador:**
   * No diretório `./CODIGO`, abra o arquivo `INSTALADOR.iss` e atualize o seguinte trecho:

   * Localize a diretiva `#define Diretorio` e substitua pelo caminho correto do diretório do projeto. Exemplo:

     ```ini
     #define Diretorio "C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\RENOMEADOR DE ARQUIVOS\CODIGO"
     ```

2. **Gerar o instalador no Inno Setup:**
   * Abra o arquivo `./CODIGO/INSTALADOR.iss` com o **Inno Setup**.
   * Clique em **"Compile"** para gerar o instalador.

3. **Limpar arquivos temporários:**
   * Após a criação do instalador, você pode excluir o executável temporário `./CODIGO/dist/RENOMEADOR DE ARQUIVOS.exe`.

4. **Instalando o Aplicativo:**
   * Se o `Aplicativo` não iniciar automaticamente a instalação, você pode executar manualmente o arquivo `./APP/RENOMEADOR DE ARQUIVOS.exe` clicando duas vezes sobre ele.
   * O assistente de instalação será iniciado e, por padrão, o aplicativo será instalado no seguinte caminho: `C:\Program Files\RENOMEADOR DE ARQUIVOS`.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos e alguns subsídios:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)
* [DOCUMENTAÇÃO OFICIAL DO PYINSTALLER](https://pyinstaller.org/en/stable/)
* [DOCUMENTAÇÃO OFICIAL DO INNO SETUP](http://www.jrsoftware.org/isinfo.php)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)



