import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner;

public class CalIdade {
    public Integer anoAtual;
    public Integer anoNasc;
    public Integer idade;
    
    public CalIdade (Integer anoAtual, Integer anoNasc){
        
        if ((1922 > anoNasc) && (anoNasc > 2022)) {
            throw new RuntimeException("Informe o ano de nascimento entre 1922 e 2022.");
        }    
        this.anoAtual = anoAtual;
        this.anoNasc = anoNasc;
        this.idade = idade;
    }
    
    public int idadeAtual() {
        idade = anoAtual - anoNasc;
        return idade;
    }
}

class IdadeAtual
{
	public static void main (String[] args) throws java.lang.Exception{
		int anoAtual = 2022;
		Scanner anoNasc = new Scanner(System.in);
		int ano;
		System.out.printf("Informe o ano de nascimento: ");
		ano = anoNasc.nextInt();
		
		try{
		    Idade i = new CalIdade(anoAtual, ano);
			
			System.out.println("Sua idade é " + i.iadeAtual() + " anos.");
		}
		catch (RuntimeException e){
				System.out.println(e.getMessage());
			}
	}
}