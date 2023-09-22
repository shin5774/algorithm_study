import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p3109 {
    public static int r, c;
    public static char[][] arr;
    public static int[] mv = { -1, 0, 1 };

    public static boolean dfs(int x, int y) {
        arr[x][y] = 'x';

        if (y == c - 1) {
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nx = x + mv[i];

            if (nx < 0 || nx == r || arr[nx][y + 1] == 'x') {
                continue;
            }

            if (dfs(nx, y + 1)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int ans = 0;
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        arr = new char[r][c];

        for (int i = 0; i < r; i++) {
            String input = br.readLine();

            for (int j = 0; j < c; j++) {
                arr[i][j] = input.charAt(j);
            }
        }

        for (int i = 0; i < r; i++) {
            if (dfs(i, 0)) {
                ans += 1;
            }
        }

        System.out.println(ans);
    }
}
