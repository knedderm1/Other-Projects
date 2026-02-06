
public class Board {
	String[][] board = new String[6][7];
	public Board() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				board[i][j] = "+";
			}
		}
	}
	
	public boolean select(int col, String player) {
		for (int i = board.length - 1; i >= 0; i--) {
			if (board[i][col].equals("+")) {
				board[i][col] = player;
				return true;
			}
		}
		return false;
	}
	
	public boolean isWin(String player) {
		for (int i = 0; i < board.length; i++) {
			int count = 0;
			for (int j = 0; j < board[i].length; j++) {
				if (board[i][j].equals(player)) {
					count++;
				}
				else {
					count = 0;
				}
				if (count == 4) {
					return true;
				}
			}
		}
		
		for (int i = 0; i < board[0].length; i++) {
			int count = 0;
			for (int j = 0; j < board.length; j++) {
				if (board[j][i].equals(player)) {
					count++;
				}
				else {
					count = 0;
				}
				if (count == 4) {
					return true;
				}
			}
		}
		
		for (int i = 0; i < 4; i++) {
			int count = 0;
			for (int j = 0; j < board.length-i+1; j++) {
				if (!(i == 0 && j == 6)) {
					if (board[j][j+i].equals(player)) {
						count++;
					}
					else {
						count = 0;
					}
					if (count == 4) {
						return true;
					}
				}
			}
		}
		
		for (int i = 0; i < 2; i++) {
			int count = 0;
			for (int j = 0; j < board.length-i; j++) {
				if (!(i == 0 && j == 5)) {
					if (board[j+1][j].equals(player)) {
						count++;
					}
					else {
						count = 0;
					}
					if (count == 4) {
						return true;
					}
				}
			}
		}
		
		for (int i = 0; i < 4; i++) {
			int count = 0;
			for (int j = 0; j < board.length-i+1; j++) {
				if (!(i == 0 && j==6)) {
					if (board[board.length-1-j][j+i].equals(player)) {
						count++;
					}
					else {
						count = 0;
					}
					if (count == 4) {
						return true;
					}
				}
			}
		} 
		
		for (int i = 0; i < 3; i++) {
			int count = 0;
			for (int j = 0; j < board.length-i; j++) {
				if (board[board.length-1-j-i][j].equals(player)) {
					count++;
				}
				else {
					count = 0;
				}
				if (count == 4) {
					return true;
				}
			}
		}
		
		return false;
	}
	
	public String toString() {
		String phrase = "";
		for (int i = 0; i < board.length+1; i++) {
			for (int j = 0; j < board[0].length; j++) {
				if (i == board.length) {
					phrase += "  " + j;
				}
				else {
					phrase += "  " + board[i][j];
				}
			}
			phrase += "\n";
		}
		return phrase;
	}
}
