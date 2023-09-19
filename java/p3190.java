import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p3190 {
    public static int n;
    public static int[][] arr;
    public static Deque<String[]> change_dir;
    public static Deque<int[]> snake_pos;
    public static int[][] mv = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

    public static boolean out_range(int x, int y) {
        if (x < 0 || y < 0 || x == n || y == n) {
            return true;
        }

        return false;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        change_dir = new ArrayDeque<>();
        snake_pos = new ArrayDeque<>();

        n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        int t = 0;
        int dir = 1;

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[x - 1][y - 1] = 1;
        }

        int l = Integer.parseInt(br.readLine());

        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            String ct = st.nextToken();
            String cd = st.nextToken();
            change_dir.add(new String[] { ct, cd });
        }

        arr[0][0] = -1;
        snake_pos.add(new int[] { 0, 0 });

        while (true) {
            t += 1;
            // move
            int[] cur = snake_pos.peekLast();
            int nx = cur[0] + mv[dir][0];
            int ny = cur[1] + mv[dir][1];

            if (out_range(nx, ny) || arr[nx][ny] == -1) {
                break;
            }

            // check
            if (arr[nx][ny] != 1) {
                int[] first = snake_pos.pollFirst();
                int fx = first[0];
                int fy = first[1];
                arr[fx][fy] = 0;
            }

            arr[nx][ny] = -1;

            // change
            snake_pos.add(new int[] { nx, ny });

            // change direction

            if (!change_dir.isEmpty() && Integer.parseInt(change_dir.peekFirst()[0]) == t) {
                if (change_dir.peekFirst()[1].equals("L")) {
                    dir -= 1;
                    if (dir < 0) {
                        dir = 3;
                    }
                } else {
                    dir += 1;
                    if (dir == 4) {
                        dir = 0;
                    }
                }

                change_dir.pollFirst();
            }

        }

        System.out.println(t);
    }
}
