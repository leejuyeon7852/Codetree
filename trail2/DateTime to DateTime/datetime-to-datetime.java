import java.util.Scanner;
public class Main {
    public static int elapsedMinutes(int d, int h, int m){
        if(d < 11){
            return -1;
        }else if(d == 11){
            if (h < 11){
                return -1;
            }else if (h == 11 && m < 11){
                return -1;
            }
        }

        int minutes = ((d-11)*24*60)+((h-11)*60)+(m-11);
        return minutes;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(elapsedMinutes(A, B, C));
    }
}