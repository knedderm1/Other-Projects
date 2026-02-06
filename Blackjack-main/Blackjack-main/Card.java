
public class Card {
	private int value;
	private String name;
	
	/*
	 * @param face_value
	 * how much the card is worth (1-10)
	 * @param card_num
	 * same as face_value for 2-10, but for face cards 
	 * is necessary to differentiate queens from kings
	 */
	public Card (String card_num, int face_value) {
		name = card_num;
		value = face_value;
	}
	
	public String getName() {
		return name;
	}
	
	public int getValue() {
		return value;
	}

}
