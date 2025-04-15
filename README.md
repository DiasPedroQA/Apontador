# 📁 Apontador

**Apontador** é um aplicativo multiplataforma desenvolvido com **Kivy** e **KivyMD**, utilizando os princípios de **TDD (Test-Driven Development)** e arquitetura **MVC (Model-View-Controller)**. O objetivo do projeto é oferecer uma ferramenta gráfica capaz de **identificar, analisar e manipular caminhos de arquivos e diretórios**, reconhecendo automaticamente o sistema operacional ao qual o caminho pertence (Windows, Linux ou macOS), e aplicando as regras apropriadas de identificação e sanitização.

---

## 🎯 Objetivo

Criar um analisador robusto de caminhos com:

- Detecção automática do sistema operacional a partir da string do caminho.
- Identificação sintática e semântica de caminhos.
- Mensagens claras de erro e sucesso.
- Interface gráfica amigável com KivyMD.
- Arquitetura modular com boas práticas de engenharia de software.

---

## 🧱 Estrutura do Projeto

O projeto segue a arquitetura **MVC** com separação clara das responsabilidades:

```plain-text
app/
├── controllers/         # Controladores que conectam view e model
├── models/              # Modelos, identificadores e lógica de negócio
│   ├── identificadores/     # Identificadores específicos por sistema
├── utils/               # Utilitários auxiliares
├── views/               # Interface gráfica com arquivos .kv e Python
├── main.py              # Ponto de entrada do aplicativo
tests/                   # Testes automatizados com pytest
```

---

## 🔨 Desenvolvimento Guiado por Testes (TDD)

O projeto é construído com foco em **Test-Driven Development**:

- Cobertura de testes com `pytest` e `pytest-cov`.
- Testes unitários para cada identificador, controlador e utilitário.
- Parametrização e uso de `mock` para simular ambientes.
- Meta: alcançar 100% de cobertura de código em componentes críticos (`identificador.py`, `controller`, `main`).

---

## 💻 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/Apontador.git
cd Apontador
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Execução

Para iniciar o aplicativo com interface gráfica:

```bash
python main.py
```

---

## ✅ Testes

Execute os testes com relatório de cobertura:

```bash
pytest --cov=app tests/
```

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Abra uma issue ou envie um pull request com sua sugestão ou melhoria.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.
