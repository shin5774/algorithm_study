import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p2468 {
    public static int n;
    public static int[][] arr;
    public static boolean[][] visited;
    public static int[] dx = { 1, -1, 0, 0 };
    public static int[] dy = { 0, 0, 1, -1 };

    public static int find(int h) {
        visited = new boolean[n][n];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] > h && !visited[i][j]) {
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[] { i, j });
                    visited[i][j] = true;

                    while (!q.isEmpty()) {
                        int[] cur = q.poll();

                        for (int d = 0; d < 4; d++) {
                            int nx = cur[0] + dx[d];
                            int ny = cur[1] + dy[d];

                            if (nx < 0 || ny < 0 || nx == n || ny == n || arr[nx][ny] <= h || visited[nx][ny]) {
                                continue;
                            }

                            q.add(new int[] { nx, ny });
                            visited[nx][ny] = true;
                        }

                    }

                    cnt += 1;
                }
            }
        }

        return cnt;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        int min = 101;
        int max = 0;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());

                if (min > arr[i][j]) {
                    min = arr[i][j];
                }

                if (max < arr[i][j]) {
                    max = arr[i][j];
                }
            }
        }

        for (int i = min - 1; i < max; i++) {
            int cur = find(i);
            if (ans < cur) {
                ans = cur;
            }
        }

        System.out.println(ans);
    }
}
