import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int l = scanner.nextInt();

        if( 380 <= l && l < 425 ){
            System.out.println("Violet");
        }else if(425 <= l && l < 450){
            System.out.println("Indigo");
        }else if(450 <= l && l < 495){
            System.out.println("Blue");
        }else if(495 <= l && l < 570){
            System.out.println("Green");
        }else if(570 <= l && l < 590){
            System.out.println("Yellow");
        }else if(590 <= l && l < 620){
            System.out.println("Orange");
        }else{
            System.out.println("Red");
        }
    }
}