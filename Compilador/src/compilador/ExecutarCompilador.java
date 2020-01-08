package compilador;
import javax.script.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class ExecutarCompilador {

	private Scanner leitor;

	public void println(String s) {
		System.out.println(s);
	}

	public String compila(Object obj) {
		String exp = ""; 
		TreeNode expr = (TreeNode)obj;
		int nFilhos = expr.childs.length;

		for(int i =0 ; i<nFilhos; i++) {
			exp = exp + compilador((TreeNode)expr.childs[i]);
		}

		return exp;
	}
	public String expressaoEntrada(){
		leitor = new Scanner(System.in);
		String entrada = leitor.nextLine();
		
		entrada = entrada.replaceAll("; ", "\n");
		entrada = entrada.replaceAll(";", "\n");
		return entrada;
	}
	public String compilador(Object obj) {

		if (!(obj instanceof TreeNode))
			throw new RuntimeException("Nao sei avaliar: " + obj);

		String exp = "";
		TreeNode expr = (TreeNode)obj;
		Object childs[] = expr.childs;


		switch (expr.label) {	
		case "T1": 
			exp = exp + "\n" + compilador((TreeNode)childs[0]) + "->" + compilador((TreeNode)childs[1]) + "->" + compilador((TreeNode)childs[2]);
			return exp;

		case "T2":	
		case "T3":
			exp = exp + "\n" + compilador((TreeNode)childs[0]) + "->" + compilador((TreeNode)childs[1]);
			return exp;

		case "STATE":
			return (String)(childs[0]);

		case "EVENT":
			return (String)(childs[0]);
		}

		throw new RuntimeException("Nao sei compilar: "+ expr);
	}


	public int analisador(Object obj) throws ScriptException{
		if (!(obj instanceof TreeNode))
			throw new RuntimeException("Nao sei avaliar, sua entrada nao esta de acordo com nossa linguagem.");

		return 0;
	}

	public void main() throws Exception {
		String exp = "";
		ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
		engine.put("factory", new Factory());
		engine.eval("parser = load('parser.js');");
		String entrada = expressaoEntrada();
		engine.put("src", entrada);
		Object result = engine.eval("parser.parse(src);");
		analisador(result);
		System.out.println("\nCodigo Fonte: \n" + engine.get("src"));
		System.out.println("Arvore = " + result);
		exp = compila((TreeNode)result);
		println("\nResultado: " + exp);
		
		// Escrever a expressao no arquivo para ser lida no python 
		FileWriter arquivo;
		arquivo = new FileWriter(new File("C:\\Users\\Diego Alves\\Desktop\\7º periodo\\Compiladores\\redeDePetri\\exp.txt"));
		arquivo.write(exp);
		arquivo.close();
		//chamaCMD();
	}

	public static void main(String args[]) throws Exception {
		new ExecutarCompilador().main();
	}


}
