import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p12015 {
    public static int n;
    public static int[] arr;
    public static int[] ans;
    public static int len;

    public static int lower_bound(int x) {
        int low = -1;
        int high = len;

        while (low + 1 < high) {
            int mid = (low + high) / 2;

            if (ans[mid] >= x) {
                high = mid;
            } else {
                low = mid;
            }
        }

        return high;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        arr = new int[n];
        ans = new int[n];
        len = 1;

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        ans[0] = arr[0];

        for (int i = 1; i < n; i++) {
            if (ans[len - 1] < arr[i]) {
                ans[len] = arr[i];
                len += 1;
            } else {
                int idx = lower_bound(arr[i]);
                ans[idx] = arr[i];
            }
        }

        System.out.println(len);
    }
}
