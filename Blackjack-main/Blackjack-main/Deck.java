import java.util.ArrayList;
import java.security.SecureRandom;
public class Deck {
	
	private ArrayList<Card> cards = new ArrayList<Card>();
	public Deck() {
		newDeck();
	}
	
	public Card hit() {
		if (cards.size() == 0) {
			newDeck();
		}
		SecureRandom rand = new SecureRandom();
		int random = rand.nextInt(cards.size());
		int cardIndex = random;
		Card card = cards.get(cardIndex);
		cards.remove(cardIndex);
		
		return card;
	}
	
	public void newDeck() {
		for (int i = 0; i < 5; i++) {
			cards.add(new Card("Ace", 11));
			for (int j = 2; j <= 10; j++) {
				cards.add(new Card("" + j, j));
			}
			cards.add(new Card("Jack", 10));
			cards.add(new Card("Queen", 10));
			cards.add(new Card("King", 10));
		}
	}
}
