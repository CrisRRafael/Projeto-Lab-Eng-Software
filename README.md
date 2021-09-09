# Projeto Laboratório de Engenharia de Software

Descrição das pastas:

- src: código-fonte do projeto

## Para construir e executar o projeto (Ubuntu / Terminal):

Criar uma pasta vazia em um local desejado 

Navegue para a pasta criada

Clonar o repositório com:

```
git clone https://github.com/CrisRRafael/Projeto-Lab-Eng-Software.git
```

Execute os comandos abaixo para criar e iniciar a venv.

```bash
$ python3 -m venv venv

$ source venv/bin/activate activate
```

Navegar para a pasta Projeto-Lab-Eng-Software

```bash
cd Projeto-Lab-Eng-Software
```

Instalar as dependências com:

```bash
pip install -r requirements.txt
```

Navegar para src/

```bash
cd src
```

 E executar:

```jsx
python app.py
```

Abrir o navegador e acessar a URL informada no terminal

Para desativar o ambiente virtual execute o comando

```bash
deactivate
```


## Para construir e executar o projeto (Windows / prompt de comandos):

Criar uma pasta vazia em um local desejado 

Clonar o repositório com:

```bash
git clone https://github.com/CrisRRafael/Projeto-Lab-Eng-Software.git
```

Criar um ambiente virtual com:

	virtualenv ENV

Ir para o caminho ENV/Scripts

```bash
cd ENV/Scripts
```

Ativar o ambiente virtual

```bash
activate.bat
```

Voltar a pasta projetos

```bash
cd ..
cd ..
```

Navegar para a pasta Projeto-Lab-Eng-Software

```bash
cd Projeto-Lab-Eng-Software
```

Instalar as dependências com:

```bash
pip install -r requirements.txt
```

Navegar para src/

```
cd src
```

 E executar:

```jsx
python app.py
```

Abrir o navegador e acessar a URL informada no prompt de comando.
