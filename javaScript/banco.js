/*Crie um código com um objeto chamado “Banco”. 
Ele deverá ter propriedades que incluem conta, saldo, tipo de conta e agência e os seus métodos devem ser: 
buscar saldo, depósito, saque e número da conta.

Observações:
- buscar saldo deve retornar o valor atual do saldo;
- para o depósito, você deverá passar um valor como parâmetro e adicioná-lo no saldo final do objeto;
- para o saque, você deverá passar um valor como parâmetro e subtraí-lo no saldo final do objeto;
- o número da conta deve retornar o número da conta.*/

// criando objeto
function Banco(conta, tipoConta, agencia, saldo) {
    this.conta = conta;
    this.tipoConta = tipoConta;
    this.agencia = agencia;
    this.saldo = saldo;
    
    buscarSaldo = function saldoAtual() {
        console.log (this.saldo);
    }

    deposito = function deposito(valorDeposito) {
        this.valorDeposito = valorDeposito;
        novoSaldoD = this.saldo + this.valorDeposito;
        this.saldo = novoSaldoD;
    }

    saque = function saque(valorSaque) {
        this.valorSaque = valorSaque;
        novoSaldoS = this.saldo + this.valorSaque;
        this.saldo = novoSaldoS;
    }

    numeroConta = function numeroConta() {
        console.log (this.conta);
    }
}
