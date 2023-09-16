import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class p2151 {
    public static int n;
    public static char[][] arr;
    public static int[][][] dp;
    public static int[] dx = { -1, 0, 1, 0 };
    public static int[] dy = { 0, 1, 0, -1 };
    public static int[] nd = { 1, -1 };
    public static int[][] doors;

    public static boolean out_range(int x, int y) {
        if (x < 0 || y < 0 || x == n || y == n) {
            return true;
        }

        return false;
    }

    public static void BFS() {
        dp = new int[4][n][n];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], n * n);
            }
        }

        Deque<int[]> q = new LinkedList<>();

        for (int i = 0; i < 4; i++) {
            q.add(new int[] { doors[0][0], doors[0][1], i, 0 });
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == doors[1][0] && cur[1] == doors[1][1]) {
                continue;
            }

            int nx = cur[0] + dx[cur[2]];
            int ny = cur[1] + dy[cur[2]];

            if (out_range(nx, ny) || arr[nx][ny] == '*') {
                continue;
            }

            if (arr[nx][ny] == '!') {
                for (int i = 0; i < 2; i++) {
                    int n_dir = cur[2] + nd[i];

                    if (n_dir == 4) {
                        n_dir = 0;
                    } else if (n_dir < 0) {
                        n_dir = 3;
                    }

                    if (dp[n_dir][nx][ny] > cur[3] + 1) {
                        q.add(new int[] { nx, ny, n_dir, cur[3] + 1 });
                    }

                    dp[n_dir][nx][ny] = cur[3] + 1;
                }
            }

            if (dp[cur[2]][nx][ny] > cur[3]) {
                q.addFirst(new int[] { nx, ny, cur[2], cur[3] });
                dp[cur[2]][nx][ny] = cur[3];
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new char[n][n];
        doors = new int[2][2];
        int idx = 0;
        int ans = n * n;

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = s.charAt(j);

                if (arr[i][j] == '#') {
                    doors[idx][0] = i;
                    doors[idx][1] = j;
                    idx += 1;
                }
            }
        }

        BFS();

        for (int i = 0; i < 4; i++) {
            ans = Math.min(ans, dp[i][doors[1][0]][doors[1][1]]);
        }

        System.out.println(ans);
    }
}
