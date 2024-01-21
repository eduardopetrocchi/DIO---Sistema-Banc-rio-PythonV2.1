# Sistema Bancário em Python

Este é um simples sistema bancário em Python que permite a realização de depósitos, saques, consulta de extrato, cadastro de clientes, criação de contas e listagem de contas. O sistema utiliza programação orientada a objetos para modelar clientes, contas bancárias e transações.

## Classes Principais

### `Cliente`

A classe `Cliente` representa um cliente do banco e contém informações básicas, como endereço e uma lista de contas associadas.

### `PessoaFisica`

A classe `PessoaFisica` herda de `Cliente` e representa uma pessoa física. Ela adiciona informações específicas, como nome, data de nascimento e CPF.

### `Conta`

A classe `Conta` representa uma conta bancária genérica e inclui métodos para depósito, saque e acesso ao histórico de transações.

### `ContaCorrente`

A classe `ContaCorrente` herda de `Conta` e adiciona características específicas de uma conta corrente, como limite de saque e limite de operações por mês.

### `Historico`

A classe `Historico` mantém um registro de todas as transações realizadas em uma conta.

### `Transacao` (interface abstrata)

A classe abstrata `Transacao` define a estrutura básica de uma transação, incluindo métodos abstratos para obter o valor da transação e registrar a transação em uma conta.

### `Saque` e `Deposito`

As classes `Saque` e `Deposito` implementam a interface `Transacao` e representam, respectivamente, operações de saque e depósito.

## Funções Principais

### `menu()`

A função `menu()` exibe um menu interativo para o usuário, permitindo a escolha de diversas operações.

### `depositar(clientes)`

A função `depositar(clientes)` realiza a operação de depósito, solicitando informações do cliente e valor a ser depositado.

### `sacar(clientes)`

A função `sacar(clientes)` realiza a operação de saque, solicitando informações do cliente e valor a ser sacado.

### `exibir_extrato(clientes)`

A função `exibir_extrato(clientes)` exibe o extrato de uma conta, mostrando todas as transações realizadas.

### `criar_cliente(clientes)`

A função `criar_cliente(clientes)` permite cadastrar um novo cliente, solicitando informações como CPF, nome, data de nascimento e endereço.

### `listar_contas(contas)`

A função `listar_contas(contas)` exibe informações detalhadas de todas as contas criadas.

### `criar_conta(numero_conta, clientes, contas)`

A função `criar_conta(numero_conta, clientes, contas)` cria uma nova conta, associando-a a um cliente existente.

### `filtrar_cliente(cpf, clientes)`

A função `filtrar_cliente(cpf, clientes)` filtra um cliente pelo CPF na lista de clientes.

### `recuperar_conta_cliente(cliente)`

A função `recuperar_conta_cliente(cliente)` recupera a primeira conta associada a um cliente.

### `main()`

A função `main()` é o ponto de entrada principal do programa, onde o loop principal do menu é executado até que o usuário escolha sair.

## Utilização

Para utilizar o sistema, execute o programa e siga as opções do menu. Insira as informações solicitadas para realizar operações como depósito, saque, consulta de extrato, cadastro de cliente, criação de contas e listagem de contas.

Esperamos que este sistema bancário simples em Python seja útil para entender os conceitos básicos de programação orientada a objetos e interação com o usuário em um ambiente de terminal.
## Autores

- [@eduardopetrocchi](https://www.github.com/eduardopetrocchi)

