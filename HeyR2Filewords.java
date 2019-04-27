import java.util.HashSet;
import java.util.Set;
public class Bose {
	public static void main(String[] args) {
		String words = "ai2,hey r2,zr2,,airtel,naruto,airtel,airtel,airtel,ar jail,hey r2,hey r2,ar2";
		String[] arr = words.split("\\s*,\\s*");
		Set<String> set = new HashSet();
		for(String s: arr) set.add(s);
		for(String s : set) System.out.println(s);
	}
}
