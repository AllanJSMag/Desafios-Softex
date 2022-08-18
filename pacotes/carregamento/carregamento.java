package carregamento;

public class Carregamento 
{
    private int codigo;
    private String nome;
    private float preco;
    private float peso;
    
    public Produto(int codigo, String nome, float preco, float peso) throws Exception
    {
        set_codigo(codigo);
        set_nome(nome);
        set_preco(preco);
        set_peso(peso);
    }
    
    private void set_codigo(String new_codigo) throws Exception
    {
        int codigo_len = new_codigo.length();
        if ( codigo_len != 12)
            throw new Exception("O código do produto deve possuir 12 algarismos");
        this.codigo = new_codigo.toUpperCase();
    }

    private void set_nome(String new_name)
    {
        this.nome = new_name;
    }
    
    private void set_preco(float new_preco) throws Exception
    {
        if (new_preco < 0)
            throw new Exception("O preço do produto inválido!");
        this.preco = new_preco;
    }
    
    private void set_peso(float peso) throws Exception
    {
        if (peso < 0)
            throw new Exception("O peso do carregamento tem que ser positivo!");
        this.peso = peso;
    }
    
    public String set_codigo()
    {
        return this.codigo;
    }
        
    public String set_name()
    {
        return this.nome;
    }
    
    public float set_preco()
    {
        return this.preco;
    }
    
    public int set_peso()
    {
        return this.peso;
    }
    
}