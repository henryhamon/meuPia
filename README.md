# meuPiá – Portugol Inteligência Artificial

![meuPia](assets/meuPia.png)

## 📖 Overview

> **Nota:** Este projeto é um *fork* evolutivo do [`portugol-compiler`](https://github.com/LuanContarin/portugol-compiler), focado em interoperabilidade.

**meuPiá** é um compilador (transpilador) de Portugol para Python projetado para o ensino de **Inteligência Artificial** e **Automação**.

**meuPiá** fornece:

* **O Compilador:** Um analisador léxico, sintático e semântico robusto que traduz Portugol diretamente para scripts Python executáveis.
* **A Runtime (Lib):** Wrappers nativos e simplificados para ocultar a complexidade de APIs avançadas, mantendo a simplicidade educacional.
* **A Ponte:** Uma arquitetura que permite ao aluno ir do "Olá Mundo" ao "Treinamento de Rede Neural" sem trocar de linguagem.

## ⚙️ How It Works

O framework opera em uma arquitetura de três estágios:

### 1. Analysis (O Legado Robusto)

Baseado no excelente trabalho do `portugol-compiler`, o meuPiá realiza a análise léxica e sintática para garantir que o aluno escreveu um algoritmo válido, gerando uma Árvore Sintática e pares de lexemas.

### 2. Code Generation (O Transpilador)

Diferente de um interpretador simples, o meuPiá possui um `CodeGenerator` que percorre a árvore sintática e escreve um arquivo `.py` equivalente, injetando automaticamente as dependências necessárias.

### 3. The Runtime Wrappers (`lib/`)

Bibliotecas Python otimizadas (o "motor" do meuPiá) que são importadas automaticamente no código gerado:

* **meupia_ml:** Encapsula `numpy` e `sklearn` para classificação e regressão.
* **meupia_space:** Gerencia a conexão RPC com o Kerbal Space Program.

## 🚀 Installation

```bash
# 1. Clone o repositório
git clone https://github.com/henryhamon/meuPia.git
cd meuPia

# 2. Instale as dependências do Python
pip install -r requirements.txt
# (Requer krpc, scikit-learn, numpy)

```

## 🛠️ Usage Examples

### 1. Compilando um Algoritmo

Coloque seu arquivo `.por` na pasta `input/` e execute o compilador:

```bash
python meuPia.py input/missao_espacial.por

```

*Isso irá gerar e executar automaticamente o arquivo `output/missao_espacial.py`.*

### 2. Exemplo: Inteligência Artificial

Treinando um modelo simples para classificar frutas em Portugol:

```portugol
algoritmo "classificador_frutas"
var
    dados, labels: inteiro
    fruta_nova: inteiro
inicio
    escreva("--- Iniciando IA ---")
    
    // [Peso, Textura] -> Treinamento
    ia_definir_dados([[150, 0], [170, 0], [130, 1]], [0, 0, 1])
    
    ia_criar_knn(3)
    ia_treinar()
    
    fruta_nova <- ia_prever([160, 0])
    
    se fruta_nova = 0 entao
        escreva("É uma maçã!")
    senao
        escreva("É uma laranja!")
    fim_se
fimalgoritmo

```

### 3. Exemplo: Automação Espacial (KSP)

Controlando a telemetria de um foguete:

```portugol
algoritmo "lancamento_automatico"
var
    altitude: inteiro
inicio
    ksp_conectar()
    altitude <- 0
    
    enquanto altitude < 10000 faca
        altitude <- ksp_obter_altitude()
        escreva("Altitude atual: ", altitude)
        
        se altitude > 5000 entao
             ksp_ativar_estagio()
        fim_se
    fim_enquanto
fimalgoritmo

```


## 🔍 Limitations

* **Dependência do KSP:** Para funções espaciais, o jogo Kerbal Space Program deve estar rodando com o mod `kRPC` instalado.

## 🙌 Credits

> **meuPiá** é desenvolvido com ❤️ por **[@henryhamon](https://github.com/henryhamon)**.

Este projeto é um *hard fork* e evolução do projeto [portugol-compiler](https://github.com/LuanContarin/portugol-compiler), criado originalmente por **Luan Contarin**. A estrutura de análise léxica e sintática é mantida como a fundação sólida deste compilador.