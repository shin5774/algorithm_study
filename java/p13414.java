import java.io.*;
import java.util.*;

public class p13414 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        Map<String, Integer> waiting = new HashMap<>();

        for (int i = 0; i < l; i++) {
            String user = br.readLine();
            waiting.put(user, i);
        }

        List<String> ans = new ArrayList<>(waiting.keySet());
        Collections.sort(ans, (v1, v2) -> (waiting.get(v1).compareTo(waiting.get(v2))));

        for (int i = 0; i < Math.min(k, ans.size()); i++) {
            System.out.println(ans.get(i));
        }
    }
}
