import java.util.*;
import java.io.*;

public class p3049 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int a = n - 2, sum = 0;
        // a:한 대각선을 만드는 두 점을 제외한 점의 수
        for (int i = 1; i < a; i++) {
            sum += i * (a - i); // 한 점이 만들수 있는 대각선과 해당 대각선의 교차점의 개수
        }

        System.out.println(sum * n / 4); // 한 점이 만들수 있는 모든 교차점* 모든 점(n) /중복(교차점을 만드는 점의 개수(4))
    }
}
