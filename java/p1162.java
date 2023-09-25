import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1162 {
    public static int[] arr;
    public static int n, s;
    public static int ans = 0;

    public static void back_tracking(int cur, int idx, int len) {
        if (idx == n) {
            if (cur == s && len != 0) {
                ans += 1;
            }

            return;
        }

        back_tracking(cur + arr[idx], idx + 1, len + 1);
        back_tracking(cur, idx + 1, len);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        back_tracking(0, 0, 0);

        System.out.println(ans);
    }
}
