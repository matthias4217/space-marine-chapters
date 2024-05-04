# Attributes

Each chapter has the following attributes. Apart of the name, they are all optional.

## Name

The name of the warband. It’s still not clear if it should be the current (M41) name, the founding name, or something else.
Find more about this issue [there](https://github.com/matthias4217/space-marine-chapters/issues/1).

## Allegiance

One of those :
* Loyalist
* Renegade/Chaos

## Faction

One of those :

* Imperium
* Chaos Undivided
* Khorne
* Slaanesh
* Tzeentch
* Nurgle

## Chapter of origin

From which chapter the Geneseed has been taken.
This is not necessarily a first-founding chapter.
Some chapters may have several parent chapters.
Their names will be separated by ` & `.

## Founding

From which founding the chapter originates.
Many Chaos warbands do not have such an attribute.
This can be :
* An integer, for the number of the founding
* A date, for the date of founding (M36 or 816.M34 for instance)
* `Ultima`, for the [Ultima founding](https://wh40k.lexicanum.com/wiki/Founding#Ultima_Founding) 

## Status

Chapter status can be :
* Active
* Destroyed
* Fusioned
* Renamed

## Legion

Boolean, True if it was part of the twenty original legions, else False.

## Homebrew

Boolean, True if this is not an official chapter, else False.
The main CSV file only features official chapters, but I have included exemples of homebrew chapters.
