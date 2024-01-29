package io.github.mainapp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ArgumentsSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MainAppTest {
    private MainApp mainApp;

    @BeforeEach
    public void setUp() throws Exception {
        mainApp = new MainApp();
    }

    @ParameterizedTest
    @ArgumentsSource(TestArgumentsProvider.class)
    public void testMainAppWithTestCases(int[] arr, int k, int expectedResult) {
        int actualResult = mainApp.Run(arr, k);
        assertEquals(expectedResult, actualResult, "Wrong answer");
    }
}
