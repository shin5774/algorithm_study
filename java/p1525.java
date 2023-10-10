import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class p1525 {
    public static Map<String, Integer> m = new HashMap<>();

    public static int find(String input) {
        Deque<String> q = new ArrayDeque<>();
        int[][] mv = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        m.put(input, 0);
        q.add(input);

        while (!q.isEmpty()) {
            String cur = q.poll();

            if (cur.equals("123456780")) {
                return m.get(cur);
            }

            int pos = cur.indexOf("0");
            int x = pos / 3, y = pos % 3;

            for (int i = 0; i < 4; i++) {
                int nx = x + mv[i][0], ny = y + mv[i][1];

                if (nx < 0 || ny < 0 || nx == 3 || ny == 3) {
                    continue;
                }

                int npos = nx * 3 + ny;

                char[] next = cur.toCharArray();
                char tmp = next[pos];
                next[pos] = next[npos];
                next[npos] = tmp;

                String ns = new String(next);

                if (!m.containsKey(ns)) {
                    m.put(ns, m.get(cur) + 1);
                    q.add(ns);
                }

            }
        }

        return -1;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String input = "";
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                input += st.nextToken();
            }
        }

        System.out.println(find(input));
    }
}
