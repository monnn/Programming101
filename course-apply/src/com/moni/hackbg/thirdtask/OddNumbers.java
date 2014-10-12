package com.moni.hackbg.thirdtask;

public class OddNumbers {

	public String dashInsert(int num) {
		String input = Integer.toString(num);
        StringBuilder result = new StringBuilder();
        for (int i = 0; i <= input.length() - 1; i++) {
            if (i != input.length() - 1) {
                int first = Integer.parseInt(String.valueOf(input.charAt(i)));
                int second = Integer.parseInt(String.valueOf(input.charAt(i + 1)));
                if (!(first % 2 == 0) && !(second % 2 == 0)) {
                    result.append(first)
                          .append("-");
                } else {
                    result.append(first);
                }
            } else {
                char lastDigit = input.charAt(i);
                result.append(lastDigit);
            }
		}
        return result.toString();
	}
	
	public static void main(String[] args) {
		OddNumbers number = new OddNumbers();
        System.out.println(number.dashInsert(99946));
        System.out.println(number.dashInsert(56730));
	}
}
