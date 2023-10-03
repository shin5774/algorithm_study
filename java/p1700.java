import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1700 {
    public static ArrayList<Integer> arr = new ArrayList<>();
    public static Set<Integer> multiTap = new HashSet<>();
    public static Map<Integer, Integer> cnt = new HashMap<>();

    public static void find(int idx) {
        for (int x : multiTap) {
            if (cnt.get(x) == 0) {
                multiTap.remove(x);
                return;
            }
        }
        int finder = Collections.max(multiTap,
                Comparator.comparingInt(x -> arr.subList(idx + 1, arr.size()).indexOf(x)));
        multiTap.remove(finder);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int ans = 0;
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < k; i++) {
            arr.add(Integer.parseInt(st.nextToken()));

            if (!cnt.containsKey(arr.get(i))) {
                cnt.put(arr.get(i), 0);
            }
            cnt.put(arr.get(i), cnt.get(arr.get(i)) + 1);
        }

        for (int i = 0; i < k; i++) {
            int cur = arr.get(i);

            if (!multiTap.contains(cur)) {
                if (multiTap.size() == n) {
                    find(i);
                    ans += 1;
                }
                multiTap.add(cur);
            }

            cnt.put(cur, cnt.get(cur) - 1);
        }

        System.out.println(ans);

    }
}
