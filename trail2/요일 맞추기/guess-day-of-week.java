import java.util.Scanner;
public class Main {
    
    static final int WEEK = 7;

    public static int totalDays(int m, int d){
        int total = 0;
        int []days =  new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        for(int i = 1; i < m; i++){
            total += days[i];
        }
        total += d;

        return total;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();

        String []weekDays = new String[]{"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

        int diff = totalDays(m2, d2) - totalDays(m1, d1);

        while(diff < 0){
            diff += WEEK;
        }

        System.out.print(weekDays[diff%WEEK]);

    }
}