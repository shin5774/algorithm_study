import java.util.*;
import java.io.*;

public class p1822 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Set<Integer> a = new HashSet<>();
        int na = Integer.parseInt(st.nextToken());
        int nb = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < na; i++) {
            a.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nb; i++) {
            int x = Integer.parseInt(st.nextToken());

            if (a.contains(x)) {
                a.remove(x);
            }
        }

        List<Integer> ans = new ArrayList<>(a);
        Collections.sort(ans);

        System.out.println(ans.size());

        for (int x : ans) {
            System.out.print(x + " ");
        }

    }
}
