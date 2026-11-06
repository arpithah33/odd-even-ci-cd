package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {

    @Test
    public void testEven() {
        assertEquals("Even", App.checkEvenOdd(4));
    }

    @Test
    public void testOdd() {
        assertEquals("Odd", App.checkEvenOdd(5));
    }

    @Test
    public void testZero() {
        assertEquals("Even", App.checkEvenOdd(0));
    }
}