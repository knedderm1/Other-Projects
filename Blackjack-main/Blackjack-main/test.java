import java.util.Scanner;
public class test {
	public static Scanner scan = new Scanner(System.in);
	public static void main(String args[]) {
		boolean play = true;
		Game game = new Game(2);
		while (play) {
			game.playRound();
			System.out.println("Play again? (y/n)");
			String response = scan.next();
			if (!response.equals("y")) {
				play = false;
			}
		}
	
	}
}
