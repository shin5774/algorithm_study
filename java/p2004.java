import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class p2004 {

    public static int find(long n, int x) {
        int cnt = 0;

        while (n > 0) {
            n /= x;
            cnt += n;
        }

        return cnt;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());

        int two = find(n, 2) - find(m, 2) - find(n - m, 2);
        int five = find(n, 5) - find(m, 5) - find(n - m, 5);

        System.out.println(Math.max(Math.min(two, five), 0));

    }
}
