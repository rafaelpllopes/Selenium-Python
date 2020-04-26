# Estudando Selenium Python
Aprendendo a utilizar o [selenium](https://www.selenium.dev/projects/)

[Curso de Selenium com Python](https://dunossauro.github.io/curso-python-selenium/) de [Eduardo Mendes](https://github.com/dunossauro)

## Configuração do ambiente (Linux)

### Python
- 3.8.2
- [Pyenv](https://github.com/pyenv/pyenv) (github)

#### pyenv

Instalação para ubuntu

1. ```sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev```
2. ```git clone https://github.com/pyenv/pyenv.git ~/.pyenv```
3. ```echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc```
4. ```echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc```
5. ```exec "$SHELL"```
6. ```pyenv install 3.8.2```
7. ```pyenv global 3.8.2```

### Editor
[Atom](https://atom.io/)

1. Baixar e instalar o Atom
2. Abrir Atom
3. Ir nas preferencias e instalar ```platformio-ide-terminal``` (para abrir o terminal ```CTRL + i + "```)

### Navegadores (Browsers)
Instalar os Navegadores

- [Firefox](https://www.mozilla.org/pt-BR/firefox/new/) ```sudo apt install firefox```
- [Chrome](https://www.google.com/intl/pt-BR/chrome/)

### Webdrivers
- [geckoDriver](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0)
1. Baixar o [geckoDriver](https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz)
2. Descompactar ```tar xzvf geckodriver-v0.26.0-linux64.tar.gz```
3. Copiar para /usr/local/bin ```sudo cp geckodriver /usr/local/bin```

- [chromeDriver](https://chromedriver.chromium.org/downloads)
1. Baixar o chromeDriver
2. Descompactar ```unzip chromedriver_linux64.zip```
3. Copiar para /usr/local/bin ```sudo cp chromedriver /usr/local/bin```
4. Testar ```chromedriver```
```ChromeDriver was started successfully```

### Docker
Instalação do [Docker](https://docs.docker.com/engine/install/ubuntu/) no terminal

1. ```sudo apt update```
2. ```sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common```
3. ```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```
4. ```sudo apt-key fingerprint 0EBFCD88```
5. ```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release-cs) stable"```
6. ```sudo apt update```
7. ```sudo apt-get install docker-ce docker-ce-cli containerd.io```
8. ```sudo usermod -aG docker $USER``` opcional
9. ```sudo systemctl enable docker``` opcional
