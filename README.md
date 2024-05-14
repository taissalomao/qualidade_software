

## Configuração do ambiente

Antes de começar, certifique-se de que tenha feito o clone desse repositório.


1. **Crie um ambiente virtual**:

    No terminal, execute o seguinte comando na raiz do projeto para criar um ambiente virtual chamado `venv`:

    ```shell
    python -m venv venv
    ```

2. **Ative o ambiente virtual**:

    - No Windows:

        ```shell
        venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```shell
        source venv/bin/activate
        ```

## Instalação de dependências

Com o ambiente virtual ativo, instale as dependências necessárias para executar os testes:

```shell
pip install -r requirements.txt
```

## Execução dos testes

 Navegue até o diretório test e execute o comando:

    ```shell
    pytest 
    ```
