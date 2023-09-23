import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p11051 {
    public static int P = 10007;

    public static int factorial(int x) {
        int cur = 1;

        while (x > 1) {
            cur *= x;
            cur %= P;
            x--;
        }

        return cur;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int n_fact = factorial(n);
        int alpha = (factorial(k) * factorial(n - k)) % P;
        int alpha_calc = 1;
        int a_pow = P - 2;

        while (a_pow > 0) {
            if (a_pow % 2 == 0) {
                alpha *= alpha;
                alpha %= P;
                a_pow /= 2;
            } else {
                alpha_calc *= alpha;
                alpha_calc %= P;
                a_pow -= 1;
            }
        }

        System.out.println((n_fact * alpha_calc) % P);
    }

}
