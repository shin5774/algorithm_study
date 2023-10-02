import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p17252 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        if (n == 0) {
            System.out.println("NO");
            return;
        }

        while (n != 0) {
            if (n % 3 > 1) {
                break;
            }
            n /= 3;
        }

        if (n == 0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
