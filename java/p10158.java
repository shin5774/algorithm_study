import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class p10158 {
    public static int t;

    public static int find(int l, int x) {
        int cur = (x + t) % (2 * l);

        if (cur > l) {
            return 2 * l - cur;
        } else {
            return cur;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        t = Integer.parseInt(br.readLine());

        System.out.println(find(w, x) + " " + find(h, y));
    }
}
