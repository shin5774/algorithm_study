import java.io.*;
import java.util.*;

public class p2636 {
    public static int row, col;
    public static int[][] arr;
    public static Set<int[]> cheeze = new HashSet<>();
    public static ArrayList<Integer> turn = new ArrayList<>();
    public static int[][] mv = new int[][] { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

    public static boolean is_air(int x, int y) {
        return x == 0 || x == row - 1 || y == 0 || y == col - 1;
    }

    public static boolean is_remove(int x, int y, boolean[][] visited) {
        visited[x][y] = true;

        for (int[] m : mv) {
            int nx = x + m[0];
            int ny = y + m[1];

            if (visited[nx][ny] || arr[nx][ny] == 1) {
                continue;
            }

            if (is_air(nx, ny)) {
                return true;
            }

            if (is_remove(nx, ny, visited)) {
                return true;
            }
        }

        return false;
    }

    public static void play() {
        ArrayList<int[]> remove = new ArrayList<>();

        for (int[] ch : cheeze) {
            if (is_remove(ch[0], ch[1], new boolean[row][col])) {
                remove.add(ch);
            }
        }

        turn.add(turn.get(turn.size() - 1) - remove.size());

        for (int[] r : remove) {
            arr[r[0]][r[1]] = 0;
            cheeze.remove(r);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());
        arr = new int[row][col];

        for (int i = 0; i < row; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < col; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 1) {
                    cheeze.add(new int[] { i, j });
                }
            }
        }

        turn.add(cheeze.size());

        while (turn.get(turn.size() - 1) != 0) {
            play();
        }

        System.out.println(turn.size() - 1);
        System.out.println(turn.get(turn.size() - 2));

    }

}
