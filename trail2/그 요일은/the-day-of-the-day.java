import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        String A = sc.next();

        String[] weekDays = new String[]{"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

        int diff = numOfDays(m2, d2)-numOfDays(m1, d1);

        int targetIndex = 0;
        for (int i = 0; i < 7; i++) {
            if (weekDays[i].equals(A)) {
                targetIndex = i;
                break;
            }
        }

        int count = diff / 7; 
        int remainder = diff % 7;
        if (remainder >= targetIndex) {
            count++;
        }

        System.out.println(count);
    }

    public static int numOfDays(int m, int d){
        int[] num_of_days = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        int totalDays = 0;
        for(int i=1; i < m; i++){
            totalDays += num_of_days[i];
        }
        totalDays += d;

        return totalDays;
    }
}