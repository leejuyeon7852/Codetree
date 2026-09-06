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

        String answer = "";
        
        int []days =  new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String []weekDays = new String[]{"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

        int diff_month = m1-m2;
        int diff_days = d1-d2;
        int index = 0; // 월요일

        // 월이 같다면
        if(diff_month == 0){
            if (diff_days == 0) answer = weekDays[index];
            // d1이 클 때 - diff_days 양수
            else if(diff_days > 0) { 
                answer = weekDays[(((index-diff_days) % WEEK)+WEEK)%WEEK];
            }
            // d1 작을 때 - diff_days가 음수 
            else{
                answer = weekDays[(index-diff_days)%WEEK];
            }
        }
        // m1이 m2보다 작다면 (diff_month가 음수)
        else if(diff_month < 0){
            int diff = totalDays(m1, d1) - totalDays(m2, d2);
            answer = weekDays[(index-diff)%WEEK];
        }
        // m1이 m2보다 크다면 (diff_month가 양수)
        else{
            int diff = totalDays(m1, d1) - totalDays(m2, d2);
            answer = weekDays[(((index-diff) % WEEK)+WEEK)%WEEK];
        }

        System.out.println(answer);

    }
}