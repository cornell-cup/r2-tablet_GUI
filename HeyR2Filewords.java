import java.util.HashSet;
import java.util.Set;

public class HeyR2Filewords {
  public static void main(String[] args) {
    String words = "ai2,hey r2,zr2,,airtel,naruto,airtel,airtel,airtel,ar jail,hey r2,hey r2,ar2,they are two,zr2,ar2,hey r2,ar2,ar-10,hey r2,hey arthur,ar2,q38,q38,ko2,hey r2,you are two,hey r2,hey r2,halo 2,rdr2 hello,hey or two,or to blue,yo are two";
    String[] arr = words.split("\\s*,\\s*");
    Set<String> set = new HashSet();
    for (String s : arr)
      set.add(s);
    System.out.print("[");
    for (String s : set)
      System.out.print(s + ",");
    System.out.print("]");
  }
}
