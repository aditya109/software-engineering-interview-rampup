# Regex Expression

## Terminology 

- pattern: regular expression pattern
- string: test string used to match the pattern
- digit: 0-9
- letter: a-z, A-Z
- symbol: !$%^&*()_+|~-=`{}[]:”;'<>?,./
- space: single white space, tab
- character: refers to a letter, digit, or symbol

## Basics

**Mixed range:** `[a-zA-Z0-9]`  Do note that a range only specifies multiple alternatives for a **single character** in a pattern.

## Repeating Characters

```
[a-z][a-z][a-z]
```

This would match all three-letter words.

There’s a better way to express such a pattern using the `{}` curly braces notation. 

 Here are examples:

- `a{5}` will match “aaaaa”.
- `n{3}` will match “nnn”.
- `[a-z]{4}` will match any four-letter word such as “door”, “room” or “book”.
- `[a-z]{6,}` will match any word with six or more letters.
- `[a-z]{8,11}` will match any word between eight and 11 letters. Basic password validation can be done this way.
- `[0-9]{11}` will match an 11-digit number. Basic international phone validation can be done this way.

## Metacharacters

Metacharacters allow you to write regular expression patterns that are even more compact. Let’s go through them one by one:

- `\d` matches any digit that is the same as `[0-9]`
- `\w` matches any letter, digit and underscore character
- `\s` matches a whitespace character — that is, a space or tab
- `\t` matches a tab character only

From what we’ve learned so far, we can write regular expressions like this:

- `\w{5}` matches any five-letter word or a five-digit number
- `\d{11}` matches an 11-digit number such as a phone number

## Special characters:

| Character | Usage                                                        |      |
| --------- | ------------------------------------------------------------ | ---- |
| `+`       | One or more quantifiers (preceding character must exist and can be optionally duplicated). For example, the expression `c+at` will match “cat”, “ccat” and “ccccccccat”. You can repeat the preceding character as many times as you like and you’ll still get a match. |      |
| `?`       | Zero or one quantifier (preceding character is optional). For example, the expression `c?at` will only match “cat” or “at”. |      |
| `*`       | Zero or more quantifier (preceding character is optional and can be optionally duplicated). For example, the expression `c*at` will match “at”, “cat” and “ccccccat”. It’s like the combination of `+` and `?`. |      |
| `\`       | this “escape character” is used when we want to use a special character literally. For example, `c\*` will exactly match “c*” and not “ccccccc”. |      |
| `[^]`     | this “negate” notation is used to indicate a character that should not be matched within a range. For example, the expression `b[^a-c]ld` will not match “bald” or “bbld” because the second letters a to c are negative. However, the pattern will match “beld”, “bild”, “bold” and so forth. |      |
| `.`       | this “do” notation will match any digit, letter or symbol except newline. For example, `.{8}` will match a an eight-character password consisting of letters, numbers and symbols. for example, “password” and “P@ssw0rd” will both match. |      |

For example:

- `.+` matches one or an unlimited number of characters. For example, “c” , “cc” and “bcd#.670” will all match.
- `[a-z]+` will match all lowercase letter words irrespective of length, as long as they contain at least one letter. For example, “book” and “boardroom” will both match.

## Groups

All the special characters we just mentioned only affect a single character or a range set. What if we wanted the effect to apply to a *section* of the expression? We can do this by creating groups using round brackets — `()`. For example, the pattern `book(.com)?` will match both “book” and “book.com”, since we’ve made the “.com” part optional.

## Alternate Characters

In regex, we can specify alternate characters using the “pipe” symbol — `|`. This is different from the special characters we showed earlier as it affects all the characters on each side of the pipe symbol. For example, the pattern `sat|sit` will match both “sat” and “sit” strings. We can rewrite the pattern as `s(a|i)t` to match the same strings.

The above pattern can be expressed as `s(a|i)t` by using `()` parentheses.

## Starting and Ending Patterns

You may have noticed that some positive matches are a result of partial matching. For example, if I wrote a pattern to match the string “boo”, the string “book” will get a positive match as well, despite not being an exact match. To remedy this, we’ll use the following notations:

- `^`: placed at the start, this character matches a pattern at the start of a string.
- `$`: placed at the end, this character matches a pattern at the end of the string.