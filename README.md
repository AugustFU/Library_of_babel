# Library Of Pybel

https://user-images.githubusercontent.com/86366345/184909568-625a3756-7a6f-49be-aa78-6713355cf627.mp4

## About

What was needed for this project was a way to generate seemingly random pages in a near-infinite address space which could also be searched for specific strings.

I realized not early on that what I needed was not a reversible RNG, but in fact an encoding scheme to cleverly encode the page's text in the address of the book. Paired with a seeded RNG for shorter pages, I could reliably generate random pages, but also encode specific text into the page to be generated.

To understand the encoding, you must think of the hex address of the book as a base-36 number and the text of the book as a base-29 number (26 letters plus space, comma, and period). The wall, shelf, volume, and page can be thought of as a base-10 number independent of the hex address. This base-10 number will be referred to as the location.

Specifically, when text is searched for, that text is padded with a random amount of characters on it's front and back side, or in the case of the `Page only contains`, it's padded with spaces on it's back side. Then, a random number in the range of each location value is calculated.

The page text is then converted from a string to a number. The location number is multiplied by a very large number and is then added to the page text number. Then the new page text number is converted into base-36, and that is the address.

Address format: `Hex_Value`:`Wall`:`Shelf`:`Volume`:`Page`

