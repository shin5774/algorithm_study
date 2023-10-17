import java.util.*;
import java.io.*;

public class p15683 {
    public static int[][] arr, checker;
    public static int n, m, ans;
    public static ArrayList<ArrayList<Integer>> cctv = new ArrayList<>();
    public static ArrayList<int[]> dir = new ArrayList<>();
    public static int[][] mv = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    public static int[][][] cctvDir = {
            { { 0 }, { 1 }, { 2 }, { 3 } },
            { { 2, 3 }, { 0, 1 } },
            { { 1, 2 }, { 0, 2 }, { 0, 3 }, { 1, 3 } },
            { { 1, 2, 3 }, { 0, 1, 2 }, { 0, 2, 3 }, { 0, 1, 3 } },
            { { 0, 1, 2, 3 } }
    };// mv에 따른 각 타입별 기체방향에 따른 cctv 감시 가능 방향

    public static boolean outRange(int x, int y) {
        if (x < 0 || y < 0 || x == n || y == m) {
            return true;
        }
        return false;
    }

    public static void draw(int x, int y, int d) {
        while (true) {
            int nx = x + mv[d][0], ny = y + mv[d][1];

            if (outRange(nx, ny) || checker[nx][ny] == 6) {
                return;
            }

            if (checker[nx][ny] == 0) {
                checker[nx][ny] = -1;
            }

            x = nx;
            y = ny;
        }
    }

    // 설정한 방향에 따라 표시
    public static void simulation() {
        checker = new int[n][m];

        // 배열 깊은 복사
        for (int i = 0; i < n; i++) {
            System.arraycopy(arr[i], 0, checker[i], 0, m);
        }

        for (int i = 0; i < dir.size(); i++) {
            for (int d : dir.get(i)) {
                draw(cctv.get(i).get(0), cctv.get(i).get(1), d);
            }
        }

        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (checker[i][j] == 0) {
                    cnt += 1;
                }
            }
        }

        ans = Math.min(ans, cnt);
    }

    // 각 타입별 경우의수 브루트포스
    public static void back_tracking(int idx) {
        if (idx == cctv.size()) {
            simulation();
            return;
        }

        for (int i = 0; i < cctvDir[cctv.get(idx).get(2) - 1].length; i++) {
            dir.add(cctvDir[cctv.get(idx).get(2) - 1][i]);
            back_tracking(idx + 1);
            dir.remove(dir.size() - 1);
        }

    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        ans = n * m;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int x = Integer.parseInt(st.nextToken());

                // cctv좌표와 타입 저장
                if (x > 0 && x < 6) {
                    cctv.add(new ArrayList<>(Arrays.asList(i, j, x)));
                }

                arr[i][j] = x;
            }
        }

        back_tracking(0);
        System.out.println(ans);
    }
}
