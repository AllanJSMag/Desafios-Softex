/*Crie dois códigos de sistema de notas para uma escola. O primeiro código deve ser um programa que informa
se o aluno reprovou, ou não, com base nas três notas que ele adicionou ao programa.
Utilize, no mínimo, um operador de atribuição e um operador ternário.
O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima
que ele deve tirar na próxima prova para poder passar com nota sete.*/
 
 
function media() {
    var nota1 = parseFloat(document.getElementById("nota1").value);
    var nota2 = parseFloat(document.getElementById("nota2").value);
    var nota3 = parseFloat(document.getElementById("nota3").value);
    var media = ((nota1 + nota2 + nota3)/3);
   
    var resultado = media >=7 ? 'Aprovado':'Reprovado';
    return resultado;
}
 
 
function notaMinima() {
    Var nota1 = parseFloat(document.getElementById("nota1").value);
    Var nota2 = parseFloat(document.getElementById("nota2").value);
    var nota3 = ( 21 - (nota1 + nota2));
    return nota3;
}