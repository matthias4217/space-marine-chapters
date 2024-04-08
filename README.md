# Space Marine Chapters & Warbands

*I wanted to get random chapters for a warband projects of mine. 😅 Then I’ve realized I couldn’t find any programmatically-accessible database and thought I could create one.*

## Why ?

This project’s aim it to create a database of Space Marine chapters, both loyalists and renegades.
It does not aim to replace official publications or wiki, but rather offer a dataset usable by scripts. 
If you ever need to get a random Space Marine chapter or a list of chapters founded in the 5th founding, this should give you all the data you need.
The database is collected as a CSV, so that it can be easily read and parsed, even a couple decades from now.

## What is included

One CSV file contains all the "official" Space Marine chapters, warbands and legions.
For each one, some information has been collected.
The full list of attributes used is displayed on [this page](attributes.md).

## How to use

There are many ways to use it.
You can create a Python, JS, shell… script to parse the data.
You can import them in a spreadsheet and do some stats.
If you have access to a Bourne shell, this is how you get a single chapter : `tail -n+2 space-marine-chapters-homebrew.csv | shuf | tail -n1`.

## Contributing

This database has been generated automatically by scraping a couple of pages of the [Lexicanum](https://wh40k.lexicanum.com) as well as [Warhammer Fandom](https://warhammer40k.fandom.com/wiki/Warhammer_40k_Wiki).
This data is incomplete, and may even be incorrect.
Moreover, as Games Workshop publishes new materials, new chapters may need to be added.
Thus any help is welcome to manually address these shortcomings.

### Pointing out a problem

The easiest way to contribute is by opening an issue.
If you notice a chapter or warband is missing or some information is incorrect, please open an issue and clearly state what the problem is.
This helps a lot.

### Fixing an issue

If you have some experience with Git, you may want to open a pull/merge request fixing what needs be.

### Generating the base collection

I have including the tools that have allowed me to generate the base CSV file.
These scripts are quick and dirty, and worked when I was using them.
However, it’s likely that they break at some point in the future.
I am not planning on maintaining them forever.
If you want to improve them, great, but they are not the core feature of this project.

