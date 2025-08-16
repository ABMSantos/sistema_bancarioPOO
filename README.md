# sistema_bancarioPOO
Descrição Geral:
Este projeto consiste em um sistema bancário simulado, desenvolvido em Python, que permite a criação e gerenciamento de contas correntes de clientes. O sistema segue uma abordagem orientada a objetos (OO), utilizando classes para representar clientes, contas, transações e histórico de movimentações.

Objetivos do Projeto:

Implementar funcionalidades básicas de um banco, como depósito, saque e visualização de extrato.

Gerenciar múltiplos clientes e contas, mantendo histórico de transações.

Garantir que cada cliente tenha login único e operações seguras.

Trabalhar conceitos de POO, herança, polimorfismo, encapsulamento e abstração.

Criar uma experiência de usuário interativa via terminal, com menus claros e instruções.

Funcionalidades Implementadas:

Cadastro de Usuários:

Validação de CPF (11 dígitos) e data de nascimento.

Preenchimento completo de endereço (logradouro, número, bairro, cidade, estado).

Login e Logout:

Usuário pode logar uma única vez e realizar múltiplas operações sem precisar digitar CPF novamente.

Logout retorna o usuário ao menu inicial.

Gerenciamento de Conta Corrente:

Cada cliente pode ter uma ou mais contas.

Limite diário de saque e número máximo de saques por dia.

Histórico detalhado de transações (depósitos e saques).

Operações Bancárias:

Depósito: adiciona saldo à conta do cliente.

Saque: retira saldo da conta, respeitando limites e saldo disponível.

Extrato: exibe todas as transações realizadas e saldo atual.

Listagem de contas: exibe todas as contas existentes no banco, com titular e agência.

Banco Simulado:

Nome do banco: ABMS

Todas as contas criadas pertencem ao banco ABMS.

Diferenciais do Projeto:

Interface de menu clara e responsiva no terminal.

Sistema de validação robusto (CPF, data de nascimento, campos obrigatórios).

Persistência de usuário em memória enquanto o sistema estiver em execução, permitindo múltiplas operações sem redigitar dados.

Estrutura escalável, permitindo facilmente a adição de novas funcionalidades como transferências entre contas ou juros.

Tecnologias e Conceitos Utilizados:

Linguagem: Python 3

Paradigma: Programação Orientada a Objetos

Conceitos: Herança, Polimorfismo, Encapsulamento, Abstração, Interfaces (ABC)

Bibliotecas: datetime (para validar datas), textwrap (para formatar menus)

Se você quiser, posso também fazer uma versão resumida e direta, ótima para colocar no GitHub ou em portfólio, com 3-4 parágrafos, que já deixa claro que é seu projeto de Engenharia de Software.

Quer que eu faça essa versão resumida também?

Você disse:
quero uma para o READme
O ChatGPT disse:

Perfeito, Ana! Vou montar uma versão enxuta, clara e profissional do README, adequada para GitHub ou portfólio:

Sistema Bancário ABMS
Descrição

O Sistema Bancário ABMS é um projeto em Python que simula operações básicas de um banco, utilizando programação orientada a objetos (POO). O sistema permite criar clientes e contas correntes, realizar depósitos, saques, consultar extrato e manter histórico detalhado das transações.

Funcionalidades

Cadastro de usuários com validação de CPF, data de nascimento e endereço completo.

Login único para cada cliente, permitindo múltiplas operações sem redigitar CPF.

Criação e gerenciamento de contas correntes, com limite de saque diário e número máximo de saques.

Registro e exibição de histórico de transações.

Listagem de todas as contas do banco ABMS.

Tecnologias e Conceitos

Linguagem: Python 3

Paradigma: Programação Orientada a Objetos

Conceitos: Herança, Polimorfismo, Encapsulamento, Abstração, Interfaces (ABC)

Bibliotecas: datetime (validação de datas), textwrap (formatação de menus)

Uso

Clone o repositório:

git clone <url-do-repositorio>


Execute o script principal:

python main.py


Use o menu interativo para criar usuários, logar, abrir contas, depositar, sacar e consultar extratos.

Observações

O sistema mantém os dados em memória durante a execução.

Limite de saque por operação: R$500,00.

Banco simulado: ABMS.
