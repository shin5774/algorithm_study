import java.io.*;
import java.util.*;

public class p9663 {
    public static int n, ans = 0;
    public static List<Integer> cur = new ArrayList<>();

    public static boolean promising(int y) {
        for (int nx = 0; nx < cur.size(); nx++) {
            if (cur.get(nx) == y || cur.size() - nx == Math.abs(cur.get(nx) - y)) {
                return false;
            }
        }

        return true;
    }

    public static void back_tracking() {
        if (cur.size() == n) {
            ans += 1;
            return;
        }

        for (int i = 0; i < n; i++) {
            if (promising(i)) {
                cur.add(i);
                back_tracking();
                cur.remove(cur.size() - 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        back_tracking();

        System.out.println(ans);
    }
}
