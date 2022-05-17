# História de usuário - Pagamento do pedido

Eu, enquanto **cliente**, desejo **realizar o pagamento 
do meu pedido**, de modo
que eu **possa ter minha compra efetivada**.

## Critérios de aceitação

1. O pagamento deve ser feito através de um **cartão de crédito** ou **vale refeição**.
2. O sistema deve permitir que o cliente selecione o meio de pagamento.
3. O sistema deve permitir que o cliente possa cadastrar mais um meio de pagamento
4. O sistema deve permitir que o cliente possa remover um meio de pagamento.
5. O sistema deve consultar a operadora de cartão de crédito para verificar se o cartão é válido.
6. O sistema deve consultar a operadora de cartão de crédito para verificar se o cartão está ativo.
7. O sistema deve consultar a operadora de cartão de crédito para verificar se o cartão está bloqueado.
8. O sistema deve consultar a operadora de cartão de crédito para verificar se o cartão está vencido.
9. O sistema deve consultar a operadora de cartão de crédito para verificar se o cartão está com saldo insuficiente.
10. O sistema deve avisar que o pagamento foi realizado com sucesso.

## Detalhes de implementação

1. A consulta da validade do cartão deve usar a API xpto.