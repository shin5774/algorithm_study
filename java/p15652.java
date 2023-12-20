import java.io.*;
import java.util.*;

public class p15652 {
    public static int n, m;
    public static List<Integer> cur = new ArrayList<>();

    public static void back_tracking(int prev) {
        if (cur.size() == m) {
            for (int x : cur) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }

        for (int i = prev; i <= n; i++) {
            cur.add(i);
            back_tracking(i);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        back_tracking(1);
    }
}
