import java.io.*;
import java.util.*;

public class p15650 {
    public static List<Integer> ans = new ArrayList<>();
    public static List<Integer> arr = new ArrayList<>();
    public static int n, m;

    public static void back_tracking(int prev) {
        if (ans.size() == m) {
            for (int x : ans) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }

        if (m - ans.size() > n - 1 - prev) {
            return;
        }

        for (int idx = prev + 1; idx < n; idx++) {
            ans.add(arr.get(idx));
            back_tracking(idx);
            ans.remove(ans.get(ans.size() - 1));
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            arr.add(i);
        }

        back_tracking(-1);
    }
}
