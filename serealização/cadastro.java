/*Crie um exemplo de como funcionam a serialização e a desserialização de um sistema qualquer.
Utilize as classes, os objetos e métodos padrões da Java e insira um endereço físico fictício.*/

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Cadastro {
    public static void main(String[] args) {
        gravadorObject();
    }

    private static void gravadorObject() throws IOException {
        Clinte cliente = new Cliente ("Maria", 29, "12345");
        ObjectOutputStream novoCadastro = new ObjectOutputStream(new FileOutputStream("cliente.ser"));
        novoCadastro.writeObject(cliente);  
        novoCadastro.close();
    }

    private static leitorObject() throws ClassNotFoundException, IOException {
        ObjectInputStream cadastro = new ObjectInputStream(new FileInputStream("cliente.ser"));
        Cliente cliente = cadastro.readObject();  
        cadastro.close();
        return cliente;
    }
}