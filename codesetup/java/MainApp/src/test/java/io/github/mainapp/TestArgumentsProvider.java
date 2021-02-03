package io.github.mainapp;

import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.ArgumentsProvider;

import java.util.stream.Stream;

public class TestArgumentsProvider implements ArgumentsProvider {
    @Override
    public Stream<? extends Arguments> provideArguments(ExtensionContext context) {
        return Stream.of(
                Arguments.of(new int[]{3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4}, 2, 5),
                Arguments.of(new int[]{3, 3, 3, 1, 1, 2, 3, 3, 4}, 2, 5)
        );
    }
}
