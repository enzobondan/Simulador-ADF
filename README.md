<h1 align="center">Simulador AFD</h1>
<h3 align="center">Simulador de Autômato Finito Determinístico</h3>

### 🎯 Objetivo
O objetivo desta atividade consiste em implementar um simulador de **autômato finito determinístico (AFD)** e a realização de testes utilizando autômatos construídos. O simulador deverá receber como entrada as configurações do AFD 
(símbolos do alfabeto, estado inicial, estado final e transições), além de uma cadeia `s` de entrada. Como resposta, deverá retornar uma mensagem informando se a cadeia `s` em questão foi aceita ou rejeitada pelo AFD. 
O arquivo de entrada do autômato deverá estar no seguinte formato:

`#Número N de estados do autômato` \
`#Estado Inicial` \
`#Número F de estados finais` \
`#Estados Finais` \
`#N´umero S de símbolos do alfabeto` \
`#Símbolos (separados por espaço)` \
`#Número M de transições` \
`#Transições (estado_atual símbolo estado_destino)` \
`#Cadeia de entrada`

---
### ✔️ Etapas da Avaliação
- `Simulador:` Implementamos um programa capaz de receber a definição formal de um AFD (conjunto de estados, alfabeto, função de transição, estado inicial e conjunto de estados de aceitação) e simular o reconhecimento de palavras.
O simulador é capaz de determinar se uma palavra é reconhecida ou não pelo autômato. os autômatos no simulador, destacando eventuais dificuldades encontradas e aprendizados adquiridos durante o processo.
Os arquivos de teste foram enviados em conjunto com o código do simulador.
- `Relatório:` Descrevemos o processo de implementação do simulador de AFD, detalhando as estruturas de dados utilizadas e os algoritmos implementados. Ademais, construímos 03 autômatos finitos e testamos no simulador construído,
fornecendo exemplos de palavras reconhecidas e rejeitadas por cada autômato. Analisamos os resultados obtidos nos testes realizados com os autômatos no simulador, destacando eventuais dificuldades encontradas e aprendizados adquiridos durante o processo.
