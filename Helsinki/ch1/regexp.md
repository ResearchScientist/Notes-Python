Regular expressions are used to match patterns within strings.

`[Aa]` any variation of A or a

`|` or

`[a-zA-Z]` range a to z and A-Z

`ab*` any multiple of b : bb , bbb

`\Z` end of string

`r"some pattern"` raw string that doesn't interpret any special syntax such as `\n` or `\t` within the pattern given

`\` escapes special characters

`^` start of string match

`$` end of string match

`?` 0 or 1 previous occurrences

`{n1,n2}` n1 to n2 previous occurrences

`*` 0 or more previous matches

`+` 1 or more previous matches

The `re` module helps working with regular expressions.

