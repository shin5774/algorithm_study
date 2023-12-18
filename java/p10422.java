import java.io.*;
import java.util.*;

public class p10422 {
    public static long[] dp = new long[5001];

    public static void calculate() {
        dp[0] = 1;

        for (int x = 2; x <= 5000; x += 2) {
            long cur = 0;
            for (int i = 0; i < x; i += 2) {
                cur += (dp[i] * dp[x - 2 - i]);
                cur %= 1000000007;
            }
            dp[x] = cur;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        calculate();

        for (int i = 0; i < t; i++) {
            int l = Integer.parseInt(br.readLine());
            System.out.println(dp[l]);
        }

    }
}
