public class JAVA_MAN {
  public static void main(String[] args) {
    for (int x = 10; x >= 1; x--) {
      System.out.println(x);
      if (x == 1) {
        try {
          Thread.sleep(1000);
        } catch (InterruptedException ex) {}
	  System.out.println("tite");
      }
      try {
        Thread.sleep(1000);
      } catch (InterruptedException ex) {}
    }
  }
}