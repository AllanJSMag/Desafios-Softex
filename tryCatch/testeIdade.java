import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner;


class IdadeAtual
{
	public static void main (String[] args) throws java.lang.Exception{
		int anoAtual = 2022;
		int correto = 0;
		
		while (correto == 0){
			try{
				Scanner anoNasc = new Scanner(System.in);
				int ano;
				System.out.printf("Informe o ano de nascimento: ");
				ano = anoNasc.nextInt();
				
				if (1921 < ano < 2023){
					int idade = anoAtual - ano;
					correto = 1;
				}
			}
			catch (Exception e){
					System.out.println("Informe o ano de nascimento entre 1922 e 2022." + e.getMessage());
				}
				
			System.out.println("Sua idade é " + idade + " anos.");
		}
	
	}
}