package compilador;

public class Factory {
   public TreeNode criaNo(String info, Object filhos[]) {
	   return new TreeNode(info,filhos);
   }
}
