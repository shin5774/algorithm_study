import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.math.*;

public class p10164 {

    public static BigInteger factorial(int n) {
        BigInteger cur = new BigInteger("1");

        for (int i = 2; i <= n; i++) {
            cur = cur.multiply(new BigInteger(Integer.toString(i)));
        }

        return cur;
    }

    public static BigInteger find(int sx, int sy, int dx, int dy) {
        int down = dx - sx, right = dy - sy;

        return factorial(right + down).divide(factorial(right).multiply(factorial(down)));
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        if (k == 0) {
            System.out.println(find(0, 0, n - 1, m - 1));
        } else {
            int ox = k / m;
            int oy = k % m - 1;

            if (oy == -1) {
                ox -= 1;
                oy = m - 1;
            }

            System.out.println(find(0, 0, ox, oy).multiply(find(ox, oy, n - 1, m - 1)));
        }

    }
}
