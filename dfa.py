class DFA:

    def __init__(self, dfa: [str]) -> None:
        '''Creates this DFA as described in dfa.

        Parameters:
        - self: obligatory reference to this object
        - dfa: description of the desired DFA

        Return: 
        None
        '''
        self.dfa = dfa
        self.states = dfa[0].split()
        self.inputs = dfa[1].split()
        self.initial_state = dfa[2]
        self.accepting_state = dfa[3].split()
        transition_listie = dfa[4:len(dfa)]

        trans_parsed = []
        for i in range(len(transition_listie)):
            trans_parsed.append(transition_listie[i].split())

        a = []
        b = []
        c = []
        for i in range(len(trans_parsed)):
            a.append(trans_parsed[i][0])
            b.append(trans_parsed[i][1])
            c.append(trans_parsed[i][2])

        self.dictionary = {}
        for i in range(len(a)):
            self.dictionary[(a[i], b[i])] = c[i]

    def accepts(self, w: str) -> bool:
        '''Returns the acceptance status of w.

        Parameters:
        - self: obligatory reference to this object
        - w: the string to check

        Return:
        True if this DFA accepts w, False otherwise.
        '''
        current_state = self.initial_state
        for i in w:
            self.dictionary[(current_state, i)]
            current_state = self.dictionary[(current_state, i)]
        return current_state in self.accepting_state
