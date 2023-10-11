import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeMap; //key의 정렬을 위해서

public class p4358 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TreeMap<String, Integer> tree = new TreeMap<>();

        String input = br.readLine();
        int cnt = 0;

        while (input != null) {
            if (!tree.containsKey(input)) {
                tree.put(input, 0);
            }
            tree.put(input, tree.get(input) + 1);
            cnt += 1;

            input = br.readLine();
        }

        for (String x : tree.keySet()) { // 이미 정렬이 되어있음
            // python의 f-string과 동일
            System.out.println(x + " " + String.format("%.4f", tree.get(x) * 100.0 / cnt));
        }
    }
}
