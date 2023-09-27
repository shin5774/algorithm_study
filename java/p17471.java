import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p17471 {
    public static int n, ans = 10000;
    public static ArrayList<Set<Integer>> graph = new ArrayList<>();
    public static int[] arr;
    public static Set<Integer> x_node = new HashSet<>();
    public static boolean[] visited;

    public static void combination(int start, int r, int x) {
        if (r == 0) {
            Set<Integer> y_node = new HashSet<>();
            int y = -1;

            // 다른 지역구 세팅
            for (int i = 1; i <= n; i++) {
                if (!x_node.contains(i)) {
                    y_node.add(i);
                    y = i;
                }
            }

            // 두 연결이 서로 잘 되어있는경우 최솟값 확인
            if (connected(x_node, x) && connected(y_node, y)) {
                int cur = Math.abs(total(x_node) - total(y_node));

                if (cur < ans) {
                    ans = cur;
                }

            }
            return;
        }

        for (int i = start; i <= n; i++) {
            x_node.add(i);
            combination(i + 1, r - 1, i);
            x_node.remove(i);
        }

    }

    public static boolean connected(Set<Integer> s, int x) {
        if (s.size() == 1) {
            return true;
        }

        visited = new boolean[n + 1];
        Deque<Integer> q = new ArrayDeque<>();
        q.add(x);

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (visited[cur]) {
                continue;
            }

            visited[cur] = true;

            for (int next : graph.get(cur)) {
                if (!visited[next] && s.contains(next)) {
                    q.add(next);
                }
            }
        }

        for (int el : s) {
            if (!visited[el]) {
                return false;
            }
        }

        return true;
    }

    public static int total(Set<Integer> s) {
        int sum = 0;

        for (int x : s) {
            sum += arr[x];
        }

        return sum;
    }

    public static void main(String[] args) throws IOException {
        // 입력 설정 및 n 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        // n의 따른 각 배열 동적 할당
        arr = new int[n + 1];
        int[] numbers = new int[n];

        for (int i = 0; i <= n; i++) {
            graph.add(new HashSet<Integer>());
        }

        // 각 도시의 인구수 받기
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            numbers[i - 1] = i;
        }

        // 각 도시의 인접도시 입력
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int sz = Integer.parseInt(st.nextToken());

            for (int j = 0; j < sz; j++) {
                graph.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        // 조합 찾기
        for (int i = 1; i < n / 2 + 1; i++) { // n개중 i개의 도시
            combination(1, i, 0);
        }

        // 값변경 유무에따른 출력 값 변화
        if (ans == 10000) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }

    }
}
