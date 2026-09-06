import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        
        // 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        int []num_of_days =  new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int total_days = 0;
        for(int i=1; i<m2; i++){
            total_days += num_of_days[i];
            //System.out.println(i+":"+total_days);
        }
        total_days += d2;
        //System.out.println(total_days);

        int sum_days = 0;
        for(int i=1; i<m1; i++){
            sum_days += num_of_days[i];
            //System.out.println(i+":"+sum_days);
        }
        sum_days += d1;
        //System.out.println(sum_days);

        System.out.println(total_days-sum_days+1);
    }
}