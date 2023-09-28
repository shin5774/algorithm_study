import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1941 {
    public static String[] arr = new String[5];
    public static int ans = 0;
    public static ArrayList<Integer> cur = new ArrayList<>();
    public static int[] dx = { 1, -1, 0, 0 };
    public static int[] dy = { 0, 0, 1, -1 };
    public static ArrayList<Integer> c_arr;

    public static void check(int idx) {
        int x = idx / 5, y = idx % 5;

        if (c_arr.size() == 7) {
            ans += 1;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            int n_idx = nx * 5 + ny;

            if (nx < 0 || nx == 5 || ny < 0 || ny == 5) {
                continue;
            }

            if (cur.contains(n_idx) && !c_arr.contains(n_idx)) {
                c_arr.add(n_idx);
                check(n_idx);
            }

        }
    }

    public static void back_tracking(int idx, int Y, int cnt) {
        int x = idx / 5;
        int y = idx % 5;

        if (Y > 3 || 25 - idx < 7 - cnt) {
            return;
        }

        if (cnt == 7) {
            c_arr = new ArrayList<>();
            check(cur.get(0));
            return;
        }

        cur.add(idx);
        if (arr[x].charAt(y) == 'Y') {
            back_tracking(idx + 1, Y + 1, cnt + 1);
        } else {
            back_tracking(idx + 1, Y, cnt + 1);
        }
        cur.remove(cnt);

        back_tracking(idx + 1, Y, cnt);

    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            arr[i] = (String) br.readLine();
        }

        back_tracking(0, 0, 0);

        System.out.println(ans);
    }
}
