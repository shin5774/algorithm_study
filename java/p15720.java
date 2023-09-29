import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p15720 {
    public static Integer[][] arr = new Integer[3][];
    public static int[] nums = new int[3];

    public static int sum(double mul, int cnt) {
        int s = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < cnt; j++) {
                s += arr[i][j] * mul;
            }

            for (int j = cnt; j < nums[i]; j++) {
                s += arr[i][j];
            }
        }

        return s;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 3; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            arr[i] = new Integer[nums[i]];
        }

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < nums[i]; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr[i], Collections.reverseOrder());
        }

        int sets = Arrays.stream(nums).min().getAsInt();

        System.out.println(sum(1, 0));
        System.out.println(sum(0.9, sets));

    }
}
