import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1614 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long lim = Long.parseLong(br.readLine());
        long ans;

        if (n == 1 || n == 5) {
            ans = n + lim * 8;
        } else {
            ans = n + lim * 4;

            if (lim % 2 != 0) {
                ans -= 2 * n - 6;
            }
        }

        System.out.println(ans - 1);
    }
}
