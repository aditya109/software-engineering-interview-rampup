package io.github.mainapp;

import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.ArgumentsProvider;

import java.util.stream.Stream;

public class TestArgumentsProvider implements ArgumentsProvider {
    @Override
    public Stream<? extends Arguments> provideArguments(ExtensionContext context) {
        return Stream.of(
                Arguments.of(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 3, 16),
                Arguments.of(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 4, 19),
                Arguments.of(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 5, 26),
                Arguments.of(new int[] { 4, 2, 1, 7, 8, 8, 1, 0 }, 3, 23)

        );
    }
}
