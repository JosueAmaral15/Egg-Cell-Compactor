    #-*- coding: utf-8 -*-

'''
Program name: Egg-Cell-Compactor
Author: Josué Amaral
Date: 

Function of the program:

Nós queremos que o programa realize operações que possam caracterizar aquilo que uma tabela verdade tem em comum.
Para que possamos realizar o procedimento, deve-se ter em mente os seguintes requisitos:

implementar a álgebra de Boole em formato binário que pode ser convertido para decimal. 
Neste caso, temos uma sequência de bits que caracterizam cada termo e cada variável seguindo a seguinte lógica: 
suponhamos que tenhamos os seguintes termos: A.B.D+B'.C'.D'. 
Primeiro devemos entender que uma variável é representada por dois bits, sendo 00 quando é inexistente, 01 (ou 10) quando é normal e 11 quando é negado. 
Para A.B.D temos então: 01010001, e para B'.C'.D' seria: 00111111. Perceba que mesmo a variável C do primeiro termo e a variável A do segundo termo, 
mesmo que inexistentes, são representados por 00. Juntando os números em binário, o resultado seria: 0101000100111111. Como a variável C do primeiro 
termo e a variável A do segundo termo são representados, podemos unir ou concatenar as duas expressões binárias sem problemas. Esse conceito pode ser 
utilizado para representar os bits de um arquivo computacional e também para realizar compactações recursivas dos arquivos do usuário. Quanto às compactações, 
utilizar o conceito do algoritmo Quine-McCluskey para transformação da saída de uma tabela verdade em álgebra booleana, usar algoritmos que transformam um arquivo 
em uma saída de uma tabela verdade e chamar o conceito de célula-ovo (ou egg-cell, em inglês). A compactação recursiva com vários arquivos pode obedecer a uma 
estrutura hierárquica de um grafo árvore binário, em que os arquivos são organizados como se fossem postos em uma lista ou em um vetor ordenado. 
Essas compactações com mais de um arquivo são bottom-up, enquanto que as descompactações são top-down, e tudo isso de maneira binária, ou seja, 
a cada nova compactação apenas dois arquivos do usuário ou dois arquivos compactados são fundidos ou unidos com a compactação por vez. 
O usuário poderá ver, por meio de um aplicativo, quais foram os arquivos compactados, E se ele escolher um único arquivo para ser descompactado, 
a estrutura hierárquica do grafo irá fazer uma busca binária para reduzir significativamente o número de descompactações de arquivos intermediários e
 realizar a descompactação do arquivo solicitado. Existem dois tipos de compactações recursivas: aquelas que fazem a compactação de um único arquivo para reduzir
 o seu tamanho e aquelas que fazem a compactação de vários arquivos compactados. Quanto mais compactações forem feitas, menor será o arquivo até o ponto de o seu 
 tamanho se tornar suficientemente menor e por isso não poder ser mais compactado. Se necessário, estudar sobre SHA-II. Para preços: 
 criar módulos independentes para empresas sem conexão com o banco de dados do sistema (R$ 2^24), aplicativos mobile conectados com o banco de dados 
 ($ 1,00 dólar por arquivo ou diretório) e programas para PC conectados com o banco de dados caso funcionar ($ 1,00 dólar por arquivo ou diretório);

Para o uso da função Quine-McCluskey:
  qm = QuineMcCluskey()
  ones = [0, 2, 3]
  dontcares = [4, 5, 6, 7]
  print(qm.simplify(ones, dontcares))

Isso retornará o seguinte conjunto:

set(['1--', '-1-', '--0'])
Observe que o bit menos significativo na saída está na posição mais à esquerda (uma posição 0 para a cadeia de caracteres). 
Se os bits são chamados ABC, então o resultado deve ser interpretado como:

C or B or (not A)

Vídeo no YouTube que explica o que seria Quine-McCluskey: https://www.youtube.com/watch?v=9Fmqk1Yhf64
Site responsável por explicar o módulo:https://p5r.uk/quine-mccluskey/index.html

  SQL_CREATE_NAME variable with the content: 'CREATE TABLE SRN (ID UNSIGNED INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL, search_record_number INTEGER NOT NULL)' in SQLite3
  is storing the search_record_number with other numbers, what is wrong.
  
  
  Implements: 
  
  [X] Resolve the problem above;
  [] Colocar ou destacar rotinas de compressão (e de descompressão) passo a passo com sys.output.printf;
  [] work with numbers and not with strings;
  [] Fix problem 'out of memory' because of big files size;
  [] Fix count and time left (put time in seconds and not in count);
  [] Put time left during compress;
  [] Comments all the algorithm;
  [] Save the data (without errors);
  [] Recover the data from the new file;
  ## First part completed
  [] Save the data from a directory;
  [] Recover the data from the new file to a directory;
  [] Make recursive compress;
  [] Make the user interface to the program;
  ## Second part completed

  
 
Function to see the result (in the terminal):
  
def see_result (con = None):
  from sqlite3 import connect
  if con:
    con.close ()
  con = connect ('tasks.EggCellCompactor')
  c = con.cursor ()
  c.execute ('select * from SRN')
  t = c.fetchall ()
  print ('{:b}'.format (int (t[0][1])))
  return int (t[0][1])
  


'''

from math import log, ceil
from os import path, remove
from sqlite3 import connect
from os import sys
from pathlib import Path
import time


DEBUG = False
ALLOW_PROMPT_MESSAGES = True
PRINT_LONG_TEXT = False
ONLY_TIME = True

class QuineMcCluskey:
    """The Quine McCluskey class.

    The QuineMcCluskey class minimises boolean functions using the Quine
    McCluskey algorithm.

    If the class was instantiiated with the use_xor set to True, then the
    resulting boolean function may contain XOR and XNOR operators.
    """
    __version__ = "0.2"



    def __init__(self, use_xor = False):
        """The class constructor.

        Kwargs:
            use_xor (bool): if True, try to use XOR and XNOR operations to give
            a more compact return.
        """
        self.use_xor = use_xor  # Whether or not to use XOR and XNOR operations.
        self.n_bits = 0         # number of bits (i.e. self.n_bits == len(ones[i]) for every i).



    def __num2str(self, i):
        """
        Convert an integer to its bit-representation in a string.

        Args:
            i (int): the number to convert.

        Returns:
            The binary string representation of the parameter i.
        """
        x = ['1' if i & (1 << k) else '0' for k in range(self.n_bits - 1, -1, -1)]
        return "".join(x)



    def simplify(self, ones, dc = []):
        """Simplify a list of terms.

        Args:
            ones (list of int): list of integers that describe when the output
            function is '1', e.g. [1, 2, 6, 8, 15].

        Kwargs:
            dc (list of int): list of numbers for which we don't care if they
            have one or zero in the output.

        Returns:
            see: simplify_los.

        Example:
            ones = [2, 6, 10, 14]
            dc = []

            This will produce the ouput: ['--10']
            This means x = b1 & ~b0, (bit1 AND NOT bit0)

        Example:
            ones = [1, 2, 5, 6, 9, 10, 13, 14]
            dc = []

            This will produce the ouput: ['--^^'].
            In other words, x = b1 ^ b0, (bit1 XOR bit0).
        """
        terms = ones + dc
        if len(terms) == 0:
            return None

        # Calculate the number of bits to use
        # Needed internally by __num2str()
        self.n_bits = int(ceil(log(max(terms) + 1, 2)))

        # Generate the sets of ones and dontcares
        ones = set(self.__num2str(i) for i in ones)
        dc = set(self.__num2str(i) for i in dc)

        return self.simplify_los(ones, dc)



    def simplify_los(self, ones, dc = []):
        """The simplification algorithm for a list of string-encoded inputs.

        Args:
            ones (list of str): list of strings that describe when the output
            function is '1', e.g. ['0001', '0010', '0110', '1000', '1111'].

        Kwargs:
            dc: (list of str)set of strings that define the don't care
            combinations.

        Returns:
            Returns a set of strings which represent the reduced minterms.  The
            length of the strings is equal to the number of bits in the input.
            Character 0 of the output string stands for the most significant
            bit, Character n - 1 (n is the number of bits) stands for the least
            significant bit.

            The following characters are allowed in the return string:
              '-' don't care: this bit can be either zero or one.
              '1' the bit must be one.
              '0' the bit must be zero.
              '^' all bits with the caret are XOR-ed together.
              '~' all bits with the tilde are XNOR-ed together.

        Example:
            ones = ['0010', '0110', '1010', '1110']
            dc = []

            This will produce the ouput: ['--10'].
            In other words, x = b1 & ~b0, (bit1 AND NOT bit0).

        Example:
            ones = ['0001', '0010', '0101', '0110', '1001', '1010' '1101', '1110']
            dc = []

            This will produce the ouput: ['--^^'].
            In other words, x = b1 ^ b0, (bit1 XOR bit0).
        """
        self.profile_cmp = 0    # number of comparisons (for profiling)
        self.profile_xor = 0    # number of comparisons (for profiling)
        self.profile_xnor = 0   # number of comparisons (for profiling)

        terms = ones | dc
        if len(terms) == 0:
            return None

        # Calculate the number of bits to use
        self.n_bits = max(len(i) for i in terms)
        if self.n_bits != min(len(i) for i in terms):
            return None

        # First step of Quine-McCluskey method.
        prime_implicants = self.__get_prime_implicants(terms)

        # Remove essential terms.
        essential_implicants = self.__get_essential_implicants(prime_implicants)
        # Insert here the Quine McCluskey step 2: prime implicant chart.
        # Insert here Petrick's Method.

        return essential_implicants



    def __reduce_simple_xor_terms(self, t1, t2):
        """Try to reduce two terms t1 and t2, by combining them as XOR terms.

        Args:
            t1 (str): a term.
            t2 (str): a term.

        Returns:
            The reduced term or None if the terms cannot be reduced.
        """
        difft10 = 0
        difft20 = 0
        ret = []
        for (t1c, t2c) in zip(t1, t2):
            if t1c == '^' or t2c == '^' or t1c == '~' or t2c == '~':
                return None
            elif t1c != t2c:
                ret.append('^')
                if t2c == '0':
                    difft10 += 1
                else:
                    difft20 += 1
            else:
                ret.append(t1c)
        if difft10 == 1 and difft20 == 1:
            return "".join(ret)
        return None



    def __reduce_simple_xnor_terms(self, t1, t2):
        """Try to reduce two terms t1 and t2, by combining them as XNOR terms.

        Args:
            t1 (str): a term.
            t2 (str): a term.

        Returns:
            The reduced term or None if the terms cannot be reduced.
        """
        difft10 = 0
        difft20 = 0
        ret = []
        for (t1c, t2c) in zip(t1, t2):
            if t1c == '^' or t2c == '^' or t1c == '~' or t2c == '~':
                return None
            elif t1c != t2c:
                ret.append('~')
                if t1c == '0':
                    difft10 += 1
                else:
                    difft20 += 1
            else:
                ret.append(t1c)
        if (difft10 == 2 and difft20 == 0) or (difft10 == 0 and difft20 == 2):
            return "".join(ret)
        return None



    def __get_prime_implicants(self, terms):
        """Simplify the set 'terms'.

        Args:
            terms (set of str): set of strings representing the minterms of
            ones and dontcares.

        Returns:
            A list of prime implicants. These are the minterms that cannot be
            reduced with step 1 of the Quine McCluskey method.

        This is the very first step in the Quine McCluskey algorithm. This
        generates all prime implicants, whether they are redundant or not.
        """

        # Sort and remove duplicates.
        n_groups = self.n_bits + 1
        marked = set()

        # Group terms into the list groups.
        # groups is a list of length n_groups.
        # Each element of groups is a set of terms with the same number
        # of ones.  In other words, each term contained in the set
        # groups[i] contains exactly i ones.
        groups = [set() for i in range(n_groups)]
        for t in terms:
            n_bits = t.count('1')
            groups[n_bits].add(t)
        if self.use_xor:
            # Add 'simple' XOR and XNOR terms to the set of terms.
            # Simple means the terms can be obtained by combining just two
            # bits.
            for gi, group in enumerate(groups):
                for t1 in group:
                    for t2 in group:
                        t12 = self.__reduce_simple_xor_terms(t1, t2)
                        if t12 != None:
                            terms.add(t12)
                    if gi < n_groups - 2:
                        for t2 in groups[gi + 2]:
                            t12 = self.__reduce_simple_xnor_terms(t1, t2)
                            if t12 != None:
                                terms.add(t12)

        done = False
        while not done:
            # Group terms into groups.
            # groups is a list of length n_groups.
            # Each element of groups is a set of terms with the same
            # number of ones.  In other words, each term contained in the
            # set groups[i] contains exactly i ones.
            groups = dict()
            for t in terms:
                n_ones = t.count('1')
                n_xor  = t.count('^')
                n_xnor = t.count('~')
                # The algorithm can not cope with mixed XORs and XNORs in
                # one expression.
                assert n_xor == 0 or n_xnor == 0

                key = (n_ones, n_xor, n_xnor)
                if key not in groups:
                    groups[key] = set()
                groups[key].add(t)

            terms = set()           # The set of new created terms
            used = set()            # The set of used terms

            # Find prime implicants
            for key in groups:
                key_next = (key[0]+1, key[1], key[2])
                if key_next in groups:
                    group_next = groups[key_next]
                    for t1 in groups[key]:
                        # Optimisation:
                        # The Quine-McCluskey algorithm compares t1 with
                        # each element of the next group. (Normal approach)
                        # But in reality it is faster to construct all
                        # possible permutations of t1 by adding a '1' in
                        # opportune positions and check if this new term is
                        # contained in the set groups[key_next].
                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_cmp += 1
                                t2 = t1[:i] + '1' + t1[i+1:]
                                if t2 in group_next:
                                    t12 = t1[:i] + '-' + t1[i+1:]
                                    used.add(t1)
                                    used.add(t2)
                                    terms.add(t12)

            # Find XOR combinations
            for key in [k for k in groups if k[1] > 0]:
                key_complement = (key[0] + 1, key[2], key[1])
                if key_complement in groups:
                    for t1 in groups[key]:
                        t1_complement = t1.replace('^', '~')
                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_xor += 1
                                t2 = t1_complement[:i] + '1' + t1_complement[i+1:]
                                if t2 in groups[key_complement]:
                                    t12 = t1[:i] + '^' + t1[i+1:]
                                    used.add(t1)
                                    terms.add(t12)
            # Find XNOR combinations
            for key in [k for k in groups if k[2] > 0]:
                key_complement = (key[0] + 1, key[2], key[1])
                if key_complement in groups:
                    for t1 in groups[key]:
                        t1_complement = t1.replace('~', '^')
                        for i, c1 in enumerate(t1):
                            if c1 == '0':
                                self.profile_xnor += 1
                                t2 = t1_complement[:i] + '1' + t1_complement[i+1:]
                                if t2 in groups[key_complement]:
                                    t12 = t1[:i] + '~' + t1[i+1:]
                                    used.add(t1)
                                    terms.add(t12)

            # Add the unused terms to the list of marked terms
            for g in list(groups.values()):
                marked |= g - used

            if len(used) == 0:
                done = True

        # Prepare the list of prime implicants
        pi = marked
        for g in list(groups.values()):
            pi |= g
        return pi



    def __get_essential_implicants(self, terms):
        """Simplify the set 'terms'.

        Args:
            terms (set of str): set of strings representing the minterms of
            ones and dontcares.

        Returns:
            A list of prime implicants. These are the minterms that cannot be
            reduced with step 1 of the Quine McCluskey method.

        This function is usually called after __get_prime_implicants and its
        objective is to remove non-essential minterms.

        In reality this function omits all terms that can be covered by at
        least one other term in the list.
        """

        # Create all permutations for each term in terms.
        perms = {}
        for t in terms:
            perms[t] = set(p for p in self.permutations(t))

        # Now group the remaining terms and see if any term can be covered
        # by a combination of terms.
        ei_range = set()
        ei = set()
        groups = dict()
        for t in terms:
            n = self.__get_term_rank(t, len(perms[t]))
            if n not in groups:
                groups[n] = set()
            groups[n].add(t)
        for t in sorted(list(groups.keys()), reverse=True):
            for g in groups[t]:
                if not perms[g] <= ei_range:
                    ei.add(g)
                    ei_range |= perms[g]
        return ei



    def __get_term_rank(self, term, term_range):
        """Calculate the "rank" of a term.

        Args:
            term (str): one single term in string format.

            term_range (int): the rank of the class of term.

        Returns:
            The "rank" of the term.
        
        The rank of a term is a positive number or zero.  If a term has all
        bits fixed '0's then its "rank" is 0. The more 'dontcares' and xor or
        xnor it contains, the higher its rank.

        A dontcare weights more than a xor, a xor weights more than a xnor, a
        xnor weights more than 1 and a 1 weights more than a 0.

        This means, the higher rank of a term, the more desireable it is to
        include this term in the final result.
        """
        n = 0
        for t in term:
            if t == "-":
                n += 8
            elif t == "^":
                n += 4
            elif t == "~":
                n += 2
            elif t == "1":
                n += 1
        return 4*term_range + n



    def permutations(self, value = ''):
        """Iterator to generate all possible values out of a string.

        Args:
            value (str): A string containing any of the above characters.

        Returns:
            The output strings contain only '0' and '1'.

        Example:
            from qm import QuineMcCluskey
            qm = QuineMcCluskey()
            for i in qm.permutations('1--^^'):
                print(i)

        The operation performed by this generator function can be seen as the
        inverse of binary minimisation methonds such as Karnaugh maps, Quine
        McCluskey or Espresso.  It takes as input a minterm and generates all
        possible maxterms from it.  Inputs and outputs are strings.

        Possible input characters:
            '0': the bit at this position will always be zero.
            '1': the bit at this position will always be one.
            '-': don't care: this bit can be zero or one.
            '^': all bits with the caret are XOR-ed together.
            '~': all bits with the tilde are XNOR-ed together.

        Algorithm description:
            This lovely piece of spaghetti code generates all possibe
            permutations of a given string describing logic operations.
            This could be achieved by recursively running through all
            possibilities, but a more linear approach has been preferred.
            The basic idea of this algorithm is to consider all bit
            positions from 0 upwards (direction = +1) until the last bit
            position. When the last bit position has been reached, then the
            generated string is yielded.  At this point the algorithm works
            its way backward (direction = -1) until it finds an operator
            like '-', '^' or '~'.  The bit at this position is then flipped
            (generally from '0' to '1') and the direction flag again
            inverted. This way the bit position pointer (i) runs forth and
            back several times until all possible permutations have been
            generated.
            When the position pointer reaches position -1, all possible
            combinations have been visited.
        """
        n_bits = len(value)
        n_xor = value.count('^') + value.count('~')
        xor_value = 0
        seen_xors = 0
        res = ['0' for i in range(n_bits)]
        i = 0
        direction = +1
        while i >= 0:
            # binary constant
            if value[i] == '0' or value[i] == '1':
                res[i] = value[i]
            # dontcare operator
            elif value[i] == '-':
                if direction == +1:
                    res[i] = '0'
                elif res[i] == '0':
                    res[i] = '1'
                    direction = +1
            # XOR operator
            elif value[i] == '^':
                seen_xors = seen_xors + direction
                if direction == +1:
                    if seen_xors == n_xor and xor_value == 0:
                        res[i] = '1'
                    else:
                        res[i] = '0'
                else:
                    if res[i] == '0' and seen_xors < n_xor - 1:
                        res[i] = '1'
                        direction = +1
                        seen_xors = seen_xors + 1
                if res[i] == '1':
                    xor_value = xor_value ^ 1
            # XNOR operator
            elif value[i] == '~':
                seen_xors = seen_xors + direction
                if direction == +1:
                    if seen_xors == n_xor and xor_value == 1:
                        res[i] = '1'
                    else:
                        res[i] = '0'
                else:
                    if res[i] == '0' and seen_xors < n_xor - 1:
                        res[i] = '1'
                        direction = +1
                        seen_xors = seen_xors + 1
                if res[i] == '1':
                    xor_value = xor_value ^ 1
            # unknown input
            else:
                res[i] = '#'

            i = i + direction
            if i == n_bits:
                direction = -1
                i = n_bits - 1
                yield "".join(res)

## User Data:
class EggCellCompactor:
  BYTE = 8
  DIR = 'DIR'
  EXT = '.ECC'
  FILE = 'FILE'
  POINT = '.'
  SLASH = '/'
  CONTRASLASH = '\\'
  SRN_DIVISION = 45
  #[0, exponent, intercalation, direction, first_num, ext, search_record_number]
  MESSAGE_NAME_ERROR = '\nThe file name is incorrect or don\'t exists.'
  MESSAGE_NAME_INPUT = '\nType the file name (or the directory name) for the compress: '
  MESSAGE_SUCCESSFULLY_CREATED = '\nThe file was successfully created.'
  MESSAGE_SUCCESSFULLY_RECOVERED = '\nThe data was successfully recovered.'
  MESSAGE_DATABASE_CREATING = "Creating data bank..."
  MESSAGE_DATABASE_CREATING_COMPLETED = "Database creation completed!"
  MESSAGE_DATABASE_REGISTER = "Recording data in the database..."
  MESSAGE_DATABASE_RECORD = "Full database record!"
  MESSAGE_EXTRACTING_BIG_NUMBER = "Extracting data from user files..."
  MESSAGE_EXTRACTING_DATA_COMPLETED = "User file data extraction completed!"
  MESSAGE_BIG_NUMBER_REVERT_FILE = "Creating new file..."
  MESSAGE_FILE_CREATION_COMPL = "File creation completed!"
  MESSAGE_COMPRESS_OPERATION = "Performing compression operation..."
  MESSAGE_COMPRESS_OPERATION_COMPL = "Compression operation completed!"
  MESSAGE_PREPARING_COMPRESS = "Initializing or preparing to compress files..."
  MESSAGE_COMPLETED_COMPRESS = "Compression operation completed successfully!"
  MESSAGE_READING_DATABANK = "Performing database read operation...!"
  MESSAGE_READING_COMPLETED = "Database read operation completed!"
  MESSAGE_DECOMPRESSION = "Performing file decompression operation..."
  MESSAGE_DECOMPRESSION_COMPLETED = "File decompression operation completed!"
  MESSAGE_PREPARING_DESCOMPRESSION = "Preparing to perform user file decompression..."
  MESSAGE_DECOMPRESSION_FINISH = "User file decompression completed successfully!"
  MESSAGE_USER_MENU = '\n\nEGG CELL COMPACTOR\n\n\t1. Compact your file\n\t2. Descompact your file\n\t3. Quit\n\n\tChoice: '
  
  #SQL_CREATE_DATA_BANK = 'CREATE TABLE Data (LEVEL_ID INTEGER PRIMARY KEY AUTOINCREMENT, package_number UNSIGNED INTEGER NOT NULL, pos_miniterm_pack UNSIGNED INTEGER NOT NULL, miniterm TEXT NOT NULL)'
  SQL_CREATE_DATA_BANK = 'CREATE TABLE Data (LEVEL_ID INTEGER PRIMARY KEY AUTOINCREMENT, miniterm INTEGER NOT NULL)'
  SQL_CREATE_NAME = 'CREATE TABLE DataComplement (name VARCHAR(255), first_number UNSIGNED SMALLINT, filesize_bits INTEGER NOT NULL)'
  #SQL_INSERT_DATA = 'INSERT INTO Data (package_number, pos_miniterm_pack, miniterm) VALUES (?,?,?)'
  SQL_INSERT_DATA = 'INSERT INTO Data (miniterm) VALUES ({0})'
  SQL_INSERT_NAME = 'INSERT INTO DataComplement VALUES (?,?,?)'
  SQL_READ_DATABANK = "SELECT * FROM Data"
  SQL_READ_COMPLEMENT = "SELECT * FROM DataComplement"
  
  TIME_LEFT = 'Bit set: {0}/{4}, percentage: {1}%, time left: {2} minutes e {3} seconds'
  TIME_LEFT_ALTERNATIVE = '(with time_delay) Bit set: {0}/{4}, percentage: {1}%, time left: {2} minutes e {3} seconds'  
  ZERO = '0'
  MAX_SIZE = sys.maxsize

  ## Getting the user data.
  @classmethod
  def user_data (cls, is_compress):
    accepted = False
    ## Take the name file or the directory file.
    while not accepted:
      name = input (cls.MESSAGE_NAME_INPUT if is_compress else cls.MESSAGE_NAME_INPUT.replace('compress', 'unzip'))
      ##Verify if the file or directory exists.
      type_name = ''
      if path.exists (name) or not name:
        accepted = True
      else:
        if ALLOW_PROMPT_MESSAGES:
          print (cls.MESSAGE_NAME_ERROR)
    return name
  
  
  @staticmethod
  def convert_miniterms_to_numbers (miniterm):
    ##Example of input: '-1100--01-111' or '-0-1-1-100111'
    string = '1'
    for i in miniterm:
      if i == '1':
        string+= '11'
      elif i == '0':
        string+= '00'
      elif i == '-':
        string += '01'
    return int (string, 2)
  
  @staticmethod
  def convert_numbers_to_miniterms (miniterm_number):
    miniterm_number = '{:b}'.format(miniterm_number)[1:]
    string = ''
    for i,j in zip(miniterm_number[:-1:2],miniterm_number[1::2]):
      if i+j == '11':
        string+= '1'
      if i+j == '00':
        string+= '0'
      if i+j == '01':
        string+= '-'
      print (i+j, type(i+j))
    return string
  
  ## Starting the data bank (creating a table).
  @classmethod
  def create_data_bank (cls, path_name):
    
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DATABASE_CREATING)
      
    if path.exists (path_name):
      remove (path_name)
    con = connect (path_name)
    cursor = con.cursor ()
    cursor.execute (cls.SQL_CREATE_DATA_BANK)
    cursor.execute (cls.SQL_CREATE_NAME)
      
    con.commit ()

    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DATABASE_CREATING_COMPLETED)
    return con
  
  @classmethod
  def register_data_bank (cls, data, con):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DATABASE_REGISTER)
    cursor = con.cursor ()
    cursor.executemany (cls.SQL_INSERT_NAME, [(data[1], data[2], data[3])])
#    for i in range (len (data[0])):
#      for j in range(len(data[0][i]))
#        cursor.executemany (cls.SQL_INSERT_DATA, [data[0][i][j]])
    count_i = 0
    count_j = 0
    len_package = len (data[0])
    
    while count_i < len_package:
      len_miniterms = len(data[0][count_i])
      while count_j < len_miniterms:
        if DEBUG:
          if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
            print (type(list(data[0][count_i])[count_j]))
            print (type(list(data[0][count_i])),list(data[0][count_i]))
            print (type(list(data[0])))
            print (list(data[0][count_i])[count_j])
        cursor.execute (cls.SQL_INSERT_DATA.format(cls.convert_miniterms_to_numbers(list(data[0][count_i])[count_j])))
        #cursor.executemany (cls.SQL_INSERT_DATA, [(count_i, count_j, list(data[0][count_i])[count_j])])
        #cursor.executemany (cls.SQL_INSERT_DATA, [count_i* len_miniterms +count_j+1, count_i, count_j, list(data[0][count_i])[count_j]])
        count_j+=1
      count_i+=1
    con.commit ()
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DATABASE_RECORD)
    
  ## Changing the file name (with details, without errors).
  @classmethod
  def change_name (cls, filename, ext):
    if 1+filename.find(cls.SLASH) or 1+filename.find(cls.CONTRASLASH):
      if 1+filename.find(cls.SLASH):
        pos_slash = len (filename) -filename[::-1].find (cls.SLASH) ## Position of the file name.
      else:
        pos_slash = len (filename) -filename[::-1].find (cls.CONTRASLASH) ## Position of the file name.
      filename_modified = filename[pos_slash:] ## Extraction of the file name.
      #current_ext = ''
      if 1 +filename_modified.find (cls.POINT):
        pos = len (filename_modified) -filename_modified[::-1].find (cls.POINT) -1 ## Position for change the new file extension.
        #current_ext = filename_modified[pos:]
      else:
        pos = len (filename_modified)
      filename_modified = filename_modified[:pos] + ext ## Full extraction of the file name and include the new extension.
      path_name = filename[:pos_slash -1] ## Extraction of the path.
      fullname = path.join (path_name, filename_modified)
    else:
      #current_ext = ''
      if 1 +filename.find (cls.POINT):
        pos = len (filename) -filename[::-1].find (cls.POINT) -1 ## Position for change the new file extension.
        #current_ext = filename[pos:]
      else:
        pos = len (filename)
      fullname = filename[:pos] + ext ## Full extraction of the file name and include the new extension.
      
    return fullname#, current_ext
      
  ## Find the number resulted from the user file content.
  @classmethod  
  def big_number (cls, filename):
    ## Open and read the user file.
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_EXTRACTING_BIG_NUMBER)
    with open (filename, "rb") as f:
      content = f.read ()
    ## Transform the file in a binary number and after in a decimal number.
    s = str ()
    n = 0
    first = True
    for i in content:
      if first:
        if DEBUG:
          if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
            print ("TEST: ", i)
        n = i
        first = False
      s += cls.ZERO*(cls.BYTE -len ('{:b}'.format (i)))+ '{:b}'.format (i) 
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_EXTRACTING_DATA_COMPLETED)
    return int (s, 2), n

  ## Transform the big number in a file content again.
  @classmethod  
  def revert_big_number (cls, big_number, filename, first_number):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_BIG_NUMBER_REVERT_FILE)
    first_number_str = '{:b}'.format (first_number)
    big_number_str = cls.ZERO*(cls.BYTE -len (first_number_str) -1 if cls.BYTE -len (first_number_str) -1 >= 0 else cls.BYTE -len (first_number_str)) +'{:b}'.format (big_number)
    string = str ()
    
    ## Open and write the new file.
    with open (filename, "w") as f:
      for i in range (0,len (big_number_str) +1 -cls.BYTE,8):
        f.write (chr (int (big_number_str[i :i +cls.BYTE -1], 2)))
        #n = int (big_number_str[i :i +cls.BYTE -1], 2)
        #f.write (n.to_bytes (2, 'big'))
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_FILE_CREATION_COMPL)

  @classmethod
  def boolean_algebra (cls,number):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_COMPRESS_OPERATION)
    #With the Quine-McCluskey function we don't need to worry about the elaboration and understanding of the algorithm, rather we can just
     #define which Boolean algebra we want using a specific module for this.
    qm = QuineMcCluskey()
    #First, we must perform an operation to determine the positions in which the number 1, the digit of a binary number, appears within the large decimal number 
    #(and which we must turn into binary).
    #We have to determine the limits for the inclusion of lists in order to avoid overflows.
    result_ones = list()
    #result_dontcares = list()
    number_str = '{:b}'.format(number) ## We store a determined sequence of bits for later analysis
    count_ones = number_str.count ('1') ## We count the number of ones in the binary sequence
    number_str_len = len (number_str) ## We determine the length of this sequence
    #if count_ones < cls.MAX_SIZE and number_str_len < cls.MAX_SIZE: ## If the current bit count is less than the system's tolerable amount (32-bit or 64-bit)
      ##We will normally do the search by the bits ones
      #ones = list (map (lambda a: a[0], list(filter (lambda x: x[1] == '1', list(enumerate(number_str))))))
      #result_ones.append(ones) ## We will store the location or position of these bits in a one-dimensional array
    #else: ##If the amount of bits exceeds the tolerable size to be accepted for creating lists, we will make a detour
    ## In this case we will divide the file into packages, and from these packages we will make different boolean functions.
    ## We will also reduce the sequence of bits of number_substr with each iteration with the for loop
      #ant_pos = 0
      #current_len = len(number_substr)
      #current_pos = current_len if current_len < cls.MAX_SIZE else cls.MAX_SIZE      
    number_substr = number_str ## As we are going to reduce the amount of bits that we put as a string, we need a variable to carry out this elimination process
    #for i in range(ceil (current_len  /cls.MAX_SIZE)):
    while number_substr: ## Here we will carry out the process of counting ones respecting the limits of list formation of the operating system to use the Quine-McCluskey function.
      ones = list (map (lambda a: a[0], list(filter (lambda x: x[1] == '1', list(enumerate(number_substr[:cls.MAX_SIZE]))))))
      result_ones.append(ones) ## We will store all the results and also do all the Boolean formula transformation operations separately.
      number_substr = number_substr[cls.MAX_SIZE:len(number_substr)] ## We will perform binary sequence reduction according to cls.MAX_SIZE
      #current_len = len (number_substr)
      #current_pos = current_len if current_len < cls.MAX_SIZE else cls.MAX_SIZE
    
    ## Now we need to know how many bits are dontcares. We will calculate the complement to determine what those bits would be.
    complement = 2**(ceil(log (number_str_len, 2))) ## We will use the size of the bit stream to calculate the amount of doncares for this purpose. Thus, the difference between the largest exponential number in base 2 will be the limit, and the size of the bit stream will be put at the beginning of the dontcares bit stream.
    final_num = number_str_len % (cls.MAX_SIZE+1) ## Here we will filter all values above cls.MAX_SIZE, which would be the maximum limit for creating lists in Python according to the bit width of the hardware word or instruction.
     ## Since the bitlist is in packets, each intermediate packet is complete and need not count dontcares, but the last packet, as well as a single bitstream packet, can have dontcares bits.
    dontcares = list(range(final_num, complement if complement -1 <= cls.MAX_SIZE else cls.MAX_SIZE+1)) ## Here we will create a list with all the dontcares bits
    #result_dontcares.append(dontcares)
    result = [qm.simplify(i, [] if result_ones.index(i) +1 != len(result_ones) else dontcares) for i in result_ones[:-1 if len(result_ones) > 1 else 1]] ## We will return the result of simplifying the bitstream with all boolean functions in a list.
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_COMPRESS_OPERATION_COMPL)
      
    return result 
  
  ## Compact the file or the directory (main function).
  @classmethod
  def compact_file (cls, data):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_PREPARING_COMPRESS)
    filesize = Path(data).stat().st_size * 8
    filename = cls.change_name (data, cls.EXT)
    if DEBUG:
      if ALLOW_PROMPT_MESSAGES:
        print (filename)
    con = cls.create_data_bank (filename) ## Starting the data bank.
    
    if path.isfile (data):
      number, first_number = cls.big_number (data) ## Transform the file in a big number.
      if DEBUG and PRINT_LONG_TEXT:
        if ALLOW_PROMPT_MESSAGES:
          print(number)
      #cls.revert_big_number (number,data[0], '.2txt', first_num)
      ## The binary sequence must be simplified with the Quine-McCluskey algorithm.
      boolean_functions = cls.boolean_algebra (number)
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
          print (boolean_functions[0])
      ## Register all the changes in a data bank.
      cls.register_data_bank ([boolean_functions, data, first_number, filesize], con)
      if ALLOW_PROMPT_MESSAGES:
        print (cls.MESSAGE_SUCCESSFULLY_CREATED)
      con.close()
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_COMPLETED_COMPRESS)
  
  @staticmethod
  def read_data_bank (con):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_READING_DATABANK)
    cursor = con.cursor ()
    cursor.execute(cls.SQL_READ_DATABANK)
    boolean_functions = cursor.fetchall()
    cursor.execute(cls.SQL_READ_COMPLEMENT)
    datacompl = cursor.fetchall()
    filename = datacompl[0][0]
    first_number = datacompl[0][1]
    filesize = datacompl[0][2]
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_READING_COMPLETED)
    return boolean_functions, first_number, filename, filesize
  
  @staticmethod
  def define_letters_for_integers (n):
    ## We want to turn numbers into strings, and the goal is that we can have variables instead of numbers.
    ## As the numbers will become variables, we have to have a bijective function, that is, in which each number corresponds to a string.
    ## For example:
    ##
    ##    0 : A;
    ##    1 : B;
    ##    9 : J;
    ##    25 : Z;
    ##    26 : AA;
    ##    27 : AB;
    ##    
    ## And so on.
    try:
      n = int (n) ## The number must be an unsigned integer.
      next_value = ceil((n+1)/26) ## We will divide the number until we have all the data.
      current = n % 26 ## This is the first letter of our string.
      string = chr(65 +current) ## Assigning the first letter to the string variable.
      n = next_value ## n variable gets value next_value
      count = 0
      while n > 1: ## Until n variable gets a value equal to or less than one, we will continue processing.
        next_value = ceil((n+1)/26)
        current = (n-2) % 26 ## The next letter will be unraveled
        string = chr(65 +current) + string
        n = next_value
        count+=1
      return string
    except:
      return ''
  
  @classmethod
  def output_truth_table (cls, boolean_functions, filesize):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DECOMPRESSION)
    ## O objetivo com esta função é conseguir a saída de uma tabela verdade.
    ## Dentro de cada variável do vetor ou da lista boolean_functions existem tuplas cujos valores são:
    ## LEVEL_ID, package_number, pos_miniterm_pack, miniterm
    ## Exemplo de entrada:
    ## [(1, 0, 0, '-1100--01-111'), (2, 0, 1, '-0-1-1-100111'), (3, 0, 2, '-110101010-0-'), (4, 0, 3, '-1010-000000-'), (5, 0, 4, '-0001111100-0')]
 
    first_time = True
    mini_lenght = 0
    miniterm_compiled = '('
    current_var = ''
    #total_amount_variables = 0  
    if ALLOW_PROMPT_MESSAGES:
      time_delay = 0
      differs = False
      time_left = 0
      time_left2 = 0
      previous_percentage = 0
      start_timestamp = time.time()
      current_timestamp = time.time()
      previous_timestamp = time.time()
      previous_second = 0
      previous_differ_timestamp = 0
      start = time.perf_counter()
    
    if DEBUG:
      if ALLOW_PROMPT_MESSAGES:
        if PRINT_LONG_TEXT:
          print("raw boolean function: ", boolean_functions)
    for i in boolean_functions:
      ## Primeiro devemos recolher cada um dos minitermos e substituir cada caractere pela sua devida variável.
      miniterm_q = cls.convert_numbers_to_miniterms(i[1])
      if first_time:
        mini_lenght = len(miniterm_q)
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES:
          print("miniterm_q: ", miniterm_q)  
      count = 0
      var_used = list()
      for j in miniterm_q:
        current_var = cls.define_letters_for_integers(mini_lenght -count -1)
        if DEBUG:
          if ALLOW_PROMPT_MESSAGES:
            print ("current_var: ", current_var, "count: ", count)
        if j == '1':
          if DEBUG:
            if ALLOW_PROMPT_MESSAGES:
              print ("current_var ", current_var, "entered by 1")
          miniterm_compiled += '{0} and '.format(current_var)
          var_used.append(current_var)
        elif j == '0':
          if DEBUG:
              if ALLOW_PROMPT_MESSAGES:
                print ("current_var ", current_var, "entered by 0")
          miniterm_compiled += '({0} -1)*(-1) and '.format(current_var)
          var_used.append(current_var)
        #elif j == '-': 
        #continue
        count+=1
        #total_amount_variables +=1
      miniterm_compiled = miniterm_compiled[:-5]+') or ('
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
          print ("miniterm_compiled", miniterm_compiled)
    miniterm_compiled = miniterm_compiled[:-5]
    
    if DEBUG:
      if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
        print ("miniterm_compiled completed: ", miniterm_compiled)
    ## Agora utilizaremos todas as variáveis para realizar a operação binária de uma tabela verdade a fim de extrair a saída:
    count = 0
    count2 = 0
    SE = lambda x: (1/0.02)*(abs(x+1)-abs(x+0.99)+0.01)
    big_number_result = ''
    while count < filesize:
      boolean_algebra = miniterm_compiled
      bin_num = count
      while count2 < mini_lenght:
        current_var = cls.define_letters_for_integers(mini_lenght -count2 -1)
        current_bit = round(SE(bin_num-2**(mini_lenght-count2 -1)))
        boolean_algebra = boolean_algebra.replace(current_var, str(current_bit))
        if DEBUG and not ONLY_TIME:
          if ALLOW_PROMPT_MESSAGES:
            print ("filesize: ", filesize, "mini_lenght: ", mini_lenght, ", count2: ",count2, ", mini_lenght -count2: ", mini_lenght -count2, ", 2**(mini_lenght-count2): ", 2**(mini_lenght-count2))
            print ("current_var : ", current_var, ", current_bit (round(SE(bin_num-2**(mini_lenght-count2))): ", current_bit, ", bin_num (count): ", bin_num)
            if PRINT_LONG_TEXT:
              print("boolean_algebra replacing: ",boolean_algebra)
        if current_bit:
          bin_num-= 2**(mini_lenght-count2-1)
        count2+=1
      if DEBUG and not ONLY_TIME:
        if ALLOW_PROMPT_MESSAGES:
          if PRINT_LONG_TEXT:
            print("boolean_algebra completed: ",boolean_algebra)
      result = eval(boolean_algebra)
      if DEBUG and not ONLY_TIME:
        if ALLOW_PROMPT_MESSAGES:
          print ("TEST result:", result)
      big_number_result += str(result) 
      count2 = 0
      count+=1
      
      #if DEBUG:
      if ALLOW_PROMPT_MESSAGES:
        #time_delay+=1
        current_percentage = 100*count/filesize
        current_timestamp = time.time()
        current_second = int(current_timestamp -start_timestamp)
        if current_second != previous_second:
          previous_second = current_second
          timestamp_differ = current_timestamp - previous_timestamp
          timestamp_differ_result = (timestamp_differ+previous_differ_timestamp)/2
          time_left = (timestamp_differ_result) * (100 -current_percentage)
          previous_differ_timestamp = timestamp_differ
          previous_timestamp = current_timestamp
          if DEBUG:
            if ALLOW_PROMPT_MESSAGES:
              print ("ENTER current_second != previous_second:", current_second != previous_second)
        if DEBUG:
          print ( "time_left: ", time_left, "current_timestamp: ", current_timestamp, "start_timestamp: ",start_timestamp, "current_second: ", current_second, "previous_second: ", previous_second, "current_second != previous_second: ", current_second != previous_second)
        print (cls.TIME_LEFT.format(count, int(current_percentage), int(time_left//60), int(time_left % 60), filesize))
        
        
       ## With time_delay
      if ALLOW_PROMPT_MESSAGES:
        time_delay+=1
        current_percentage2 = int(current_percentage)
        if current_percentage2 != previous_percentage:
          time_left2 = ((time_delay //10) * (100 -current_percentage2))/2  
        print (cls.TIME_LEFT_ALTERNATIVE.format(count, int(current_percentage2), int(time_left2//60), int(time_left2 % 60), filesize))
        if current_percentage2 != previous_percentage:
          time_delay = 0
          previous_percentage = current_percentage2
          
    if DEBUG and ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
        print ('big_number_result',big_number_result)
        
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DECOMPRESSION_COMPLETED)
    return int(big_number_result, 2)
    
    
  ## descompact the file or the directory (main function).
  @classmethod
  def descompact_file (cls, data):
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_PREPARING_DESCOMPRESSION)
    if path.isfile (data): ## If the user input is a file and not a folder.
      con = connect (data) ## Starting the data bank.
      boolean_functions, first_number, filename, filesize = cls.read_data_bank (con) ## Read all the components of the data bank.
      number = cls.output_truth_table (boolean_functions, filesize) ## Recover the big number from boolean functions. 
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
          print (boolean_functions[0])
      ## Register all the changes in a data bank.
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES:
          print("TEST: filename: ",filename)
          if PRINT_LONG_TEXT:
            print ("big number", number)
      cls.revert_big_number(number, filename, first_number)
      if ALLOW_PROMPT_MESSAGES:
        print (cls.MESSAGE_SUCCESSFULLY_RECOVERED)
      con.close()
    if ALLOW_PROMPT_MESSAGES:
      print(cls.MESSAGE_DECOMPRESSION_FINISH)

## Main program
data = True
choice = 1
while data and choice != '3':
  choice = input(cls.MESSAGE_USER_MENU)
  if choice == '1':
    data = EggCellCompactor.user_data (True)
    EggCellCompactor.compact_file (data)
  elif choice == '2':
    data = EggCellCompactor.user_data (False)
    EggCellCompactor.descompact_file (data)


