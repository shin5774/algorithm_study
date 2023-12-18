import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p10972 {
    public static int n;
    public static int[] arr;

    public static int find(int idx) {
        int find = n;

        for (int i = idx; i < n; i++) {
            if (arr[i] > arr[idx - 1] && arr[i] < arr[find]) {
                find = i;
            }
        }

        return find;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        arr[n] = n + 1;

        int idx;

        for (idx = n - 1; idx > 0; idx--) {
            if (arr[idx] > arr[idx - 1]) {
                break;
            }
        }

        if (idx == 0) {
            System.out.println(-1);
            return;
        }

        int find = find(idx);

        // 값 스위치
        int tmp = arr[idx - 1];
        arr[idx - 1] = arr[find];
        arr[find] = tmp;

        Arrays.sort(arr, idx, n);

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
