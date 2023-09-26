import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.math.BigInteger;

public class p2407 {
    public static BigInteger factorial(int n) {
        BigInteger cur = new BigInteger("1");

        for (int i = 2; i <= n; i++) {
            cur = cur.multiply(new BigInteger(Integer.toString(i)));
        }

        return cur;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        System.out.println(factorial(n).divide(factorial(m)).divide(factorial(n - m)));
    }
}
