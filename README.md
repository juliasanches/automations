# Ransomware Lab

Este repositório é estudo prático sobre o funcionamento de ransomware, desenvolvido para fins de pesquisa e aprendizado. O objetivo é a criação e análise de scripts de ransomware que utilizam criptografia simétrica, bem como técnicas para aumentar a evasão de detecção. Trata-se de um projeto pessoal em andamento, portanto pretendo alterar muitas das funcionalidades que ainda são bem simples. 

## Objetivo do Projeto

O principal objetivo deste projeto é entender e testar o funcionamento de ransomware em um ambiente seguro. Por isso ele contém a funcionalidade de criptograr e descriptografar na mesma estrutura. Como parte dos estudos, pretendo desenvolver e explorar técnicas mais de persistência, obfuscação de código e métodos de comunicação com um servidor de comando e controle (C2).

## Estrutura

O projeto está estruturado da seguinte maneira:

* ``pseudoransomware.py``: O código principal do ransomware. Contém funções para criptografia e descriptografia de arquivos no sistema usando a biblioteca cryptography (Fernet).

* ``key.key``: Arquivo onde a chave de criptografia é armazenada. A chave é gerada automaticamente pelo script na primeira execução.

* ``README.md``: Este arquivo com as informações do projeto.

## Como Usar

### 1. Dependências

`` pip install cryptography `` 

### 2. Executar o script

Clone este repositório e execute o script pseudoransomware.py. 

`` git clone https://github.com/juliasanches/ransomware-lab.git``

``cd ransomwware-lab``

``python pseudoransomware.py`` 

## O que esperar

Por padrão, o script criptografará todos os arquivos no diretório escolhido. Fique a vontade para alterar este comportamento e escolher quais tipos de arquivos serão modificados. 

## Aviso Legal

Este projeto é estritamente para fins educacionais e de pesquisa. O uso indevido de ransomware ou qualquer parte deste código fora de ambientes de teste pode resultar em consequências legais graves. Utilize este estudo de forma responsável.
