package compilador;

public class TreeNode {
	public String label;
	public Object childs[];
	public TreeNode(String lbl, Object childs[]) {
		//System.out.println("Construtor chamado...");
		this.label = lbl;
		this.childs = childs;
	}
	public String toString() {
		String result = label + "[ ";
		for (int c=0;c<childs.length;c++) {
			if (c>0) result += " , ";
			result += childs[c];
		}
		result += " ]";
		return result;
	}
}
