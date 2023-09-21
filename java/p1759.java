import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p1759 {
    public static int l, c;
    public static ArrayList<String> arr;
    public static ArrayList<String> cur = new ArrayList<>();
    public static Set<String> vowel_set = new HashSet<>(Arrays.asList("a", "e", "i", "o", "u"));
    public static int const_n = 0, vow_n = 0;

    public static void next_add_find(int idx) {
        cur.add(arr.get(idx));
        find(idx + 1);
        cur.remove(cur.size() - 1);
    }

    public static void find(int idx) {
        if (cur.size() == l) {
            if (const_n >= 2 && vow_n >= 1) {
                System.out.println(String.join("", cur));
            }
            return;
        }

        if (idx == c) {
            return;
        }

        if (vowel_set.contains(arr.get(idx))) {
            vow_n += 1;
            next_add_find(idx);
            vow_n -= 1;
        } else {
            const_n += 1;
            next_add_find(idx);
            const_n -= 1;
        }

        find(idx + 1);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        arr = new ArrayList<String>();

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < c; i++) {
            arr.add(st.nextToken());
        }

        Collections.sort(arr);

        find(0);
    }
}
