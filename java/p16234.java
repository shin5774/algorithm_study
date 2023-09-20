import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p16234 {
    public static int n, l, r;
    public static boolean[][] visited;
    public static int[][] arr;
    public static ArrayList<Pos> unions;
    public static int[][] mv = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

    public static class Pos {
        int x;
        int y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static boolean out_range(int x, int y) {
        return (x < 0 || y < 0 || x == n || y == n);
    }

    public static boolean find(int x, int y) {
        unions = new ArrayList<Pos>();
        Deque<Pos> q = new ArrayDeque<Pos>();
        q.add(new Pos(x, y));
        unions.add(new Pos(x, y));
        int u_sum = arr[x][y];
        visited[x][y] = true;

        while (!q.isEmpty()) {
            Pos cur = q.pop();

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + mv[i][0], ny = cur.y + mv[i][1];

                if (out_range(nx, ny) || visited[nx][ny]) {
                    continue;
                }

                int diff = Math.abs(arr[cur.x][cur.y] - arr[nx][ny]);

                if (diff >= l && diff <= r) {
                    q.add(new Pos(nx, ny));
                    unions.add(new Pos(nx, ny));
                    visited[nx][ny] = true;
                    u_sum += arr[nx][ny];

                }
            }
        }

        if (unions.size() == 1) {
            return false;
        }

        for (Pos p : unions) {
            arr[p.x][p.y] = u_sum / unions.size();
        }

        return true;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = 0;

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            visited = new boolean[n][n];
            boolean checker = false;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j]) {
                        checker = find(i, j) || checker;
                    }
                }
            }

            if (!checker) {
                break;
            }

            t += 1;
        }

        System.out.println(t);
    }

}
