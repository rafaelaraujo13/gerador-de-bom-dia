# gerador-de-bom-dia
App para criar imagens de bom dia automaticamente feito em Python

## Como Usar
1. Clone esse repositório e navegue até a pasta `gerador-de-bom-dia`
```bash
git clone https://github.com/rafaelaraujo13/gerador-de-bom-dia.git
cd gerador-de-bom-dia
```
2. Instale as dependências necessárias
```bash
pip install -r requirements.txt
```
3. Vá até a pasta `src/credentials` e crie um arquivo `google.json` seguindo a estrutura do [exemplo](src/credentials/google.example.json)

4. Volte à pasta principal e rode o programa
```bash
python src/main.py
```

5. O arquivo final estará em `src/images/converted.png`

## Como funciona
Ao ser executado, o programa:
1. Seleciona e extrai uma frase aleatória de https://www.mundodasmensagens.com/frases-bom-dia/
2. Busca e faz o download de uma imagem de fundo adequada
3. Mescla a imagem com a frase selecionada
