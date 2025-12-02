import difflib

tokens = input("Enter tokens (separated by space): ").split()
identifier_count = 0
keyword_count = 0



    
keywords = ["When-galaxy", "Blow","Other-galaxy","Other-universe","N-cycle","Repeat","Occurrence","Wave","Micro-wave","Planet","Meteor","Blackhole","Echo","Absorb","Molten","Frozen"]

for input_string in tokens:
    match = difflib.get_close_matches(input_string, keywords, n=1, cutoff=0.5)
    if match:
        match[0]

    inputstr = list(input_string)
    accepted = False
    printed = False
    state = 1
    
          
    # Keyword When-galaxy 
    if not accepted:
        state = 1
        error_message = ""
        
        for ch in input_string:
            match state:
                case 1:
                    if ch == 'W':
                        state = 2
                    else:
                        error_message = "Keyword must start with uppercase 'W'. Correct form: When-galaxy"
                        state = -1
                        break
                case 2:
                    if ch == 'h':
                        state = 3
                    else:
                        error_message = "After 'W' must come 'h'. Correct form: When-galaxy"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Wh' must come 'e'. Correct form: When-galaxy"
                        state = -1
                        break
                case 4:
                    if ch == 'n':
                        state = 5
                    else:
                        error_message = "After 'Whe' must come 'n'. Correct form: When-galaxy"
                        state = -1
                        break
                case 5:
                    if ch == '-':
                        state = 6
                    else:
                        error_message = "After 'When' must come '-'. Correct form: When-galaxy"
                        state = -1
                        break
                case 6:
                    if ch == 'g':
                        state = 7
                    else:
                        error_message = "After 'When-' must come 'g'. Correct form: When-galaxy"
                        state = -1
                        break
                case 7:
                    if ch == 'a':
                        state = 8
                    else:
                        error_message = "After 'When-g' must come 'a'. Correct form: When-galaxy"
                        state = -1
                        break
                case 8:
                    if ch == 'l':
                        state = 9
                    else:
                        error_message = "After 'When-ga' must come 'l'. Correct form: When-galaxy"
                        state = -1
                        break
                case 9:
                    if ch == 'a':
                        state = 10
                    else:
                        error_message = "After 'When-gal' must come 'a'. Correct form: When-galaxy"
                        state = -1
                        break
                case 10:
                    if ch == 'x':
                        state = 11
                    else:
                        error_message = "After 'When-gala' must come 'x'. Correct form: When-galaxy"
                        state = -1
                        break
                case 11:
                    if ch == 'y':
                        state = 12
                    else:
                        error_message = "After 'When-galax' must come 'y'. Correct form: When-galaxy"
                        state = -1
                        break
                case 12:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break

        if state == 12:
            keyword_count += 1
            print(f"KEYWORD (if statement) {keyword_count}: {input_string}")
            accepted = True
        elif error_message and not printed and match == ['When-galaxy']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True
            

    # Keyword blow 
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'B':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'B'. Correct form: Blow"
                        state = -1
                        break
                case 1:
                    if ch == 'l':
                        state = 2
                    else:
                        error_message = "After 'B' must come 'l'. Correct form: Blow"
                        state = -1
                        break
                case 2:
                    if ch == 'o':
                        state = 3
                    else:
                        error_message = "After 'Bl' must come 'o'. Correct form: Blow"
                        state = -1
                        break
                case 3:
                    if ch == 'w':
                        state = 4
                    else:
                        error_message = "After 'Blo' must come 'w'. Correct form: Blow"
                        state = -1
                        break
                case 4:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break

        if state == 4:
            keyword_count += 1
            print(f"KEYWORD (return statement) {keyword_count}: {input_string}")
            accepted = True
        elif error_message and not printed and match == ['Blow']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True            
           
    # keyword "Other-galaxy"
    if not accepted:
        state = 0
        error_message = ""
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'O':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'O'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 1:
                    if ch == 't':
                        state = 2
                    else:
                        error_message = "After 'O' must come 't'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 2:
                    if ch == 'h':
                        state = 3
                    else:
                        error_message = "After 'Ot' must come 'h'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Oth' must come 'e'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 4:
                    if ch == 'r':
                        state = 5
                    else:
                        error_message = "After 'Othe' must come 'r'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 5:
                    if ch == '-':
                        state = 6
                    else:
                        error_message = "After 'Other' must come '-'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 6:
                    if ch == 'g':
                        state = 7
                    else:
                        error_message = "After 'Other-' must come 'g'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 7:
                    if ch == 'a':
                        state = 8
                    else:
                        error_message = "After 'Other-g' must come 'a'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 8:
                    if ch == 'l':
                        state = 9
                    else:
                        error_message = "After 'Other-ga' must come 'l'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 9:
                    if ch == 'a':
                        state = 10
                    else:
                        error_message = "After 'Other-gal' must come 'a'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 10:
                    if ch == 'x':
                        state = 11
                    else:
                        error_message = "After 'Other-gala' must come 'x'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 11:
                    if ch == 'y':
                        state = 12
                    else:
                        error_message = "After 'Other-galax' must come 'y'. Correct form: Other-galaxy"
                        state = -1
                        break
                case 12:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                

        if state == 12:
            keyword_count += 1
            print(f"KEYWORD (else if statement) {keyword_count}: {input_string}")
            accepted = True
        elif error_message and not printed and match == ['Other-galaxy']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True   
          

    # keyword "Other-universe"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'O':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'O'. Correct form: Other-universe"
                        state = -1
                        break
                case 1:
                    if ch == 't':
                        state = 2
                    else:
                        error_message = "After 'O' must come 't'. Correct form: Other-universe"
                        state = -1
                        break
                case 2:
                    if ch == 'h':
                        state = 3
                    else:
                        error_message = "After 'Ot' must come 'h'. Correct form: Other-universe"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Oth' must come 'e'. Correct form: Other-universe"
                        state = -1
                        break
                case 4:
                    if ch == 'r':
                        state = 5
                    else:
                        error_message = "After 'Othe' must come 'r'. Correct form: Other-universe"
                        state = -1
                        break
                case 5:
                    if ch == '-':
                        state = 6
                    else:
                        error_message = "After 'Other' must come '-'. Correct form: Other-universe"
                        state = -1
                        break
                case 6:
                    if ch == 'u':
                        state = 7
                    else:
                        error_message = "After 'Other-' must come 'u'. Correct form: Other-universe"
                        state = -1
                        break
                case 7:
                    if ch == 'n':
                        state = 8
                    else:
                        error_message = "After 'Other-u' must come 'n'. Correct form: Other-universe"
                        state = -1
                        break
                case 8:
                    if ch == 'i':
                        state = 9
                    else:
                        error_message = "After 'Other-un' must come 'i'. Correct form: Other-universe"
                        state = -1
                        break
                case 9:
                    if ch == 'v':
                        state = 10
                    else:
                        error_message = "After 'Other-uni' must come 'v'. Correct form: Other-universe"
                        state = -1
                        break
                case 10:
                    if ch == 'e':
                        state = 11
                    else:
                        error_message = "After 'Other-univ' must come 'e'. Correct form: Other-universe"
                        state = -1
                        break
                case 11:
                    if ch == 'r':
                        state = 12
                    else:
                        error_message = "After 'Other-unive' must come 'r'. Correct form: Other-universe"
                        state = -1
                        break
                case 12:
                    if ch == 's':
                        state = 13
                    else:
                        error_message = "After 'Other-univer' must come 's'. Correct form: Other-universe"
                        state = -1
                        break
                case 13:
                    if ch == 'e':
                        state = 14
                    else:
                        error_message = "After 'Other-univers' must come 'e'. Correct form: Other-universe"
                        state = -1
                        break
                case 14:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 14:
            keyword_count += 1
            print(f"KEYWORD (else statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Other-universe']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 
    # keyword "N-cycle"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'N':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'N'. Correct form: N-cycle"
                        state = -1
                        break
                case 1:
                    if ch == '-':
                        state = 2
                    else:
                        error_message = "After 'N' must come '-'. Correct form: N-cycle"
                        state = -1
                        break
                case 2:
                    if ch == 'c':
                        state = 3
                    else:
                        error_message = "After 'N-' must come 'c'. Correct form: N-cycle"
                        state = -1
                        break
                case 3:
                    if ch == 'y':
                        state = 4
                    else:
                        error_message = "After 'N-c' must come 'y'. Correct form: N-cycle"
                        state = -1
                        break
                case 4:
                    if ch == 'c':
                        state = 5
                    else:
                        error_message = "After 'N-cy' must come 'c'. Correct form: N-cycle"
                        state = -1
                        break
                case 5:
                    if ch == 'l':
                        state = 6
                    else:
                        error_message = "After 'N-cyc' must come 'l'. Correct form: N-cycle"
                        state = -1
                        break
                case 6:
                    if ch == 'e':
                        state = 7
                    else:
                        error_message = "After 'N-cycl' must come 'e'. Correct form: N-cycle"
                        state = -1
                        break
                case 7:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break
                
        if state == 7:
            keyword_count += 1
            print(f"KEYWORD (for-loop statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['N-cycle']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True
    # keyword "Repeat"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'R':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'R'. Correct form: Repeat"
                        state = -1
                        break
                case 1:
                    if ch == 'e':
                        state = 2
                    else:
                        error_message = "After 'R' must come 'e'. Correct form: Repeat"
                        state = -1
                        break
                case 2:
                    if ch == 'p':
                        state = 3
                    else:
                        error_message = "After 'Re' must come 'p'. Correct form: Repeat"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Rep' must come 'e'. Correct form: Repeat"
                        state = -1
                        break
                case 4:
                    if ch == 'a':
                        state = 5
                    else:
                        error_message = "After 'Repe' must come 'a'. Correct form: Repeat"
                        state = -1
                        break
                case 5:
                    if ch == 't':
                        state = 6
                    else:
                        error_message = "After 'Repea' must come 't'. Correct form: Repeat"
                        state = -1
                        break
                case 6:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break
                                                                       
        if state == 6:
            keyword_count += 1
            print(f"KEYWORD (while-loop statement) {keyword_count}: {input_string}")
            accepted = True  
        elif error_message and not printed and match == ['Repeat']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True
    # keyword "Wave"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'W':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'W'. Correct form: Wave"
                        state = -1
                        break
                case 1:
                    if ch == 'a':
                        state = 2
                    else:
                        error_message = "After 'W' must come 'a'. Correct form: Wave"
                        state = -1
                        break
                case 2:
                    if ch == 'v':
                        state = 3
                    else:
                        error_message = "After 'Wa' must come 'v'. Correct form: Wave"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Wav' must come 'e'. Correct form: Wave"
                        state = -1
                        break
                case 4:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                              

        if state == 4:
            keyword_count += 1
            print(f"KEYWORD (string statement) {keyword_count}: {input_string}")
            accepted = True 
        elif error_message and not printed and match == ['Wave']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True
    # keyword "Micro-wave"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'M':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'M'. Correct form: Micro-wave"
                        state = -1
                        break
                case 1:
                    if ch == 'i':
                        state = 2
                    else:
                        error_message = "After 'M' must come 'i'. Correct form: Micro-wave"
                        state = -1
                        break
                case 2:
                    if ch == 'c':
                        state = 3
                    else:
                        error_message = "After 'Mi' must come 'c'. Correct form: Micro-wave"
                        state = -1
                        break
                case 3:
                    if ch == 'r':
                        state = 4
                    else:
                        error_message = "After 'Mic' must come 'r'. Correct form: Micro-wave"
                        state = -1
                        break
                case 4:
                    if ch == 'o':
                        state = 5
                    else:
                        error_message = "After 'Micr' must come 'o'. Correct form: Micro-wave"
                        state = -1
                        break
                case 5:
                    if ch == '-':
                        state = 6
                    else:
                        error_message = "After 'Micro' must come '-'. Correct form: Micro-wave"
                        state = -1
                        break
                case 6:
                    if ch == 'w':
                        state = 7
                    else:
                        error_message = "After 'Micro-' must come 'w'. Correct form: Micro-wave"
                        state = -1
                        break
                case 7:
                    if ch == 'a':
                        state = 8
                    else:
                        error_message = "After 'Micro-w' must come 'a'. Correct form: Micro-wave"
                        state = -1
                        break
                case 8:
                    if ch == 'v':
                        state = 9
                    else:
                        error_message = "After 'Micro-wa' must come 'v'. Correct form: Micro-wave"
                        state = -1
                        break
                case 9:
                    if ch == 'e':
                        state = 10
                    else:
                        error_message = "After 'Micro-wav' must come 'e'. Correct form: Micro-wave"
                        state = -1
                        break
                case 10:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                              

        if state == 10:
            keyword_count += 1
            print(f"KEYWORD (char statement) {keyword_count}: {input_string}")
            accepted = True 
        elif error_message and not printed and match == ['Micro-wave']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True            
    #keyword : Planet
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'P':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'P'. Correct form: Planet"
                        state = -1
                        break
                case 1:
                    if ch == 'l':
                        state = 2
                    else:
                        error_message = "After 'P' must come 'l'. Correct form: Planet"
                        state = -1
                        break
                case 2:
                    if ch == 'a':
                        state = 3
                    else:
                        error_message = "After 'Pl' must come 'a'. Correct form: Planet"
                        state = -1
                        break
                case 3:
                    if ch == 'n':
                        state = 4
                    else:
                        error_message = "After 'Pla' must come 'n'. Correct form: Planet"
                        state = -1
                        break
                case 4:
                    if ch == 'e':
                        state = 5
                    else:
                        error_message = "After 'Plan' must come 'e'. Correct form: Planet"
                        state = -1
                        break
                case 5:
                    if ch == 't':
                        state = 6
                    else:
                        error_message = "After 'Plane' must come 't'. Correct form: Planet"
                        state = -1
                        break
                case 6:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break
                
        if state == 6:
            keyword_count += 1
            print(f"KEYWORD (integer-numbers statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Planet']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True

    # keyword "Occurrence"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'O':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'O'. Correct form: Occurrence"
                        state = -1
                        break
                case 1:
                    if ch == 'c':
                        state = 2
                    else:
                        error_message = "After 'O' must come 'c'. Correct form: Occurrence"
                        state = -1
                        break
                case 2:
                    if ch == 'c':
                        state = 3
                    else:
                        error_message = "After 'Oc' must come 'c'. Correct form: Occurrence"
                        state = -1
                        break
                case 3:
                    if ch == 'u':
                        state = 4
                    else:
                        error_message = "After 'Occ' must come 'u'. Correct form: Occurrence"
                        state = -1
                        break
                case 4:
                    if ch == 'r':
                        state = 5
                    else:
                        error_message = "After 'Occu' must come 'r'. Correct form: Occurrence"
                        state = -1
                        break
                case 5:
                    if ch == 'r':
                        state = 6
                    else:
                        error_message = "After 'Occur' must come 'r'. Correct form: Occurrence"
                        state = -1
                        break
                case 6:
                    if ch == 'e':
                        state = 7
                    else:
                        error_message = "After 'Occurr' must come 'e'. Correct form: Occurrence"
                        state = -1
                        break
                case 7:
                    if ch == 'n':
                        state = 8
                    else:
                        error_message = "After 'Occurre' must come 'n'. Correct form: Occurrence"
                        state = -1
                        break
                case 8:
                    if ch == 'c':
                        state = 9
                    else:
                        error_message = "After 'Occurren' must come 'c'. Correct form: Occurrence"
                        state = -1
                        break
                case 9:
                    if ch == 'e':
                        state = 10
                    else:
                        error_message = "After 'Occurrenc' must come 'e'. Correct form: Occurrence"
                        state = -1
                        break
                case 10:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                              

        if state == 10:
            keyword_count += 1
            print(f"KEYWORD (defining function statement) {keyword_count}: {input_string}")
            accepted = True 
        elif error_message and not printed and match == ['Occurrence']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True

    # keyword "Meteor"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'M':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'M'. Correct form: Meteor"
                        state = -1
                        break
                case 1:
                    if ch == 'e':
                        state = 2
                    else:
                        error_message = "After 'M' must come 'e'. Correct form: Meteor"
                        state = -1
                        break
                case 2:
                    if ch == 't':
                        state = 3
                    else:
                        error_message = "After 'Me' must come 't'. Correct form: Meteor"
                        state = -1
                        break
                case 3:
                    if ch == 'e':
                        state = 4
                    else:
                        error_message = "After 'Met' must come 'e'. Correct form: Meteor"
                        state = -1
                        break
                case 4:
                    if ch == 'o':
                        state = 5
                    else:
                        error_message = "After 'Mete' must come 'o'. Correct form: Meteor"
                        state = -1
                        break
                case 5:
                    if ch == 'r':
                        state = 6
                    else:
                        error_message = "After 'Meteo' must come 'r'. Correct form: Meteor"
                        state = -1
                        break
                case 6:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 6:
            keyword_count += 1
            print(f"KEYWORD (float-numbers statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Meteor']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True             

    # keyword "Blackhole"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'B':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'B'. Correct form: Blackhole"
                        state = -1
                        break
                case 1:
                    if ch == 'l':
                        state = 2
                    else:
                        error_message = "After 'B' must come 'l'. Correct form: Blackhole"
                        state = -1
                        break
                case 2:
                    if ch == 'a':
                        state = 3
                    else:
                        error_message = "After 'Bl' must come 'a'. Correct form: Blackhole"
                        state = -1
                        break
                case 3:
                    if ch == 'c':
                        state = 4
                    else:
                        error_message = "After 'Bla' must come 'c'. Correct form: Blackhole"
                        state = -1
                        break
                case 4:
                    if ch == 'k':
                        state = 5
                    else:
                        error_message = "After 'Blac' must come 'k'. Correct form: Blackhole"
                        state = -1
                        break
                case 5:
                    if ch == 'h':
                        state = 6
                    else:
                        error_message = "After 'Black' must come 'h'. Correct form: Blackhole"
                        state = -1
                        break
                case 6:
                    if ch == 'o':
                        state = 7
                    else:
                        error_message = "After 'Blackh' must come 'o'. Correct form: Blackhole"
                        state = -1
                        break
                case 7:
                    if ch == 'l':
                        state = 8
                    else:
                        error_message = "After 'Blackho' must come 'l'. Correct form: Blackhole"
                        state = -1
                        break
                case 8:
                    if ch == 'e':
                        state = 9
                    else:
                        error_message = "After 'Blackhol' must come 'e'. Correct form: Blackhole"
                        state = -1
                        break
                case 9:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 9:
            keyword_count += 1
            print(f"KEYWORD (null statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Blackhole']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 

    # keyword "Echo"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'E':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'E'. Correct form: Echo"
                        state = -1
                        break
                case 1:
                    if ch == 'c':
                        state = 2
                    else:
                        error_message = "After 'E' must come 'c'. Correct form: Echo"
                        state = -1
                        break
                case 2:
                    if ch == 'h':
                        state = 3
                    else:
                        error_message = "After 'Ec' must come 'h'. Correct form: Echo"
                        state = -1
                        break
                case 3:
                    if ch == 'o':
                        state = 4
                    else:
                        error_message = "After 'Ech' must come 'o'. Correct form: Echo"
                        state = -1
                        break
                case 4:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 4:
            keyword_count += 1
            print(f"KEYWORD (print statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Echo']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 

    # keyword "Absorb"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'A':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'A'. Correct form: Absorb"
                        state = -1
                        break
                case 1:
                    if ch == 'b':
                        state = 2
                    else:
                        error_message = "After 'A' must come 'b'. Correct form: Absorb"
                        state = -1
                        break
                case 2:
                    if ch == 's':
                        state = 3
                    else:
                        error_message = "After 'Ab' must come 's'. Correct form: Absorb"
                        state = -1
                        break
                case 3:
                    if ch == 'o':
                        state = 4
                    else:
                        error_message = "After 'Abs' must come 'o'. Correct form: Absorb"
                        state = -1
                        break
                case 4:
                    if ch == 'r':
                        state = 5
                    else:
                        error_message = "After 'Abso' must come 'r'. Correct form: Absorb"
                        state = -1
                        break
                case 5:
                    if ch == 'b':
                        state = 6
                    else:
                        error_message = "After 'Absor' must come 'b'. Correct form: Absorb"
                        state = -1
                        break
                case 5:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 14:
            keyword_count += 1
            print(f"KEYWORD (input statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Absorb']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 

    # keyword "Molten"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'M':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'M'. Correct form: Molten"
                        state = -1
                        break
                case 1:
                    if ch == 'o':
                        state = 2
                    else:
                        error_message = "After 'M' must come 'o'. Correct form: Molten"
                        state = -1
                        break
                case 2:
                    if ch == 'l':
                        state = 3
                    else:
                        error_message = "After 'Mo' must come 'l'. Correct form: Molten"
                        state = -1
                        break
                case 3:
                    if ch == 't':
                        state = 4
                    else:
                        error_message = "After 'Mol' must come 't'. Correct form: Molten"
                        state = -1
                        break
                case 4:
                    if ch == 'e':
                        state = 5
                    else:
                        error_message = "After 'Molt' must come 'e'. Correct form: Molten"
                        state = -1
                        break
                case 5:
                    if ch == 'n':
                        state = 6
                    else:
                        error_message = "After 'Molte' must come 'n'. Correct form: Molten"
                        state = -1
                        break
                case 6:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 6:
            keyword_count += 1
            print(f"KEYWORD (True(boolean type) statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Molten']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 

    # keyword "Frozen"
    if not accepted:
        state = 0
        for ch in input_string:
            match state:
                case 0:
                    if ch == 'F':
                        state = 1
                    else:
                        error_message = "Keyword must start with uppercase 'F'. Correct form: Frozen"
                        state = -1
                        break
                case 1:
                    if ch == 'r':
                        state = 2
                    else:
                        error_message = "After 'F' must come 'r'. Correct form: Frozen"
                        state = -1
                        break
                case 2:
                    if ch == 'o':
                        state = 3
                    else:
                        error_message = "After 'Fr' must come 'o'. Correct form: Frozen"
                        state = -1
                        break
                case 3:
                    if ch == 'z':
                        state = 4
                    else:
                        error_message = "After 'Fro' must come 'z'. Correct form: Frozen"
                        state = -1
                        break
                case 4:
                    if ch == 'e':
                        state = 5
                    else:
                        error_message = "After 'Froz' must come 'e'. Correct form: Frozen"
                        state = -1
                        break
                case 5:
                    if ch == 'n':
                        state = 6
                    else:
                        error_message = "After 'Froze' must come 'n'. Correct form: Frozen"
                        state = -1
                        break
                case 6:
                    error_message = "😡 Extra characters after valid keyword."
                    state = -1
                    break                                                                               
        if state == 6:
            keyword_count += 1
            print(f"KEYWORD (False(boolean type) statement) {keyword_count}: {input_string}")
            accepted = True   
        elif error_message and not printed and match == ['Frozen']:
            print(f"🥺 Invalid keyword: {input_string} 👉 {error_message}") 
            printed = True 

    # Check for identifier
    if not accepted:
        state = 0
        error_message_id = ""
        for ch in input_string:
            match state:
                case 0:
                    if 'A' <= ch <= 'Z':
                        state = 1
                    else:
                        error_message_id = "Identifiers must start with a capital letter (A-Z). Example: Esasa2!"
                        state = -1
                        break
                case 1:
                    if 'a' <= ch <= 'z' or '0' <= ch <= '9':
                        state = 1
                    elif ch == '!':
                        state = 2
                    else:
                        error_message_id = f"Invalid character '{ch}' in identifier. Allowed: lowercase letters or digits, then '!'."
                        state = -1
                        break
                case 2:
                    error_message_id = "Nothing should come after '!' in identifier."
                    state = -1
                    break

        # --- FIX: handle case where input ended in state 1 (no '!') ---
        if state == 2:
            identifier_count += 1
            print(f"✅ IDENTIFIER {identifier_count}: {input_string}")
            accepted = True
        elif state == 1:
            # if we ended normally in state 1 (valid chars but missing '!'):
            
            error_message_id = "Identifier must end with '!' . Correct example: Esasa2!"
            # only print if we haven't printed some earlier message for this token
        if error_message_id and not printed:
            print(f"❌ Invalid identifier: {input_string} 👉 {error_message_id}")
            printed = True

print(f"\n📊 Total: {keyword_count} keywords, {identifier_count} identifiers") 