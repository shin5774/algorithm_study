import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1300 {
    public static int n;
    public static int k;

    public static boolean check(int x) {
        int cnt = 0;

        for (int i = 1; i <= n; i++) {
            cnt += Math.min(n, x / i);
        }

        return cnt >= k;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        int low = 1;
        int high = k;

        while (low + 1 < high) {
            int mid = (low + high) / 2;

            if (check(mid)) {
                high = mid;
            } else {
                low = mid;
            }
        }

        System.out.println(high);
    }
}
