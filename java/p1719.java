import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1719 {
    public static int n;
    public static ArrayList<ArrayList<Node>> graph;
    public static int INF = Integer.MAX_VALUE;

    public static class Node {
        int next, cost;

        Node(int next, int cost) {
            this.next = next;
            this.cost = cost;
        }
    }

    public static class dNode {
        int cur, cost, prev;

        dNode(int cur, int cost, int prev) {
            this.cur = cur;
            this.cost = cost;
            this.prev = prev;
        }
    }

    public static int[] dijkstra(int x) {
        int[] cost = new int[n + 1];
        int[] didx = new int[n];
        Arrays.fill(cost, INF);
        ArrayList<ArrayList<Integer>> root = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= n; i++) {
            root.add(new ArrayList<Integer>());
        }

        PriorityQueue<dNode> q = new PriorityQueue<dNode>((o1, o2) -> Integer.compare(o1.cost, o2.cost));

        q.add(new dNode(x, 0, 0));

        while (!q.isEmpty()) {
            dNode cur = q.poll();

            if (cost[cur.cur] != INF) {
                continue;
            }
            cost[cur.cur] = cur.cost;
            root.get(cur.cur).clear();

            for (int nidx : root.get(cur.prev)) {
                root.get(cur.cur).add(nidx);
            }

            root.get(cur.cur).add(cur.cur);

            for (Node next : graph.get(cur.cur)) {
                if (cost[next.next] > cur.cost + next.cost) {
                    q.add(new dNode(next.next, cur.cost + next.cost, cur.cur));
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            if (i == x) {
                didx[i - 1] = 0;
            } else {
                didx[i - 1] = root.get(i).get(1);
            }
        }

        return didx;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new ArrayList<ArrayList<Node>>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }

        for (int i = 1; i <= n; i++) {
            int[] ans = dijkstra(i);

            for (int j = 0; j < n; j++) {
                if (i - 1 == j) {
                    System.out.print("- ");
                } else {
                    System.out.print(ans[j] + " ");
                }
            }
            System.out.println();
        }

    }
}
