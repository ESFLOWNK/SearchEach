# SearchEach

If the program has an error please report it to my gmail: otakuflownk@gmail.com

# How to use

If you open the program normally, the program will suddenly close.

-- Instructions --

1.- Open the cmd or powershell.

2.- Write this on the terminal:

    searcheach <file_to_read> <searched_character> <(Optional) second_searched_character> <file_with_the_results>

file_to_read: The file where the program will search.

searched_character: The character used for searching texts between it.

second_searched_character: (Optional) Texts will be searched between the first ingresed character and the second one.

file_with_the_results: The program will create this file and write the results there.

# News

2023 - March - 11:

* I changed the mode in which the files are read. Now the files are read so that the result is what is between the first searched character found to the last searched character found.

2024 - August - 27

* Now there's only one optimized script file.

* Two characters search feature.

# Example for one character

I create a file named "history.txt" with this content:

```text file
-The world is fantastic- and then the world exploded.
But only a kid kept living.
He happened too many adventures together to a -bear named ber-.
```

And then I open the cmd (or powershell) and write this:
```console
searcheach history.txt - results.txt
```

And then the program creates a file named "results.txt", and if you open it, this appears:

```text file
-The world is fantastic-
-bear named ber-
```

# Example for two characters

I create a text named "MathProblems.txt" that contents:

```text file
Question #1: (-1)-(4x(2-3)) =
Question #1: (-5x3)-4X =
Question #1: 6x(23-X) =
```

And then I open the cmd (or powershell) and write this:
```console
searcheach MathProblems.txt ( ) results.txt
```

And then the program creates a file named "results.txt", and if you open it, this appears:

```text file
(-1)
(4x(2-3))
(-5x3)
(23-X)
```

# Extra

If you want to search things between quotes ("), in the cmd isn't a problem (i think), but in the powershell happens this (at least to me):

    PS C:\Users\ESFLOWNK> searcheach file.txt " results.txt
    >>
    >>
    >>

If it happens then you have to write this instead:

    PS C:\Users\User> searcheach file.txt strings results.txt

(The word `"strings"` replaces the quotes to avoid problems)


If you put the quotes, don't close the powershell. press CTRL+C instead.