import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p14499 {
    public static int swap(int a, int b) {
        return a;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][m];
        int[][] mv = { { 0, 1 }, { 0, -1 }, { -1, 0 }, { 1, 0 } };
        int up = 0, down = 0, left = 0, right = 0, uup = 0, ddown = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < k; i++) {
            int cmd = Integer.parseInt(st.nextToken()) - 1;
            int nx = x + mv[cmd][0], ny = y + mv[cmd][1];

            if (nx < 0 || ny < 0 || nx == n || ny == m) {
                continue;
            }

            x = nx;
            y = ny;

            switch (cmd) {
                case 0:
                    down = swap(right, right = down);
                    right = swap(up, up = right);
                    left = swap(up, up = left);
                    break;
                case 1:
                    down = swap(left, left = down);
                    left = swap(up, up = left);
                    right = swap(up, up = right);
                    break;
                case 2:
                    uup = swap(up, up = uup);
                    up = swap(ddown, ddown = up);
                    ddown = swap(down, down = ddown);
                    break;
                case 3:
                    ddown = swap(down, down = ddown);
                    up = swap(ddown, ddown = up);
                    uup = swap(up, up = uup);
                    break;
            }

            if (arr[x][y] == 0) {
                arr[x][y] = down;
            } else {
                down = arr[x][y];
                arr[x][y] = 0;
            }

            System.out.println(up);
        }

    }
}
