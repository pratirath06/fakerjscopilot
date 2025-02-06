def load_word_dictionary():
   docs = {
       "word": {
           "adjective": {
               "description": "Returns a random adjective",
               "patterns": ["adjective", "descriptive word", "generate adjective"],
               "examples": [
                   "faker.word.adjective() // 'pungent'",
                   "faker.word.adjective(5) // 'slimy'",
                   "faker.word.adjective(100) // 'complete'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "adverb": {
               "description": "Returns a random adverb",
               "patterns": ["adverb", "word modifying verb", "generate adverb"],
               "examples": [
                   "faker.word.adverb() // 'quarrelsomely'",
                   "faker.word.adverb(5) // 'madly'",
                   "faker.word.adverb(100) // 'sadly'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "conjunction": {
               "description": "Returns a random conjunction",
               "patterns": ["conjunction", "connecting word", "generate conjunction"],
               "examples": [
                   "faker.word.conjunction() // 'in order that'",
                   "faker.word.conjunction(5) // 'since'",
                   "faker.word.conjunction(100) // 'as long as'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "interjection": {
               "description": "Returns a random interjection",
               "patterns": ["interjection", "exclamation", "generate interjection"],
               "examples": [
                   "faker.word.interjection() // 'gah'",
                   "faker.word.interjection(5) // 'fooey'",
                   "faker.word.interjection(100) // 'yowza'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "noun": {
               "description": "Returns a random noun",
               "patterns": ["noun", "naming word", "generate noun"],
               "examples": [
                   "faker.word.noun() // 'external'",
                   "faker.word.noun(5) // 'front'",
                   "faker.word.noun(100) // 'care'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "preposition": {
               "description": "Returns a random preposition",
               "patterns": ["preposition", "positional word", "generate preposition"],
               "examples": [
                   "faker.word.preposition() // 'without'",
                   "faker.word.preposition(5) // 'abaft'",
                   "faker.word.preposition(100) // 'an'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "verb": {
               "description": "Returns a random verb",
               "patterns": ["verb", "action word", "generate verb"],
               "examples": [
                   "faker.word.verb() // 'act'",
                   "faker.word.verb(5) // 'tinge'",
                   "faker.word.verb(100) // 'mess'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "sample": {
               "description": "Returns a random word of any type",
               "patterns": ["random word", "any word", "generate word"],
               "examples": [
                   "faker.word.sample() // 'incidentally'",
                   "faker.word.sample(5) // 'fruit'"
               ],
               "parameters": {
                   "length": "optional - number | {min: number, max: number} - Target word length",
                   "strategy": "optional - 'fail' | 'closest' | 'shortest' | 'longest' | 'any-length'"
               }
           },
           "words": {
               "description": "Returns random words separated by spaces",
               "patterns": ["multiple words", "word list", "generate words"],
               "examples": [
                   "faker.word.words() // 'almost'",
                   "faker.word.words(5) // 'before hourly patiently dribble equal'"
               ],
               "parameters": {
                   "count": "optional - number | {min: number, max: number} - Number of words to return"
               }
           }
       }
   }
   return docs