import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i=1; i<=n; i++){
            q.add(i);
        }
        
        int count = 0;
        while (q.size() != 0){
            int person = q.poll(); // 맨 앞 사람 꺼내기
            count++;
            if (count == k){
                System.out.print(person+" ");
                count = 0;
            } else {
                q.add(person);
            }
        }

    }
}