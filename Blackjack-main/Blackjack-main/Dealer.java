public class Dealer extends Player{
	public Dealer() {
		super(1);
	}
	
	public String toString() {
		return "The dealer has a(n) " + getHand().get(0).getName();
	}
	
	public String getCard(int index) {
		return getHand().get(index).getName();
	}
	
	public int handSize() {
		return getHand().size();
	}
}
