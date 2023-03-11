# SearchEach

First. Thanks for seing this.

Second. If the program has an error please report it. My Discord is: ESFLOWNK#0119.

# How to use

If you open the program normally, the program will suddenly close.

-- Instructions --

1.- Open the cmd or powershell.

2.- Write this on the terminal:

    searcheach <file_to_read> <searched_character> <file_with_the_results>

file_to_read: The file where the program will search.

searched_character: The character that the program will search and show it's content.

file_with_the_results: The program will create this file and write the results there.

# Example

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

# Extra

If you want to search things between quotes ("), in the cmd isn't a problem (i think), but in the powershell happens this (at least to me):

    PS C:\Users\ESFLOWNK> searcheach file.txt " results.txt
    >>
    >>
    >>

If it happens then you have to write this instead:

    PS C:\Users\User> searcheach file.txt strings results.txt

(The word "strings" replaces the quotes to avoid problems)


If you put the quotes, don't close the powershell. press CTRL+C instead.

## Thanks for reading this :)
