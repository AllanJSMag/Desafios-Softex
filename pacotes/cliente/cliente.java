package cliente;

public class cliente 
{
    private String nome;
    private int idade;
    private float cpf;
    
    public Cliente(String nome, int idade, int cpf) throws Exception
    {
        set_idade(idade);
        this.nome = nome;
        this.cpf = cpf;
    }
    
    public void set_idade(int idade) throws Exception
    {
        if (0 > idade || idade > 120 )
            throw new Exception("Idade inválida");
        this.idade = idade;
    }
    
    public String get_nome()
    {
        return this.nome;
    }
    
    public int get_idade()
    {
        return this.idade;
    }
    
    public float get_cpf()
    {
        return this.cpf;
    }
    
}