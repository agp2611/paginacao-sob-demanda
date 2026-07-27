# paginacao-sob-demanda

Projeto desenvolvido para a disciplina de **Sistemas Operacionais I** do Centro de Informática da Universidade Federal da Paraíba (UFPB). O objetivo deste simulador é demonstrar na prática o funcionamento dos principais algoritmos de substituição de páginas em memória RAM

---

## ⚙️ Algoritmos Implementados

O programa lê uma sequência de acessos à memória e calcula o número de faltas de páginas (page faults) utilizando os seguintes algoritmos:

*   **FIFO (First In, First Out):** A página que entrou primeiro na memória será a primeira a ser substituída quando faltar espaço
*   **OTM (Algoritmo Ótimo):** Substitui a página que demorará mais tempo para ser referenciada novamente no futuro da sequência
*   **LRU (Least Recently Used):** Substitui a página que está há mais tempo sem ser utilizada (Menos Recentemente Utilizada)

---

## 📂 Estrutura do Projeto

*   `main.py`: Arquivo principal que faz a leitura dos dados e orquestra a chamada dos simuladores
*   `entrada.txt`: Arquivo de texto esperado pelo sistema contendo as configurações da simulação

---

## 📝 Formato de Entrada e Saída

### Arquivo de Entrada (`entrada.txt`)
A entrada deve ser composta exclusivamente por números inteiros, dispostos um por linha
1. O **primeiro número** representa a quantidade máxima de quadros de memória disponíveis
2. Os **demais números** representam a sequência de páginas sendo referenciadas

**Exemplo:**
```text
4
1
2
3
4
1
2
5
1
2
3
4
5