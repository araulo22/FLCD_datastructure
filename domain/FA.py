from typing import List, Dict, Tuple


class FiniteAutomata:
    states: List[str]
    alphabet: List[str]
    transitions: Dict[Tuple[str, str], List[str]]
    initial_state: str
    final_states: List[str]

    def __init__(self, states: List[str], alphabet: List[str], transitions: Dict[Tuple[str, str], List[str]],
                 initial_state: str, final_states: List[str]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    @staticmethod
    def read_file(file_name: str):
        states = []
        alphabet = []
        transitions = {}
        initial_state = None
        final_states = []

        with open(file_name, 'r') as file:
            for lineCounter, line in enumerate(file, start=1):
                line: str = line.strip()
                tokens = line.split(";")
                if tokens[0] == "states":
                    states = tokens[1:]
                elif tokens[0] == "alphabet":
                    alphabet = tokens[1:]
                elif tokens[0] == "transitions":
                    for transition in tokens[1:]:
                        transition_tokens = transition.split(",")
                        trans = (transition_tokens[0], transition_tokens[1])
                        if trans in transitions:
                            transitions[trans].append(transition_tokens[2])
                        else:
                            transitions[trans] = [transition_tokens[2]]
                elif tokens[0] == "initialState":
                    initial_state = tokens[1]
                elif tokens[0] == "finalState":
                    final_states = tokens[1:]
        return FiniteAutomata(states, alphabet, transitions, initial_state, final_states)

    def print_states(self):
        print("Set of states: ", self.states)

    def print_alphabet(self):
        print("FA alphabet: ", self.alphabet)

    def print_init_state(self):
        print("Initial state: ", self.initial_state)

    def print_final_state(self):
        print("Final states: ", self.final_states)

    def print_transitions(self):
        print("Transitions: ")
        for t in self.transitions.keys():
            print("D({0}, {1}) = {2}".format(t[0], t[1], self.transitions[t]))

    def check_sequence(self, sequence) -> bool:
        if not self.is_dfa():
            raise ArithmeticError("FiniteAutomaton is not a DFA")
        current_state = self.initial_state

        while sequence != "":
            transition_key = (current_state, sequence[0])

            if transition_key in self.transitions.keys():
                current_state = self.transitions[transition_key][0]
                sequence = sequence[1:]

            else:
                return False

        return current_state in self.final_states

    def is_dfa(self) -> bool:
        for k in self.transitions.keys():
            if len(self.transitions[k]) > 1:
                return False
        return True


automata = FiniteAutomata.read_file("test_fa.txt")
automata.print_states()
automata.print_alphabet()
automata.print_init_state()
automata.print_final_state()
automata.print_transitions()
print("aab", automata.check_sequence("aab"))
print("aba", automata.check_sequence("aba"))
print("ab", automata.check_sequence("ab"))