import sys #for sys.argv practice
from pathlib import Path
from collections import Counter #for learning the Counter class, a subclass of Dict.
import re #for learning a simple regex formula for normalising text

if len(sys.argv) < 2: #using sys.argv for learning
    print("Usage: python word_counter.py <input_file> [output_file]") #<> means requires [] means optional
    sys.exit(1) # 1 signals something went wrong

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else "results.txt" #first time using conditional expression

def load_stopwords(filename ="stopwords.txt"):
    p = Path(filename)
    if p.exists():
        with p.open(encoding="utf8") as f:
            return {line.strip().lower() for line in f}
    else:
        p.write_text('', encoding = 'utf8')
        return set()
        
def normalise(raw_s, as_lst = False): #mynormaliser function, which uses re.findall to capture good text()
    new_lst = re.findall((r"\b(?:[ai]|[a-z]{2,})\b"), raw_s.lower())  #single ch words a or i only or a to z if more than 2 ch

    if as_lst:
        return new_lst #return as list optional
    
    new_str = " ".join(new_lst).rstrip()
    return new_str #return as string default

with open(input_file, 'r', encoding='utf-8') as f: #encoding to handle unicode
    stop_words = load_stopwords()
    counts = Counter(word for word in normalise(f.read(), as_lst = True) if word not in stop_words) #using Counter to avoid boilerplate
    

sorted_words = sorted(counts.items(), key=lambda x: (-x[1], -len(x[0]))) #sorting values by value then char count

with open(output_file, 'w', encoding='utf-8') as f: #write the results into an output file
    for word, count in sorted_words:
        f.write(f'{word} has appeared: {count} times.\n')

    f.write(f'The most common word is: "{sorted_words[0][0]}", which appeared: {sorted_words[0][1]} times')
print('done')