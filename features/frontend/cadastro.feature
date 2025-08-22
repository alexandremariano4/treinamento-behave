# language:pt

Funcionalidade: Cadastrar novo entregador para o Buger Eats

    @success
    Esquema do Cenário: Cadastro de um novo entregador na plataforma com sucesso
        Dado Está na tela principal do sistema
        E Clicar no botão "Cadastre-se para fazer entregas"
        Quando Preenche o formulário de Cadastro
        E Envia a imagem da CNH
        Então Deve ser exibido uma mensagem de sucesso "<result>"

    Exemplos:
    |name |     cpf   |     email     |  phone    |   cep  |number| complement | delivery_method |result                                                                                             |
    |Teste|00000014141|teste@gmail.com|31984976025|66833620| 78   | complemento| Moto            |Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato.|

    @failure @cpf @nome @endereco
    Esquema do Cenário: Cadastro de um novo entregador na plataforma com dados inválido
        Dado Está na tela principal do sistema
        E Clicar no botão "Cadastre-se para fazer entregas"
        Quando Preenche o formulário de Cadastro
        E Envia a imagem da CNH
        Então Deve ser exibido uma mensagem de erro "<result>"

    Exemplos:
    |name |     cpf   |     email     |  phone    |   cep  |number| complement |delivery_method| result           |
    |Teste|abcefghijkl|teste@gmail.com|31984976025|66833620| 78   | complemento|Moto           |Oops! CPF inválido|
    |     |00000014141|teste@gmail.com|31984976025|66833620| 78   | complemento|Bicicleta      |É necessário informar o nome|
    |Teste|00000014141|teste@gmail.com|31984976025|66833620|      | complemento|Van/Carro      |É necessário informar o número do endereço|

    @failure @email @popup
    Esquema do Cenário: Cadastro de um novo entregador na plataforma com email inválido
        Dado Está na tela principal do sistema
        E Clicar no botão "Cadastre-se para fazer entregas"
        Quando Preenche o formulário de Cadastro
        E Envia a imagem da CNH
        Então Deve ser exibido uma mensagem popup de erro "<result>"

    Exemplos:
    |name |     cpf   |     email     |  phone    |   cep  |number| complement |delivery_method| result           |
    |Teste|abcefghijkl|     teste     |31984976025|66833620| 78   | complemento|  Moto         |Inclua um "@" no endereço de e-mail. "teste" está com um "@" faltando.|
    