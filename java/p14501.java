import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class p14501 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] arr = new int[n][2];
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 0);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + arr[i][0]; j <= n; j++) {
                if (dp[j] < dp[i] + arr[i][1]) {
                    dp[j] = dp[i] + arr[i][1];
                }
            }
        }

        System.out.println(dp[n]);
    }
}
