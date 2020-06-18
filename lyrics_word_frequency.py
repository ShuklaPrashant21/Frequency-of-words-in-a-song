##Find frequency of each word in a song by using dictionary.

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    
    
let_it_be = ("""When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness She is standing right in front of men Speaking words of wisdom let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be And when the broken hearted people Living in the world agree There will be an answer let it be For though they may be parted There is still a chance that they will see There will be an answer let it be Let it be let it be Let it be let it be There will be an answer let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be Let it be let it be Let it be yeah let it be Whisper words of wisdom let it be And when the night is cloudy There is still a light that shines on me Shine on until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be And let it be let it be Let it be let it be Whisper words of wisdom let it be Let it be let it be Let it be yeah let it be Whisper words of wisdom let it be"""
)

let_It_be_lower = let_it_be.lower()
let_it_be_list = list(let_It_be_lower.split(" "))

beatles = lyrics_to_frequencies(let_it_be_list)

print(beatles)

##Find words which occurs more than or equals to x times.

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result

x = int(input("Enter minimum occurence of a word :"))

print(words_often(beatles, x))














      
