
public class test {
	public static void main(String args[]) {
		int[][] board = {{0, 1, 2, 0, 4, 6, 3, 8, 9}, 
						 {3, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 8, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 0, 0, 0},
						 {0, 0, 0, 0, 0, 0, 2, 0, 0},};
		Solver x = new Solver(board);
		x.sudokuSolver();
		System.out.println(x);
	}
}
