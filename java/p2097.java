import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.math.*;

public class p2097 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Long.parseLong(br.readLine());
        long m = (long) Math.sqrt(n);

        if (n <= 2) {
            System.out.println(4);
            return;
        }

        if (m * m == n) {
            System.out.println((m - 1) * 4);
            return;
        }

        if (n <= m * m + m) {
            System.out.println((m - 1) * 4 + 2);
        } else {
            System.out.println(m * 4);
        }

    }
}
