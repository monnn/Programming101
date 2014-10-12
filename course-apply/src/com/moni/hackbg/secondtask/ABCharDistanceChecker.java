package com.moni.hackbg.secondtask;

public class ABCharDistanceChecker {

    private static final int DISTANCE_THRESHOLD = 3;

	public boolean ABCheck(String str) {
		boolean check = false;
	    for (int i = 0; i <= str.length() - 5; i++) {
            char firstChar = str.charAt(i);
            char secondChar = str.charAt(i + DISTANCE_THRESHOLD + 1);
            if (firstChar == 'a' && secondChar =='b') {
				check = true;
			}
	    }

	    return check;
    }

	public static void main(String[] args) {
		ABCharDistanceChecker checker = new ABCharDistanceChecker();
        System.out.println(checker.ABCheck("Laura sobs"));
        System.out.println(checker.ABCheck("after badly"));
	}
}
