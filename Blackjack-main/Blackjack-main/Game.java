import java.util.Scanner;
public class Game {
	private static Scanner scan = new Scanner(System.in);
	private Deck cards = new Deck();
	private Player player;
	Dealer dealer = new Dealer();
	
	public Game(int difficulty) {
		player = new Player(difficulty);
	}
	
	public int compare(Player player) {
		if (player.getHandValue() > 21) {
			System.out.println("You busted!");
			return -1;
		}
		if (dealer.getHandValue() > 21) {
			return 1;
		}
		if (player.getHandValue() > dealer.getHandValue()) {
			return 1;
		}
		
		if (player.getHandValue() == dealer.getHandValue()) {
			return 0;
		}
		
		return -1;
	}
	
	public void dealerPlay() {
		System.out.println("The dealer's first card is a(n) " + dealer.getCard(0) + ". The dealer's second card was a(n) " + dealer.getCard(1));
		System.out.println("Value of dealer's hand: " + dealer.getHandValue());
		while (dealer.getHandValue() < 17) {
			dealer.hit(cards);
			if (dealer.getHandValue() > 21) {
				dealer.aceReducer();
			}
			System.out.println("The dealer drew a(n) " + dealer.getCard(dealer.handSize()-1));
			System.out.println("Value of dealer's hand: " + dealer.getHandValue());
		}
	}
	
	public void oneHandRound(Player player) {
		while (!player.getStand()) {
			{
				System.out.println("Hit (h) or Stand (s)?");
				String response = scan.next();
				if (response.equals("h")) {
					player.hit(cards);
					if (player.getHandValue() > 21) {
						player.aceReducer();
					}
					System.out.println(player);
					System.out.println("Value of hand: " + player.getHandValue());
					if (player.getHandValue() > 21) {
						player.stand();
					}
				}
				else {
					player.stand();
				}
			}
		}
	}
	
	public void playRound() {
		boolean split = false;
		dealer.hit(cards);
		dealer.hit(cards);
		player.hit(cards);
		player.hit(cards);
		System.out.println(dealer);
		System.out.println(player);
		System.out.println("Value of hand: " + player.getHandValue());
		System.out.println("Dealer: " + dealer.getHand().get(0).getValue());
		System.out.println(player.getBalance() + ". Enter your bet: ");
		int bet = scan.nextInt();
		scan.nextLine();
		if (bet > player.getMoney()) {
			bet = player.getMoney();
		}
		player.bet(bet);
		if (player.split() && bet <= player.getMoney()) {
			System.out.println("You have the option to split your hand into two. (y/n)");
			String response = scan.next();
			split = response.equals("y");
		}
		if (!split) {
			oneHandRound(player);
			dealerPlay();
			player.addMoney(winTally(bet, 2.5, player));
		}
		else {
			player.bet(bet);
			Card one = player.getHand().get(0);
			Card two = player.getHand().get(1);
			
			player.reset();
			player.hit(one);
			player.hit(cards);
			
			Player handTwo = new Player(2);
			handTwo.hit(two);
			handTwo.hit(cards);
			
			System.out.println(player);
			oneHandRound(player);
			System.out.println(handTwo);
			oneHandRound(handTwo);
			dealerPlay();
			int money = winTally(bet, 2, player);
			money += winTally(bet, 2, handTwo);
			player.addMoney(money);
		}
		player.reset();
		dealer.reset();
		System.out.println(player.getBalance());
	}
	
	public int winTally(int bet, double payout, Player player) {
		int win_val = compare(player);
		if (win_val == 1) {
			System.out.println("You won! ");
			return (int)(bet*payout);
		}
		
		if (win_val == 0) {
			System.out.println("You tied! ");
			return bet;
		}
		
		System.out.println("You lost!");
		return 0;
	}
}
