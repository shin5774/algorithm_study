import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
import java.math.BigInteger;

public class p1256 {
    public static BigInteger factorial(int n) {
        BigInteger x = new BigInteger("1");
        for (int i = 2; i <= n; i++) {
            x = x.multiply(new BigInteger(Integer.toString(i)));
        }

        return x;
    }

    public static BigInteger calc(int n, int m) {
        return factorial(n + m).divide(factorial(n).multiply(factorial(m)));
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        BigInteger k = new BigInteger(st.nextToken());
        ArrayList<String> ans = new ArrayList<>();

        if (k.compareTo(calc(n, m)) == 1) {
            System.out.println(-1);
            return;
        }
        while (k.compareTo(new BigInteger("1")) == 1) {
            BigInteger up = calc(n - 1, m);
            if (k.compareTo(up) == 1) {
                k = k.subtract(up);
                m -= 1;
                ans.add("z");
            } else {
                n -= 1;
                ans.add("a");
            }
        }

        for (int i = 0; i < n; i++) {
            ans.add("a");
        }
        for (int i = 0; i < m; i++) {
            ans.add("z");
        }

        System.out.println(String.join("", ans));

    }
}
