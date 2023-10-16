import java.io.*;
import java.util.*;

public class p14891 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        ArrayList<ArrayList<Integer>> gears = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            ArrayList<Integer> gear = new ArrayList<>();
            String input = br.readLine();
            for (int j = 0; j < 8; j++) {
                gear.add(input.charAt(j) - '0');
            }
            gears.add(gear);
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int target = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());

            ArrayList<Integer> left = new ArrayList<>();

            for (int j = target - 1; j >= 0; j--) {
                if (gears.get(j).get(2) + gears.get(j + 1).get(6) == 1) {
                    left.add(j);
                } else {
                    break;
                }
            }

            for (int idx : left) {
                if (Math.abs(target - idx) % 2 == 0) {
                    Collections.rotate(gears.get(idx), dir);
                } else {
                    Collections.rotate(gears.get(idx), -dir);
                }
            }

            ArrayList<Integer> right = new ArrayList<>();

            for (int j = target + 1; j < 4; j++) {
                if (gears.get(j).get(6) + gears.get(j - 1).get(2) == 1) {
                    right.add(j);
                } else {
                    break;
                }
            }

            for (int idx : right) {
                if (Math.abs(target - idx) % 2 == 0) {
                    Collections.rotate(gears.get(idx), dir);
                } else {
                    Collections.rotate(gears.get(idx), -dir);
                }
            }

            Collections.rotate(gears.get(target), dir);
        }
        int ans = 0;
        int add = 1;
        for (ArrayList<Integer> gear : gears) {
            if (gear.get(0) == 1) {
                ans += add;
            }

            add *= 2;
        }

        System.out.println(ans);
    }
}
