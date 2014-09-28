package com.moni.hackbg.firsttask;

public class XOCounter {

	public boolean ExOh(String input){
		int counter = 0;
		for (int i = 0; i <= input.length() -1; i++) {
			if (input.charAt(i)=='x') {
				counter++;
			} else if (input.charAt(i)=='o') {
				counter--;
			} else {
				System.out.println("Only 'x' and 'o' supported !");
			}
		}

		return (counter == 0);
	}

	public static void main(String[] args) {
		XOCounter newXOCounter = new XOCounter();
        System.out.println(newXOCounter.ExOh("xoxoox"));
        System.out.println(newXOCounter.ExOh("oooxoo"));
	}
}
