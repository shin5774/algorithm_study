import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p6603 {
    public static int[] arr;
    public static int n;
    public static Stack<Integer> cur = new Stack<>();

    public static void back_tracking(int idx) {

        if (cur.size() == 6) {
            Iterator iter = cur.iterator();
            while (iter.hasNext()) {
                System.out.print(iter.next() + " ");
            }
            System.out.println();

            return;
        }

        if (idx == n) {
            return;
        }

        cur.push(arr[idx]);
        back_tracking(idx + 1);
        cur.pop();
        back_tracking(idx + 1);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            arr = new int[n];

            if (n == 0) {
                break;
            }

            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            back_tracking(0);
            System.out.println();
        }
    }
}
