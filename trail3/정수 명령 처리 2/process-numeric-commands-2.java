import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        //큐 정의
        Queue<Integer> q = new LinkedList<>();
        
        // 명령 시작
        for(int i = 1; i<=n; i++){
            String line = sc.nextLine();

            if(line.startsWith("push")){
                String[] tokens = line.split(" ");
                String cmd = tokens[0];
                int value = Integer.parseInt(tokens[1]);
                q.add(value);
            }else if(line.equals("front")){
                System.out.println(q.peek());
            }else if(line.equals("size")){
                System.out.println(q.size());
            }else if(line.equals("empty")){
                System.out.println(q.isEmpty() ? 1: 0);
            }else if (line.equals("pop")){
                System.out.println(q.poll());
            }
        }
    }
}