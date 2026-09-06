import java.util.Scanner;
public class Main {
    public static int numOfDays(int m, int d){
        // 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        int []days =  new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int totalDays = 0;

        for(int i = 1; i < m; i++){
            totalDays += days[i];
        }
        totalDays += d;

        return totalDays;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        
        System.out.println(numOfDays(m2, d2)-numOfDays(m1, d1) + 1);
    }
}