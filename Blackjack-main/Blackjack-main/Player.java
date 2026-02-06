import java.util.ArrayList;

public class Player {
	
	private ArrayList<Card> hand = new ArrayList<Card>();
	private int money = 1000;
	private boolean stand = false;
	
	public Player(int difficulty) {
		money /= difficulty;
	}
	
	public void aceReducer() {
		for (int i = 0; i < getHand().size(); i++) {
			if (getHandValue() > 21 && getHand().get(i).getValue() == 11) {
				remove(i);
				Card ace = new Card("Ace", 1);
				hit(ace);
			}
		}
	}
	
	public void addMoney(int amount) {
		money += amount;
	}
	
	public void removeMoney(int amount) {
		money -= amount;
	}
	
	public int bet(int amount) {
		this.removeMoney(amount);
		return amount;
	}
	
	public String getBalance() {
		return "You have $" + getMoney();
	}
	
	public ArrayList<Card> getHand(){
		return hand;
	}
	
	public int getHandValue() {
		int total = 0;
		for (int i = 0; i < hand.size(); i++) {
			total += hand.get(i).getValue();
		}
		
		return total;
	}
	
	public int getMoney() {
		return money;
	}
	
	public boolean getStand() {
		return stand;
	}
	
	public void hit(Deck cards) {
		hand.add(cards.hit());
	}
	
	public void hit(Card card) {
		hand.add(card);
	}
	
	public void reset() {
		stand = false;
		hand = new ArrayList<Card>();
	}
	
	public void remove(int index) {
		hand.remove(index);
	}
	
	public boolean split() {
		return hand.size() == 2 && hand.get(0).getName().equals(hand.get(1).getName());
	}
	
	public void stand() {
		stand = true;
	}
	
	public String toString() {
		String response = "You have the following cards:";
		for (int i = 0; i < hand.size(); i++) {
			response += hand.get(i).getName() + " ";
		}
		return response;
	}
}
