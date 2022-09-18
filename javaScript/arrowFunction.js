/*Crie um programa que contenha os seguintes tipos de funções:
 
1. uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;
2. uma função tradicional com parâmetros e um retorno de valor;
3. uma arrow function com parâmetros e que retorne um valor.
 
Crie um programa que utilize essas três funções de forma lógica, por exemplo: um programa de calculadora.*/
 
 
//função tradicional com a palavra reservada “Function” e sem nenhum parâmetro
function olaMundo () {
    console.log("Olá, mundo!");
}
 
//função tradicional com parâmetro e um retorno de valor
function soma (num1, num2) {
    resultado = num1+num2;
    return resultado;
}
 
//arrow function com parâmetros e que retorne um valor
const texto = (nome, saudacao) => `Olá ${nome}, ${saudacao}!`;