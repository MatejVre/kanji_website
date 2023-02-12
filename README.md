# kanji_website
This is a student project used for learning web development using Django and Bootstrap.

I have created my own mini database with the help of 
Tamaoka, K., Makioka, S., Sanders, S. & Verdonschot, R.G. (2017). www.kanjidatabase.com: A new interactive online database for psychological and linguistic research on Japanese kanji and their compound words. Psychological Research. 81, 696-708
from which i got an XML of all the kanji

Because i was used to the way JISHO.org organized their kanji with readings and meanings, i have then used the JISHO api, to add meanings and proper readings split to kunyomi and onyomi.

The website uses django, to filter the database based on the picked JLPT level. It displays all of the characters within a level, allowing the user to browse. 
When a user clicks on a character, they are taken to a detailed page, describing the characters meaning, readings, classification and number of strokes.

I have then added a practice section, with which users can practice meanings of characters in the desired class.
