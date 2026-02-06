
public class Solver {
	public int[][] board;
	
	public Solver(int[][] board) {
		this.board = board;
	}
	
	public int[] getEmpty() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				if (board[i][j] == 0) {
					int[] coords = {i, j};
					return coords;
				}
			}
		}
		int[] coords = {-1, -1};
		return coords;
	}
	
	public boolean validator(int[] coords, int value) {
		int y = coords[0];
		int x = coords[1];
		int boxSize = (board.length + 2)/3;
		for (int i = 0; i < board.length; i++) {
			if (board[i][x] == value || board[y][i] == value) {
				return false;
			}
		}
		
		for (int j = 0; j < boxSize; j++) {
			for (int k = 0; k < boxSize; k++) {
				if (board[boxSize * (y / boxSize) + (j+y)%boxSize][boxSize * (x / boxSize) + (k+x)%boxSize] == value) {
					return false;
				}
			}
		}
		
		return true;
	}
	
	public boolean sudokuSolver() {
		if (getEmpty()[0] != -1) {
			int[] coords = getEmpty();
			for (int i = 1; i < board.length + 1; i++) {
				if (validator(coords, i)) {
					setBoard(coords, i);
					if (!sudokuSolver()) {
						setBoard(coords, 0);
					}
				}
			}
			return board[coords[0]][coords[1]] != 0;
		}
		return true;
	}
	
	public void setBoard(int[] coords, int value) {
		board[coords[0]][coords[1]] = value;
	}
	
	public String toString() {
		String print = "";
		int boxSize = (board.length + 2) / 3;
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				print += " " + board[i][j];
				if (boxSize - (j%boxSize) == 1){
					print += " | ";
				}
			}
			print += "\n";
			if (boxSize - (i%boxSize) == 1) {
				for (int k = 0; k < board.length + boxSize; k++) {
					print += "- ";
				}
				print += "\n";
			}
		}
		return print;
	}
}
