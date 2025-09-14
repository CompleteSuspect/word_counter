import sys #for sys.argv practice
from collections import Counter #for learning the Counter class, a subclass of Dict.
import re #for learning a simple regex formula for normalising text

if len(sys.argv) < 2: #using sys.argv for learning
    print("Usage: python wordcount.py <input_file> [output_file]") #<> means requires [] means optional
    sys.exit(1) # 1 signals something went wrong

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else "results.txt" #first time using conditional expression

print(output_file)

def normalise(raw_s, as_lst = False): #mynormaliser function, which uses re.findall to capture good text()
    new_lst = re.findall(r"([a-z]+)", raw_s.lower())  #it also converts string into lowecase

    if as_lst:
        return new_lst #return as list optional
    
    new_str = " ".join(new_lst).rstrip()
    return new_str #return as string default

with open(input_file, 'r', encoding='utf-8') as f: #encoding to handle unicode
    counts = Counter(normalise(f.read(), as_lst = True)) #using Counter to avoid boilerplate

sorted_words = sorted(counts.items(), key=lambda x: (-x[1], -len(x[0]))) #sorting values by value then char count

with open(output_file, 'w') as f: #write the results into an output file
    for word, count in sorted_words:
        f.write(f'{word} has appeared: {count} times.\n')
        print(word, count)

    most_common = counts.most_common(1) #maybe this could be tidier, but this prints most common word
    f.write(f'The most common word is: "{most_common[0][0]}", which appeared: {most_common[0][1]} times')