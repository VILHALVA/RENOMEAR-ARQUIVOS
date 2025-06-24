# [ATUALIZAÇÕES:](./UPDATES.md#vers%C3%A3o-10---06122023)

## VERSÃO 1.4 - 14/06/2025
* ✅**Controles de ordenação visíveis apenas no modo GERAL:** Os botões de ordenação e o switch de ordem agora só aparecem e funcionam quando o modo GERAL está selecionado.
* ✅**Seção de zeros à esquerda (modo `0`):** Ao selecionar o modo `0`, uma nova seção é exibida acima do botão RENOMEAR, contendo o controle QUANTIDADE — um *slider* que vai de 1 a 9. Esse controle permite definir o número total de dígitos desejado nos números finais dos nomes dos arquivos. O valor padrão é 3 dígitos.
* ✅**Botão RESETAR:** Permite desfazer a última renomeação realizada, restaurando os nomes originais dos arquivos. Não feche o aplicativo ou inicie uma nova renomeação, senão a ação de resetar será perdida.
---

## VERSÃO 1.3 - 09/06/2025
* ✅**Numeração inteligente:** Agora, se o nome universal terminar com um número, a numeração sequencial começará a partir desse número, mantendo os zeros à esquerda.  
  Exemplo: FAIXA 05 → FAIXA 05, FAIXA 06, FAIXA 07...

  * ✔️Também funciona nos seguintes casos:
    * Quando o nome universal é apenas um número:  
      Exemplo: 05 → 05.ext, 06.ext, 07.ext...
    * Quando o campo está em branco:  
      Resultado: 01.pdf, 02.png, 03.docx...

* ✅Arquivos ocultos e de sistema são ignorados automaticamente durante o processo de renomeação — mesmo que estejam visíveis no Explorador do Windows.
* ✅O nome do aplicativo foi alterado de "RENOMEAR ARQUIVOS" para "RENOMEADOR DE ARQUIVOS".
---

## VERSÃO 1.2 - 21/05/2025
* ✅Este aplicativo agora utiliza a biblioteca `customtkinter` para uma interface gráfica mais moderna e estilizada, substituindo o antigo `tkinter`. 
* ✅Foi adicionado um novo botão chamado `MISTO`, que renomeia os arquivos convertendo apenas a primeira letra de cada nome para maiúscula.
---

## VERSÃO 1.1 - 20/05/2025:
* ✅O aplicativo agora se chama "RENOMEAR ARQUIVOS".
* ✅Foi criado o instalador.
* ✅Renomeia arquivos com 4 modos: `GERAL` (ordem por ID3), `0` (adiciona "0"), `UPPER` e `LOWER`. Campo "NOME UNIVERSAL" aparece só no modo `GERAL`. Feedback via pop-ups.
* ✅Os aplicativos apagados foram: "RENOMEAR PARA 0" e "RENOMEAR UPPER" -> (06/12/2023).
---

## VERSÃO 1.0 - 06/12/2023:
* ✅**O aplicativo é lançado oficialmente com o nome `RENOMEAR MUSICAS`, desenvolvido com `tkinter`:**
A interface conta com um botão "SELECIONAR", utilizado para escolher o diretório, um campo para inserir o nome universal (aceitando apenas um parâmetro) e o botão "RENOMEAR".
Uma `messagebox` é exibida ao final do processo, indicando se a renomeação foi bem-sucedida ou se ocorreu algum erro.
* ✅**Em `18/12/2023`, foram feitas algumas melhorias no aplicativo (1.0.1):**
  * 🔹Adição de um rodapé com meu nome e meu username do GitHub.
  * 🔹Refatoração e revisão do código para maior clareza e eficiência.
  * 🔹Inclusão do nome e do ícone oficial do aplicativo.
  * 🔹Alteração no parâmetro de compilação, eliminando a necessidade de o usuário ter pacotes do módulo `_internal` instalados no sistema. Agora, o aplicativo é totalmente autônomo.



