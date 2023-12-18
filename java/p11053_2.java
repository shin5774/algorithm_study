import java.io.*;
import java.util.*;

public class p11053_2 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            int find = 0;

            for (int j = 0; j < i; j++) {
                if (arr[j] < x) {
                    find = Math.max(find, dp[j]);
                }
            }
            arr[i] = x;
            dp[i] = find + 1;
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
