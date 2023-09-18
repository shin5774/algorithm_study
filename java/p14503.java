import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p14503 {
    public static int n;
    public static int m;
    public static int rx;
    public static int ry;
    public static int rd;
    public static int[][] arr;
    public static int[] dx = { -1, 0, 1, 0 };
    public static int[] dy = { 0, 1, 0, -1 };

    public static boolean out_range(int x, int y) {
        if (x < 0 || y < 0 || x == n || y == m) {
            return true;
        }

        return false;
    }

    public static boolean find_move() {
        for (int i = 0; i < 4; i++) {
            rd -= 1;

            if (rd < 0)
                rd = 3;

            int nx = rx + dx[rd];
            int ny = ry + dy[rd];

            if (out_range(nx, ny))
                continue;

            if (arr[nx][ny] == 0) {
                rx = nx;
                ry = ny;

                return true;
            }

        }

        return false;
    }

    public static boolean back() {
        int d = rd + 2;

        if (d >= 4)
            d -= 4;

        int nx = rx + dx[d];
        int ny = ry + dy[d];

        if (arr[nx][ny] == 1)
            return true;

        rx = nx;
        ry = ny;

        return false;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int ans = 0;

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        st = new StringTokenizer(br.readLine());
        rx = Integer.parseInt(st.nextToken());
        ry = Integer.parseInt(st.nextToken());
        rd = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            if (arr[rx][ry] == 0) {
                arr[rx][ry] = 2;
                ans += 1;
            }

            if (!find_move() && back())
                break;

        }

        System.out.println(ans);
    }

}
