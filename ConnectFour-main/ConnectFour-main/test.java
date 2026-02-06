import java.util.Scanner;
public class test {
	public static void main(String args[]) {
		Board game = new Board();
		boolean ingame = true;
		Scanner scan = new Scanner(System.in);
		while (ingame) {
			System.out.println(game);
			System.out.println("Red, select a column: ");
			boolean valid = false;
			while(!valid) {
				int col = scan.nextInt();
				if (game.select(col, "R")) {
					valid = true;
				}
				else {
					System.out.println("Invalid choice! Try another!");
					System.out.println(game);
				}
			}
			if (game.isWin("R")) {
				ingame = false;
				System.out.println(game);
				System.out.println("Red has won!");
			}
			
			if(ingame) {
				System.out.println(game);
				System.out.println("Blue, select a column: ");
				valid = false;
				while(!valid) {
					int col = scan.nextInt();
					if (game.select(col, "B")) {
						valid = true;
					}
					else {
						System.out.println("Invalid choice! Try another!");
						System.out.println(game);
					}
				}
				if (game.isWin("B")) {
					ingame = false;
					System.out.println(game);
					System.out.println("Blue has won!");
				}
			}
		}
		scan.close();
		
	}
}
