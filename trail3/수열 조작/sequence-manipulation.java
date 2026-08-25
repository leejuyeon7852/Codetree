import java.util.Scanner;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        Deque<Integer> dq = new ArrayDeque<>();

        for(int i = 1; i <= n;  i++){
            dq.addLast(i);
        }

        while(dq.size() != 1){
            // 맨 앞 정수 제거
            dq.pollFirst();

            // 제거 후 남은 수열 뒤로 이동
            dq.addLast(dq.pollFirst());
        }

        // 남은 수열 출력 
        System.out.println(dq.peekFirst()); 
    }
}