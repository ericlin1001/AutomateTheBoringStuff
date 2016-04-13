import os, random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',      'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',      'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',      'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':          'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':              'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def genQ(a):
    qu = [];
    if a[2] == 0:
        qu.append("Which is the capital of " + a[0] + "?");
    else:
        qu.append("Whose capital is " + a[1] + "?");
    x = list(range(4));
    random.shuffle(x);
    Option = ['A', 'B', 'C', 'D'];
    for i in range(len(x)):
        qu.append(Option[i] + ". " + a[3][x[i]]);
    an = Option[x.index(0)];
    return '\n'.join(qu), an;

def saveFile(file, str):
    f = open(file, 'w');
    f.write(str);
    print(str);
    
    f.close();
def genQuiz(no):
    x = list(range(len(capitals)));
    #q = [];
    random.shuffle(x);
    k = list(capitals.keys());
    questions = [];
    answers = [];
    qno = 1;
    for i in x:
        state = k[i];
        cap = capitals[state];
        xx = list(range(len(capitals)));
        xx.remove(i);
        random.shuffle(xx);
        type = random.randint(0, 1)
        if type == 0:
            option = [cap, capitals[k[xx[0]]], capitals[k[xx[1]]], capitals[k[xx[2]]]];
        else:
            option = [state, k[xx[0]], k[xx[1]], k[xx[2]]];

        #q.append([state, cap,type,  option ]);
        q = [state, cap,type,  option ]
        qu, an = genQ(q);
        questions.append(str(qno) + ". " + qu);
        answers.append(str(qno) + ". "  + an);
        qno = qno + 1

    saveFile("Question" +str(no) + ".txt", '\n\n'.join(questions))
    saveFile("Answer" +str(no) + ".txt", '\n'.join(answers))
    
    
genQuiz(0)
