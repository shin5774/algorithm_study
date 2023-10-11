import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class p5568 {
    public static int n, k;
    public static ArrayList<String> arr = new ArrayList<>();
    public static Set<String> ans = new HashSet<>();
    public static ArrayList<String> cur = new ArrayList<>();
    public static boolean[] cur_idx;

    public static void back_tracking() { // 순열을 찾는 과정
        if (cur.size() == k) {

            ans.add(String.join("", cur));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (cur_idx[i])
                continue;

            cur.add(arr.get(i));
            cur_idx[i] = true;
            back_tracking();
            cur.remove(cur.size() - 1);
            cur_idx[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            arr.add(br.readLine());
        }

        cur_idx = new boolean[n];
        back_tracking();

        System.out.println(ans.size());
    }
}
