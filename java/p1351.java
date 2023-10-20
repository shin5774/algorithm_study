import java.util.*;
import java.io.*;

public class p1351 {
    public static Map<Long, Long> dp = new HashMap<>();
    public static long p, q;

    public static Long find(Long x) {
        if (!dp.containsKey(x)) {
            dp.put(x, find(x / p) + find(x / q));
        }

        return dp.get(x);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken()); // long은 10^18까지 표현 가능
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());
        dp.put(Long.valueOf(0), Long.valueOf(1));

        System.out.println(find(n));

    }
}
