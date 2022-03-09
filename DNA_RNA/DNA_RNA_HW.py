#Создать классы Dna и Rna, объекты которых обладают следующими свойствами:

#    Могут быть инициализированы строкой, соответствующей последовательности ДНК/РНК
#    Позволяют определить долю GC нуклеотдиов в последовательности с помощью метода gc_content
#    Позволяют создать комплементарную последовательность с помощью метода reverse_complement
#    Позволяют итерироваться по последовательности
#    Объекты с одинаковыми последовательностями должны быть равны (так как про eq мы поговорить не успели еще, по собственному желанию)
#    Их можно добавлять в множества (так как про hash мы поговорить не успели еще, по собственному желанию)


#Объекты класса Dna дополнительно имеют метод transcribe позволяющий создавать объект класса Rna, соответствующий результату транскрипции последовательности.

#Весь код написать в отдельной ветке в своем репозитории и сделать PR в main, поставив меня/Катю в ревьюеры.



class NucleicAcid:
    def __init__(self, sequence):
        self.sequence = sequence

    def gc_content(self):
        seq = list(self.sequence.upper())

        g_nucleotides = seq.count('G')
        c_nucleotides = seq.count('C')

        total_nucleotides_number = len(self.sequence)

        gc_content =  ((g_nucleotides + c_nucleotides) / total_nucleotides_number) * 100

        return gc_content

    def __iter__(self):
        return NucleicAcidIterator(self)


    def __eq__(self, other):
        if not isinstance(other, NucleicAcid):
            return NotImplemented
        return self.sequence == other.sequence

    def __hash__(self):
        return hash(self.sequence)

class Rna(NucleicAcid):
    def reverse_complement(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        seq = self.sequence.upper()

        reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))

        return reverse_complement

class Dna(NucleicAcid):

    def reverse_complement(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        seq = self.sequence.upper()

        reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))

        return reverse_complement

    def transcribe(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C','T': 'A'}
        seq = self.sequence.upper()

        transcribe = "".join(complement.get(base, base) for base in seq)

        return Rna(transcribe)

class NucleicAcidIterator:
    def __init__(self, na):
        self._na = na
        self._index = 0

    def __next__(self):
        if self._index < len(self._na.sequence):
            result = self._na.sequence[self._index]
            self._index += 1
            return result

        raise StopIteration
