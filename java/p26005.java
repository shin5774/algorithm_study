import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p26005 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if (n == 1 || n % 2 == 0) {
            System.out.println(n * n / 2);
        }
        else {
            System.out.println(n * n / 2 + 1);
        }
    }
}
