import java.util.*;
import java.io.*;

public class p2002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> input = new HashMap<>();
        List<Integer> stack = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        for (int i = 0; i < n; i++) {
            input.put(br.readLine(), i);
        }

        for (int i = 0; i < n; i++) {
            int outputNum = input.get(br.readLine());
            while (!stack.isEmpty() && stack.get(stack.size() - 1) > outputNum) {
                ans += 1;
                stack.remove(stack.get(stack.size() - 1)); // 스택 pop
            }

            stack.add(outputNum);
        }

        System.out.println(ans);
    }
}
