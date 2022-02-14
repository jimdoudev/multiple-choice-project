import os, time, random

#clear console / Ελέγχει τον τύπο os και καθαρίζει την κονσόλα
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Visuals / δημιουργεί τα διάφορα οπτικά εφέ
def visuals(filename):
    clearConsole()
    file = open("visuals/"+filename, "r")
    lines = file.readlines()
    for line in lines:
        print(line[:-1])
        time.sleep(0.05)
    time.sleep(1.5)

#Ιntro / Εισαγωγή του ερωτηματολογίου
def intro():
    clearConsole()
    visuals("intro.txt")
    print("\n\nΚαλωσήλθατε στην άσκηση πολλαπλών επιλογών για την ασφάλεια στο διαδίκτυο\n\n")
    name = input("Εισάγετε το ονοματεπώνυμό σας για να συνεχίσετε: ")
    for x in range(3):
        print(".\t")
        time.sleep(0.8)
    print("Το όνομα σας καταχωρήθηκε με επιτυχία. Πατήστε enter για να ξεκινήσετε...")
    input()
    clearConsole()
    return name
    

#Examination / Λογική της εξέτασης / +20 για σωστή απάντηση - +10 για σωστή 2η ευκαιρία - 0 για λάθος
def examination(lines_q, lines_a):
    answers = ["α", "β", "γ", "δ"]
    score = 0
    for x in range(2):
        answer=""
        print(lines_q[x], "\n")
        print(lines_a[x][0]+"\n")
        while answer not in answers:
            answer = input("Απάντηση: ")
        if(lines_a[x][1][answers.index(answer)] == "c"):
            score += 20
            visuals("perfect.txt")
            clearConsole()
        elif(lines_a[x][1][answers.index(answer)] == "s"):
            visuals("2nd_chance.txt")
            clearConsole()
            answer=""
            print(lines_q[x+2], "\n")
            print(lines_a[x+2][0]+"\n")
            while answer not in answers:
                answer = input("Απάντηση: ")
            if(lines_a[x+2][1][answers.index(answer)] == "c"):
                score += 10
                visuals("perfect.txt")
                clearConsole()
            else:
                visuals("bad.txt")
                clearConsole()
        else:
            visuals("bad.txt")
            clearConsole()
    return score

#Evaluation - Γενική αξιολόγηση βάσει απόδοσης στην εξέταση
def eval(lines, name):
    visuals("eval.txt")
    print("\n\n")
    score = (sum(lines)*100)/120
    print("Τελική Βαθμολογία: ", score, "/100.0\n")
    time.sleep(1)
    if score > 90:
        print("Συγχαρητήρια ", name, "! Συνέχισε έτσι για να παραμείνεις στην κορυφή!\n")
    elif score > 70:
        print("Μπράβο ", name, "! Με λίγη παραπάνω προσπάθεια θα φτάσεις ακόμη πιο ψηλά.\n")
    elif score >= 50:
        print("Καλή προσπάθεια ", name, ", χρειάζεσαι βελτίωση!\n")
    else:
        print("Μάλλον κάποιος δεν διάβασε όσο έπρεπε " , name, "! Διάβασε την ύλη και προσπάθησε ξανα!\n")
    time.sleep(1)

#Evaluation per unit - Ειδική αξιολόγηση βάσει απόδοση σε κάθε ξεχωριστή θεματική ενότητα
def unit_eval(lines):
    units = ["Μαθαίνω να προστατεύομαι", "Αποκαλύπτω με προσοχη...", "Τα φαινόμενα απατούν"]
    print("Συγκεκριμένα:\n")
    time.sleep(1)
    index = 0
    for line in lines:
        if line < 10:
            print("Στην ενότητα '", units[index], "' ήσουν τελείως αδιάβαστος! Δεν απάντησες τίποτα σωστά.\n")
        elif line < 30:
            print("Στην ενότητα '", units[index], "' απάντησες κάποια σωστά, αλλά χρειάζεσαι επανάληψη.\n")
        elif line < 40:
            print("Στην ενότητα '", units[index], "' είχες μόνο ένα λαθάκι που διόρθωσες στη 2η ευκαιρία σου!\n")
        else:
            print("Στην ενότητα '", units[index], "' τα απάντησες όλα σωστά. Μπράβο\n")
        time.sleep(1)
        index += 1

#Load questions - Φορτώνει τις ερωτήσεις της ορισθείσας θεματικής ενότητας και τις επιστρέφει σε μορφή λίστας
def load_q(filename):
    lines = []
    file = open(filename, "r")
    temp_lines = file.readlines()
    for line in temp_lines:
        lines.append(line[:-1])
    return lines

#Load answers - Φορτώνει τις απαντήσεις της ορισθείσας θεματικής ενότητας και τις επιστρέφει σε μορφή λίστας
def load_a(filename):
    lines = []
    file = open(filename, "r")
    temp_lines = file.readlines()
    for x in range(0, len(temp_lines), 4):
        lines.append([temp_lines[x][:-1] + "\n" + temp_lines[x+1][:-1] + "\n" + temp_lines[x+2][:-1] + "\n" + temp_lines[x+3][:-1], 
        temp_lines[x][-2] + temp_lines[x+1][-2] + temp_lines[x+2][-2] + temp_lines[x+3][-2]])
    return lines

#Shuffle questions - Ανακατεύει ερωτήσεις και απαντήσεις με τον ίδιο τρόπο, ώστε να μην χαθεί η αντιστοιχία των indexes
def shuffle(q1, a1, q2, a2, q3, a3):
    temp = list(zip(q1, a1, q2, a2, q3, a3))
    random.shuffle(temp)
    return temp

#Μain program - 
def main():
    asfaleia_q = load_q("q&a/asfaleia_q.txt")
    asfaleia_a = load_a("q&a/asfaleia_a.txt")
    personal_q = load_q("q&a/personal_q.txt")
    personal_a = load_a("q&a/personal_a.txt")
    strangers_q = load_q("q&a/strangers_q.txt")
    strangers_a = load_a("q&a/strangers_a.txt")
    temp = shuffle(asfaleia_q, asfaleia_a, personal_q, personal_a, strangers_q, strangers_a)
    asfaleia_q, asfaleia_a, personal_q, personal_a, strangers_q, strangers_a = zip(*temp)
    evaluation = []
    name = intro()
    score = examination(asfaleia_q, asfaleia_a)
    evaluation.append(score)
    score = examination(personal_q, personal_a)
    evaluation.append(score)
    score = examination(strangers_q, strangers_a)
    evaluation.append(score)
    eval(evaluation, name)
    unit_eval(evaluation)
    

if __name__ =='__main__':
    main()