import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class p2812 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        String input = br.readLine();
        Deque<Integer> deq = new ArrayDeque<>();
        ArrayList<String> ans = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int cur = input.charAt(i) - '0';
            while (!deq.isEmpty() && k > 0 && deq.peekLast() < cur) {
                deq.pollLast();
                k -= 1;
            }
            deq.addLast(cur);
        }

        while (deq.size() > k) {
            int x = deq.pollFirst();
            ans.add(String.valueOf(x));
        }

        System.out.println(String.join("", ans));
    }

}
