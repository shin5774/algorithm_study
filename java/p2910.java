import java.io.*;
import java.util.*;

public class p2910 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long c = Long.parseLong(st.nextToken());
        Map<Long, Integer> d = new LinkedHashMap<>(); // 문제 조건의 동일 빈도수의 경우 먼저 나온것을 해야했기에 LinkedHashMap을 사용
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(st.nextToken());

            if (!d.containsKey(x)) {
                d.put(x, 0);
            }
            d.put(x, d.get(x) + 1);
        }

        // 람다식을 이용한 map의 value기준 내림차순 정렬
        // 오름차순의 경우는 o1.compareTo(o2)의 방식
        List<Long> keySet = new ArrayList<>(d.keySet());
        keySet.sort((o1, o2) -> d.get(o2).compareTo(d.get(o1)));

        for (Long key : keySet) {
            for (int i = 0; i < d.get(key); i++) {
                System.out.print(key + " ");
            }
        }
    }

}
