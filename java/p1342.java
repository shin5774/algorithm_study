import java.io.*;
import java.util.*;

public class p1342 {
    public static int ans = 0;
    public static int size = 0;
    public static Map<String, Integer> alpha = new HashMap<>();

    public static void back_tracking(int level, String before) {
        if (level == size) {
            ans += 1;
            return;
        }

        for (String a : alpha.keySet()) {
            if (alpha.get(a) == 0) {
                continue;
            }

            if (a.equals(before)) {
                continue;
            }

            alpha.put(a, alpha.get(a) - 1);
            back_tracking(level + 1, a);
            alpha.put(a, alpha.get(a) + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        size = input.length();

        for (String a : input.split("")) {
            if (!alpha.containsKey(a)) {
                alpha.put(a, 0);
            }

            alpha.put(a, alpha.get(a) + 1);
        }

        back_tracking(0, "");

        System.out.println(ans);
    }
}
