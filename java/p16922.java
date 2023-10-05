import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class p16922 {
    public static int n, ans = 0;
    public static int[] adder = { 1, 5, 10, 50 };
    public static boolean[] visited = new boolean[1001];

    public static void back_tracking(int level, int start, int cur) {
        if (level == n) {
            if (!visited[cur]) {
                ans += 1;
                visited[cur] = true;
            }
            return;
        }

        for (int i = start; i < 4; i++) {
            back_tracking(level + 1, i, cur + adder[i]);
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        back_tracking(0, 0, 0);

        System.out.println(ans);
    }
}
