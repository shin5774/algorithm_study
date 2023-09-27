import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p10973 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int idx = -1;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                idx = i;
            }
        }

        if (idx == -1) {
            System.out.println(-1);
        } else {
            int cur = 0, max_idx = -1;

            for (int i = idx; i < n; i++) {
                if (arr[i] < arr[idx] && cur < arr[i]) {
                    max_idx = i;
                    cur = arr[i];
                }
            }

            arr[max_idx] = arr[idx];
            arr[idx] = cur;

            int[] s_arr = Arrays.copyOfRange(arr, idx + 1, n);
            Arrays.sort(s_arr);

            for (int i = idx + 1; i < n; i++) {
                arr[i] = s_arr[n - (i + 1)];
            }

            for (int x : arr) {
                System.out.print(x + " ");
            }
        }

    }
}
