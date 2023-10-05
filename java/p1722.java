import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.*;

public class p1722 {
    public static boolean[] number;
    public static int n;

    public static BigInteger factorial(int n) {
        BigInteger k = new BigInteger("1");

        for (int i = 2; i <= n; i++) {
            k = k.multiply(new BigInteger(Integer.toString(i)));
        }

        return k;
    }

    public static void problem1(BigInteger k) {
        ArrayList<String> ans = new ArrayList<>();

        int cur = n - 1;
        while (k.compareTo(new BigInteger("1")) == 1) {
            BigInteger cur_fact = factorial(cur);

            int cnt = 1;

            while (k.compareTo(cur_fact.multiply(new BigInteger(Integer.toString(cnt)))) == 1) {
                cnt += 1;
            }
            cnt -= 1;

            k = k.subtract(cur_fact.multiply(new BigInteger(Integer.toString(cnt))));

            for (int i = 1; i <= n; i++) {
                if (number[i])
                    continue;

                if (cnt == 0) {
                    ans.add(Integer.toString(i));
                    number[i] = true;
                    break;
                }
                cnt -= 1;
            }

            cur -= 1;
        }

        for (int i = 1; i <= n; i++) {
            if (number[i])
                continue;
            ans.add(Integer.toString(i));
        }

        System.out.println(String.join(" ", ans));
    }

    public static void problem2(int[] input) {
        BigInteger ans = new BigInteger("1");

        for (int i = 0; i < n - 1; i++) {
            int target = input[i];
            int cnt = 0;

            for (int j = 1; j <= n; j++) {
                if (number[j])
                    continue;
                if (j == target) {
                    number[j] = true;
                    ans = ans.add(factorial(n - i - 1).multiply(new BigInteger(Integer.toString(cnt))));
                    break;
                }

                cnt += 1;
            }
        }

        System.out.println(ans);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        number = new boolean[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int op = Integer.parseInt(st.nextToken());

        if (op == 1) {
            problem1(new BigInteger(st.nextToken()));
        } else {
            int[] input = new int[n];
            for (int i = 0; i < n; i++) {
                input[i] = Integer.parseInt(st.nextToken());
            }

            problem2(input);
        }
    }
}
