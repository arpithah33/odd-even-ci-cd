package com.example;

import java.util.Scanner;

public class App {

    public static String checkEvenOdd(int n) {
        if (n % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        System.out.println(checkEvenOdd(n));

        sc.close();
    }
}