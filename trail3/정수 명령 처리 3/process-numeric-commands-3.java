import java.util.Scanner;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // Deque 선언
        Deque<Integer> dq = new ArrayDeque<>();

        for(int i = 0; i < n; i++){
            String cmd = sc.next();
            
            if(cmd.equals("push_back")){
                int value = sc.nextInt();
                dq.addLast(value);
            }
            else if(cmd.equals("push_front")){
                int value = sc.nextInt();
                dq.addFirst(value);
            }
            else if(cmd.equals("pop_front")){
                System.out.println(dq.pollFirst());
            }
            else if(cmd.equals("pop_back")){
                System.out.println(dq.pollLast());
            }
            else if(cmd.equals("size")){
                System.out.println(dq.size());
            }
            else if(cmd.equals("front")){
                System.out.println(dq.peekFirst());
            }
            else if(cmd.equals("back")){
                System.out.println(dq.peekLast());
            }
            else if(cmd.equals("empty")){
                System.out.println(dq.isEmpty() ? 1 : 0);
            }
        }
    }
}
