import java.util.*;
import java.io.*;

public class p20291 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> ans = new HashMap<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), ".");
            st.nextToken();
            String ex = st.nextToken();
            if (!ans.containsKey(ex)) {
                ans.put(ex, 0);
            }

            ans.put(ex, ans.get(ex) + 1);
        }

        List<String> keys = new ArrayList<>(ans.keySet());

        Collections.sort(keys);

        for (String key : keys) {
            System.out.println(key + " " + ans.get(key));
        }
    }
}
