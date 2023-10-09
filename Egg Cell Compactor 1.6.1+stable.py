    #-*- coding: utf-8 -*-

'''
Program name: Egg-Cell-Compactor
Author: Josué Amaral
Date of creation: 05/12/22
Last update: 26/02/23

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
  [X] Colocar ou destacar rotinas de compressão (e de descompressão) passo a passo com sys.output.printf;
  [X] Resolver problema com aninhamento de parênteses;
  [X] Resolver problemas com o caractere '\r' (que não funciona atribuindo ao end do print);
  [X] Fragmentar o reduce;
  [X] Resolver problemas para realizar a transformação de strings para números com o conceito de árvores binárias (1,2,2,4,4,4,4,8,8,8,8,8,8,8,8,...);
  [X] Implementar timer para partes de compactação, incluindo durante o uso do método QuineMcCluskey;
  [X] Incluir constante CLI_MODE para evitar todo e qualquer tipo de impressão no terminal;
  [X] Colocar tamanho de caracteres da algebra booleana no início da descompactação;
  [X] Ajudar partes do código em que existem conversões das variáveis em algarismos binários e em números decimais. Incluir constantes NEGATE_BOOLEAN_VARIABLE_REPRESENTION, BOOLEAN_VARIABLE_REPRESENTION e BOOLEAN_VARIABLE_NOT_INCLUDED (convert_miniterms_to_numbers, line 804; convert_numbers_to_miniterms, line 817);
  [X] Transformar tabela do banco de dados em uma tabela sem chave primária e sem coluna com auto_increment;
  [X] Acrescentar 'calculing' para a classe TimeLeft;
  [X] substituir divisão por deslocamento e máscara;
  [X] Remover coluna de numeração da tabela principal do banco de dados; 
  [X] Tentar realizar operações com números (e não com strings) ao descompactar o arquivo. Realizar operações sobre os minitermos numéricos da tabela verdade;
  [X] work with numbers and not with strings (convert_miniterms_to_numbers, line 804; convert_numbers_to_miniterms, line 817; output_truth_table, line 1218);
  [X] Fix count and time left (put time in seconds and not in count);
  [X] Put time left during compress;
  [X] Resolver problemas com fórmula linha 1023 a fim de realizar recursividade;
  [X] Resolver problemas da função transform_content_revert;
  [X] Resolver problema com um byte a mais durante descompactação (pode ser a recursividade na função big_number (recursive = True), linha 1046). Tem a ver com o fato de não processar uma letra, de retornara junto duas letras antes da conversão (por exemplo, cd) e converter apenas uma só (por exemplo, c = 99);
  [X] Resolver problema referente à linha 1016 com recursividade e inserção maior de zeros com deslocamento (colocar True para argumento da função na linha 1055 a fim de analisar recursividade);
  [X] Colocar no algoritmo not cls.THREADS_AMMOUNT == 0 or cls.THREADS_AMMOUNT < cls.THREADS_MAX;
  [X] Incluir variável de ilimitação de espaço de armazenamento para não haver interrupções no processamento dos dados durante a recursividade, especialmente em relação à função da linha 1701;
  [] Resolver função da linha 1701 que demonstra ser falível com relação aos bits que são fornecidos:
  11111111011000010110001001100011011001000000101001100101011001100110011100001010
  11111111011000000110001001100010011001000000101001100100011001100010011100001010
                 ^               ^                       ^         ^              
                16              32                      56        66              
                                                                                  
  Provavelmente problema tem a ver com minitermos que não estão sendo utilizados pelo programa.
  
  [] Preparar função Quine-McCluskey para efetuar processamento massivo de informações.
    [] Substituir todas as estruturas de laço for para while;
    [] Remover as listas sempre quando possível;
    [] Converter operações com strings para operações com números ("1100" para 12);
  [] Colocar recursividade, colocar threads e passar funções para a GPU ao mesmo tempo em relação a algumas funções que demoram muito. Interagir com recursos da GPU, com threads e com recursividade. Para isso acontecer, DEBUG deve estar ativado e deve-se compreender a forma como os dados serão armazenados; Utilizar GPU e threads para realizar operações de maneira mais rápida tanto na compactação como na descompactação;
  [] Fazer com que o programa pergunte se pode utilizar a GPU, os threads e a recursividade a depender do sistema (e de qual dispositivo e módulos estão disponíveis), e verifica quanto de memória principal tem para utilizar 80% do espaço de armazenamento disponível no máximo;
  [] Fazer observações com arquivos binários. Criar e compilar um algoritmo que tem a função de mostrar na tela a mensagem hello world a fim de utilizá-lo como stub para o software Egg Cell compactor;
  [] Save the data (without errors from binary file);
  [] Recover the data from the new file (binary file);
  [] Fix problem 'out of memory' because of big files size;
  [] Transformar EEG em linha de comando com argumentos para definir se quer recursividade, se quer uso otimizado, se quer que haja impressão na tela, etc, como se fosse um comando no terminal
  [] Comments all the algorithm;
  ## First part completed
  [] Save the data from a directory;
  [] Recover the data from the new file to a directory;
  [] Make recursive compress;
  [] Make the user interface to the program;
  [] Make the program automatically install modules that are not installed;
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
from psutil import virtual_memory
from math import log, ceil
from os import path, remove
from sqlite3 import connect
from os import sys
from pathlib import Path
import time
from functools import reduce
from numba import njit

CLI_MODE = True
ALLOW_PROMPT_MESSAGES = True
ENABLE_TIME_LEFT_APPEAR = True
DEBUG = False
PRINT_LONG_TEXT = False

def filter_log (num, b):
  if num > 0:
    return int (log (num, b))
  else:
    return 1

class TimeLeft:
  def __init__ (self, description, total_bool, show_time_left):
    self.TIME_LEFT = '{5}: {0}/{4}, percentage: {1}%, time left: {2} minutes and {3} seconds.' if show_time_left else '{2}: Occurrence time: {0} minutes and {1} seconds.'
    self.TIME_LEFT_FIRST = '{5}: {0}/{4}, percentage: {1}%, time left: calculing...' if show_time_left else '{2}: Occurrence time: {0} minutes and {1} seconds.'
    self.time_left = 0
    self.previous_percentage = 0
    self.start_timestamp = time.time()
    self.current_timestamp = time.time()
    self.previous_timestamp = time.time()
    self.previous_second = 0
    self.timestamp_differ = 0
    self.count_bool = 0
    self.total_bool = total_bool
    self.timestamp_differ_result = int(filter_log(filter_log(self.total_bool,2),2)) #int(log(log(total_bool)))
    #self.resist = lambda x, a: (2*x+a+1)/(2*x+2*a+1)
    self.description = description
    self.show_time_left = show_time_left
  
  def count_time_and_print (self):
    if self.show_time_left:
      current_percentage = int(100*self.count_bool/self.total_bool)
      current_percentage_float = 100*self.count_bool/self.total_bool
      current_timestamp = time.time()
      current_second = int(current_timestamp -self.start_timestamp)
      
      if current_second != self.previous_second:
        self.previous_second = current_second
        self.timestamp_differ_result = (self.timestamp_differ_result + self.timestamp_differ)/2
        #self.timestamp_differ_result = ((self.timestamp_differ_result + self.timestamp_differ)/2)*(1 -self.resist(self.count_bool, self.total_bool)) + self.timestamp_differ_result*self.resist(self.count_bool, self.total_bool)
        self.time_left = int((self.timestamp_differ_result) * (100 -current_percentage_float))

      if current_percentage != self.previous_percentage:
        self.timestamp_differ = current_timestamp - self.previous_timestamp
        self.previous_timestamp = current_timestamp
        self.previous_percentage = current_percentage
      
      if current_percentage > 0:
        print (self.TIME_LEFT.format(self.count_bool, int(current_percentage), int(self.time_left//60), int(self.time_left % 60), self.total_bool, self.description), end = '\r')
      else:
        print (self.TIME_LEFT_FIRST.format(self.count_bool, int(current_percentage), int(self.time_left//60), int(self.time_left % 60), self.total_bool, self.description), end = '\r')
      self.count_bool+=1
      
    else:
      current_timestamp = time.time()
      current_second = int(current_timestamp -self.start_timestamp)
      print (self.TIME_LEFT.format(int(self.time_left//60), int(self.time_left % 60), self.description), end = '\r')


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
        self.TIME_LEFT_QUINE_MCCLUSKEY = dict()
        self.TIME_LEFT_QUINE_MCCLUSKEY['GET_PRIME_IMPLICANTS'] = ['Processing first part of compaction [1/7]', 
   'Processing second part of compaction [2/7]', 
   'Processing thirt part of compaction [3/7]', 
   'Processing fourth part of compaction [4/7]', 
        
        ]
        self.TIME_LEFT_QUINE_MCCLUSKEY['GET_ESSENTIAL_IMPLICANTS'] = [
        'Processing fifth part of compaction [5/7]', 
        'Processing sixth part of compaction [6/7]', 
        'Processing seventh part of compaction [7/7]', 
        
        ]
        

    def __num2str(self, i):
        """
        Convert an integer to its bit-representation in a string.

        Args:
            i (int): the number to convert.

        Returns:
            The binary string representation of the parameter i.
        """
        #x = ['1' if i & (1 << k) else '0' for k in range(self.n_bits - 1, -1, -1)]
        x = ''
        count = self.n_bits - 1
        while count > -1:
            if i & (1 << count):
                x += '1'
            else:
                x += '0'
            count-=1
        return x



    def simplify(self, ones, dc = []):
      if ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print (EggCellCompactor.MESSAGE_QUINE_MCCLUSKEY)
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
        
        #self.n_bits = max(len(i) for i in terms)
        list_terms = list(terms)
        length_terms = len(list_terms)
        maximum = len(list_terms[0])
        count = 0
        while count < length_terms:
            if maximum < len(list_terms[count]):
                maximum = len(list_terms[count])
            count+=1
        
        self.n_bits = maximum
        
        #if self.n_bits != min(len(i) for i in terms):
            #return None
        
        minimum = len(list_terms[0])
        count = 0
        while count < length_terms:
          if minimum > len(list_terms[count]):
              minimum = len(list_terms[count])
          count+=1
        
        if self.n_bits != minimum:
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
        '''
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
        '''
        count = 0
        size = len(t1)
        while count < size:
          if t1[count] == '^' or t2[count] == '^' or t1[count] == '~' or t2[count] == '~':
              return None
          elif t1[count] != t2[count]:
              ret.append('^')
              if t2[count] == '0':
                  difft10 += 1
              else:
                  difft20 += 1
          else:
              ret.append(t1[count])
          count+=1
          
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
        '''
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
        '''
        
        count = 0
        size = len(t1)
        while count < size:
          if t1[count] == '^' or t2[count] == '^' or t1[count] == '~' or t2[count] == '~':
              return None
          elif t1[count] != t2[count]:
              ret.append('~')
              if t1[count] == '0':
                  difft10 += 1
              else:
                  difft20 += 1
          else:
              ret.append(t1[count])
          count+=1
          
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
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
            timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_PRIME_IMPLICANTS'][0], len(terms), True)
        #groups = [set() for i in range(n_groups)]
        groups = list()
        count = 0
        while count < n_groups:
            groups.append(set())
            count+=1
        '''
        for t in terms:
            n_bits = t.count('1')
            groups[n_bits].add(t)
            if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
              timing.count_time_and_print()
        '''
        
        for t in terms:
            n_bits = t.count('1')
            groups[n_bits].add(t)
            if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
                timing.count_time_and_print()
        if self.use_xor:
            # Add 'simple' XOR and XNOR terms to the set of terms.
            # Simple means the terms can be obtained by combining just two
            # bits.
            if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
                timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_PRIME_IMPLICANTS'][1], len(list(groups)), True)
            '''    
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
                if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
                  timing.count_time_and_print()
            '''
            count = 0
            size = len(groups)
            while count < size:
                group = groups[count]
                count1 = 0
                size1 = len(group)
                while count1 < size1:
                    t1 = group[count1]
                    count2 = 0
                    size2 = len(group)
                    while count2 < size2:
                        t2 = group[count2]
                        t12 = self.__reduce_simple_xor_terms(t1, t2)
                        if t12 != None:
                            terms.add(t12)
                        count2+=1
                    if count < n_groups - 2:
                        count3 = 0
                        group_element = groups[count +2]
                        size3 = len(group_element)
                        while count3 < size3:
                            t2 = group_element[count3]
                            t12 = self.__reduce_simple_xnor_terms(t1, t2)
                            if t12 != None:
                                terms.add(t12)
                            count3+=1
                    count1+=1
                if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
                    timing.count_time_and_print()
                count+=1
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
            timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_PRIME_IMPLICANTS'][2], 0, False)
        done = False
        while not done:
            # Group terms into groups.
            # groups is a list of length n_groups.
            # Each element of groups is a set of terms with the same
            # number of ones.  In other words, each term contained in the
            # set groups[i] contains exactly i ones.
            groups = dict()
            for t in terms:
                t = list_terms[count]
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
            
            #STOP HERE
            
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
            
            if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
              timing.count_time_and_print()

        # Prepare the list of prime implicants
        pi = marked
        
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
          timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_PRIME_IMPLICANTS'][3], len(list(groups.values())),True)
        for g in list(groups.values()):
            pi |= g
            if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
              timing.count_time_and_print()
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
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
            timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_ESSENTIAL_IMPLICANTS'][0], len(terms), True)
        # Create all permutations for each term in terms.
        perms = {}
        count = 0
        size = len(terms)
        while count < size:
            t = terms[count]
            perms[t] = set(p for p in self.permutations(t))
            count+=1

        # Now group the remaining terms and see if any term can be covered
        # by a combination of terms.
        ei_range = set()
        ei = set()
        groups = dict()
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
            timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_ESSENTIAL_IMPLICANTS'][1], len(terms), True)
        
        count = 0
        size = len(terms)
        while count < size:
            t = terms[count]
            n = self.__get_term_rank(t, len(perms[t]))
            if n not in groups:
                groups[n] = set()
            groups[n].add(t)
            count+=1
        
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
            timing = TimeLeft (self.TIME_LEFT_QUINE_MCCLUSKEY['GET_ESSENTIAL_IMPLICANTS'][2], len(sorted(list(groups.keys()), reverse=True)), True)
        count = 0
        sorted_group = sorted(list(groups.keys()), reverse=True)
        size = len (sorted_group)
        while count < size:
            t = sorted_group[count]
            count1 = 0
            group_element = groups[t]
            size1 = len(group_element)
            while count1 < size1:
                g = group_element[count1]
                if not perms[g] <= ei_range:
                    ei.add(g)
                    ei_range |= perms[g]
                count1+=1
            count+=1
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
        '''
        for t in term:
            if t == "-":
                n += 8
            elif t == "^":
                n += 4
            elif t == "~":
                n += 2
            elif t == "1":
                n += 1
        '''
        count = 0
        size = len(term)
        while count < size:
          t = term[count]
          if t == "-":
              n += 8
          elif t == "^":
              n += 4
          elif t == "~":
              n += 2
          elif t == "1":
              n += 1
          count+=1
                
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
  COMPRESS = 'compress'
  UNZIP = 'unzip'
  MASK = 255
  NEGATE_BOOLEAN_VARIABLE_REPRESENTION = 1
  BOOLEAN_VARIABLE_REPRESENTION = 3
  BOOLEAN_VARIABLE_NOT_INCLUDED = 0
  #[0, exponent, intercalation, direction, first_num, ext, search_record_number]
  MESSAGE_NAME_ERROR = '\nThe file name is incorrect or don\'t exists.'
  MESSAGE_NAME_INPUT = '\nType the file name (or the directory name) for the compress: '
  MESSAGE_SUCCESSFULLY_CREATED = 'The file was successfully created.'
  MESSAGE_SUCCESSFULLY_RECOVERED = 'The data was successfully recovered.'
  MESSAGE_DATABASE_CREATING = "Creating data bank..."
  MESSAGE_DATABASE_CREATING_COMPLETED = "Database creation completed!"
  MESSAGE_DATABASE_REGISTER = "Recording data in the database..."
  MESSAGE_DATABASE_RECORD = "Full database record!"
  MESSAGE_EXTRACTING_BIG_NUMBER = "Extracting data from user files..."
  MESSAGE_EXTRACTING_DATA_COMPLETED = "\nUser file data extraction completed!"
  MESSAGE_BIG_NUMBER_REVERT_FILE = "Creating new file..."
  MESSAGE_FILE_CREATION_COMPL = "File creation completed!"
  MESSAGE_COMPRESS_OPERATION = "Performing compression operation..."
  MESSAGE_COMPRESS_OPERATION_COMPL = "Compression operation completed!"
  MESSAGE_PREPARING_COMPRESS = "Initializing or preparing to compress files..."
  MESSAGE_COMPLETED_COMPRESS = "All compression operations completed successfully!"
  MESSAGE_READING_DATABANK = "Performing database read operation...!"
  MESSAGE_READING_COMPLETED = "Database read operation completed!"
  MESSAGE_DECOMPRESSION = "Performing file decompression operation..."
  MESSAGE_DECOMPRESSION_COMPLETED = "\nFile decompression operation completed!"
  MESSAGE_PREPARING_DESCOMPRESSION = "Preparing to perform user file decompression..."
  MESSAGE_DECOMPRESSION_FINISH = "User file decompression completed successfully!"
  MESSAGE_USER_MENU = '\n\nEGG CELL COMPACTOR\n\n\t1. Compact your file\n\t2. Descompact your file\n\t3. Quit\n\n\tChoice: '
  MESSAGE_QUINE_MCCLUSKEY = "\nProcessing file data..."
  MESSAGE_QUINE_MCCLUSKEY_COMPL = "\nFile data processing completed!"
  MESSAGE_SET_BOOLEAN_ALGEBRA = "Preparing boolean algebra..."
  MESSAGE_SET_BOOLEAN_ALGEBRA_COMPL = "\nComplete boolean algebra preparation!"
  #SQL_CREATE_DATA_BANK = 'CREATE TABLE Data (LEVEL_ID INTEGER PRIMARY KEY AUTOINCREMENT, package_number UNSIGNED INTEGER NOT NULL, pos_miniterm_pack UNSIGNED INTEGER NOT NULL, miniterm TEXT NOT NULL)'
  SQL_CREATE_DATA_BANK = 'CREATE TABLE Data (miniterm INTEGER NOT NULL)'
  SQL_CREATE_NAME = 'CREATE TABLE DataComplement (name VARCHAR(255), filesize_bits INTEGER NOT NULL, is_binary BIT NOT NULL)'
  #SQL_INSERT_DATA = 'INSERT INTO Data (package_number, pos_miniterm_pack, miniterm) VALUES (?,?,?)'
  SQL_INSERT_DATA = 'INSERT INTO Data (miniterm) VALUES ({0})'
  SQL_INSERT_NAME = 'INSERT INTO DataComplement VALUES (?,?,?)'
  SQL_READ_DATABANK = "SELECT * FROM Data"
  SQL_READ_COMPLEMENT = "SELECT * FROM DataComplement"
  
  TIME_LEFT = 'Bit set'
  TIME_LEFT_ASSEMBLY_BOOL_ALG = 'Preparing processing model'
  TIME_LEFT_REDUCE_BITS = 'Bit set for compact'
  TIME_LEFT_BIG_NUMBER = 'Converting data file'
  #TIME_LEFT_ALTERNATIVE = '(with time_delay) Bit set: {0}/{4}, percentage: {1}%, time left: {2} minutes e {3} seconds.'
  ZERO = '0'
  MAX_SIZE = sys.maxsize
  #MAX_FREE_MEMORY = virtual_memory()[1] -virtual_memory()[1]*0.8
  MAX_FREE_MEMORY = 0
  MAX_RECURSIVE = 0
  NUMBER_RECURSIVE_FUNCTIONS = 0
  
  SE = lambda x: (x/(2*0.01))*(abs(x)-abs(x-0.01)+0.01)
  SE2 = lambda x: (1/(2*0.01))*(abs(x)-abs(x-0.01)+0.01)

  ## Getting the user data.
  @classmethod
  def user_data (cls, is_compress):
    accepted = False
    ## Take the name file or the directory file.
    while not accepted:
      name = input (cls.MESSAGE_NAME_INPUT if is_compress else cls.MESSAGE_NAME_INPUT.replace(cls.COMPRESS, cls.  UNZIP))
      ##Verify if the file or directory exists.
      type_name = ''
      if path.exists (name) or not name:
        accepted = True
      else:
        if ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print (cls.MESSAGE_NAME_ERROR)
    return name
  
  '''
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
  '''
  
  @classmethod
  def convert_miniterms_to_numbers (cls,miniterm):
    ##Example of input: '-1100--01-111' or '-0-1-1-100111'
    ##Example of output: 32527231 (in binary '01111100000101001101111111') or 18734143 (in binary '01000111011101110000111111')
    number = 1
    for i in miniterm:
      if i == '1':
        number = (number<<2) +cls.BOOLEAN_VARIABLE_REPRESENTION
      elif i == '0':
        number = (number<<2) +cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION
      elif i == '-':
        number = (number<<2) +cls.BOOLEAN_VARIABLE_NOT_INCLUDED
    return number
  
  '''
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
      #if DEBUG and ALLOW_PROMPT_MESSAGES:
      #print (i+j, type(i+j))
    return string
  '''
  
  @classmethod
  def convert_numbers_to_miniterms (cls,miniterm_number):
    string = ''
    count = 0
    miniterm_number_size = int (filter_log(miniterm_number,2))
    mask = 3
    while count < miniterm_number_size:
      term = miniterm_number & mask
      if term == cls.BOOLEAN_VARIABLE_REPRESENTION:
        string = '1' + string
      if term == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
        string = '0' +string
      if term == cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
        string = '-' +string
      miniterm_number>>=2
      count+=2
    return string
  
  ## Starting the data bank (creating a table).
  @classmethod
  def create_data_bank (cls, path_name):
    
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_DATABASE_CREATING)
      
    if path.exists (path_name):
      remove (path_name)
    con = connect (path_name)
    cursor = con.cursor ()
    cursor.execute (cls.SQL_CREATE_DATA_BANK)
    cursor.execute (cls.SQL_CREATE_NAME)
      
    con.commit ()

    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_DATABASE_CREATING_COMPLETED)
    return con
  
  @classmethod
  def register_data_bank (cls, data, con):
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_DATABASE_REGISTER)
    cursor = con.cursor ()
    cursor.executemany (cls.SQL_INSERT_NAME, [(data[1], data[2], 1 if data[3] else 0)])
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
          if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT and CLI_MODE:
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
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
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
  
  ## Filter the input and the logaritm value
  @staticmethod
  def filter_log (num, b):
    if num > 0:
      return int (log (num, b))
    else:
      return 1
  
  '''
  #Recursive function for convert strings in numbers
  @classmethod
  def recursive_str_to_num (cls,string):
    if len(string) > 1:
      if DEBUG and ALLOW_PROMPT_MESSAGES:
        print("TRUE string:", string, "len(string): ", len(string))
      part1 = cls.recursive_str_to_num (string[:len(string)//2])
      part2 = cls.recursive_str_to_num (string[len(string)//2:])
      if DEBUG and ALLOW_PROMPT_MESSAGES:
        print ("part1: {0}, type: {1}, part2: {2}, type: {3} string: {4}, len(string): {5}".format(part1, type(part1), part2, type(part2), string, len(string)))
      #result = part1 <<(2**(3+((int(log(part2)))//8))) | part2
      result = part1 <<(2**(int(log(log(2**part2-1,2)+8,2)))) | part2
      if DEBUG and ALLOW_PROMPT_MESSAGES:
        print ("result: ", result, "part1 <<(int(log(part2))+1): ", bin(part1 <<(int(log(part2))+1)), "part2: ", bin(part2))
      return result
    else:
      if DEBUG and ALLOW_PROMPT_MESSAGES:
        print("FALSE string:", string, "len(string): ",len(string))
      return ord (string)
   '''
      
#  @classmethod
#  def recursive_str_to_num (cls,string):
#    WIDTH = 8
#    if len(string) > WIDTH and len(string)//2 >= 8:
#      print("TRUE string:", string, "width: ", WIDTH)
#      part1 = cls.recursive_str_to_num (string[:len(string)//2])
#      part2 = cls.recursive_str_to_num (string[len(string)//2:])
#      print ("part1: {0}, type: {1}, part2: {2}, type: {3}".format(part1, type(part1), part2, type(part2)))
#      result = part1 <<(int(log(part2))+1) | part2
#    else:
#      print("FALSE string:", string, "width: ", WIDTH)
#      return reduce (lambda x, y: (ord (x) if type (x) == type (str()) else x)<<8|ord (y), string)
    
  @classmethod
  def transform_content (cls, content, total_length):
    if total_length > 1 and (not cls.MAX_RECURSIVE or cls.NUMBER_RECURSIVE_FUNCTIONS < cls.MAX_RECURSIVE) and (not cls.MAX_FREE_MEMORY or virtual_memory()[1] > cls.MAX_FREE_MEMORY):
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST content: ", content, "cls.NUMBER_RECURSIVE_FUNCTIONS (up): ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      left = cls.transform_content(content[:len(content)//2], total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST 2 content: ", content, "cls.NUMBER_RECURSIVE_FUNCTIONS (up): ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      right = cls.transform_content(content[len(content)//2:], total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      
      #difference_bits_eight_left = 8-(int(log(left))+1)%8
      #difference_bits_eight_right = 8-(int(log(right))+1)%8
      #difference_bits_left = int(2**(3+round(cls.SE(int(log(int(log(left,2)),2))-2)))) -(int(log(left,2))+1)
      #difference_bits_right = int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))) -(int(log(right,2))+1)
      
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST cls.NUMBER_RECURSIVE_FUNCTIONS (down) 2: ", cls.NUMBER_RECURSIVE_FUNCTIONS, "left: ", left, "bin(left): ", bin(left), "len(bin(left)): ", len(bin(left)) -2,  "right: ", right, "bin(right): ", bin(right), "len(bin(right)): ", len(bin(right)) -2, "result: ", left << 8*round(len(content)//2) | right, "bin(result): ", bin(left << 8*round(len(content)//2) | right))
        print("len(content): ", len(content), "len(content)//2: ", len(content)//2, "round(len(content)//2)+2: ", round(len(content)//2), "8*(round(len(content)//2)): ", 8*(round(len(content)//2)), "left << 8*round(len(content)//2) | right: ", left << 8*round(len(content)//2) | right, "bin(left << 8*round(len(content)//2) | right): ", bin(left << 8*round(len(content)//2) | right))
        #print ("TEST difference bits left: ", difference_bits_left, "difference bits right: ", difference_bits_right, "difference_bits_eight_left: ", difference_bits_eight_left, "difference_bits_eight_right: ", difference_bits_eight_right)
        #print("TEST cls.NUMBER_RECURSIVE_FUNCTIONS (down) 2: ", cls.NUMBER_RECURSIVE_FUNCTIONS, "left: ", left, "bin(left): ", bin(left), "len(bin(left)): ", len(bin(left)) -2,  "right: ", right, "bin(right): ", bin(right), "len(bin(right)): ", len(bin(right)) -2, "result: ", left << int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))) | right, "bin(result): ", bin(left << int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))) | right))
        
        #print ("log(right,2): ", log(right,2), "; int(log(right,2)): ",  int(log(right,2)), "; log(int(log(right,2)),2): ", log(int(log(right,2)),2), "; int(log(int(log(right,2)),2)): ", int(log(int(log(right,2)),2)), "; cls.SE(int(log(int(log(right,2)),2))-2): ", cls.SE(int(log(int(log(right,2)),2))-2), "; round(cls.SE(int(log(int(log(right,2)),2))-2)): ", round(cls.SE(int(log(int(log(right,2)),2))-2)), "; 3+round(cls.SE(int(log(int(log(right,2)),2))-2)): ", 3+round(cls.SE(int(log(int(log(right,2)),2))-2)), "; 2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2))): ", 2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2))), "; int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))): ", int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))))
      
      #return left << (int(2**(3+round(cls.SE(int(log(int(log(right,2)),2))-2)))) -difference_bits_right +round(cls.SE2(difference_bits_right))) | right
      #return left << ((int(log(right))+1) +round(cls.SE2(difference_bits_right))) | right
      #return left << (int(log(right))+1 +(8*round(cls.SE2((int(log(right))+1)%8))-(int(log(right))+1)%8)) | right
      #print("int(log(right))+1: ", int(log(right))+1, "(int(log(right))+1)%8: ", (int(log(right))+1)%8, "(8-(int(log(right))+1)%8): ", (8-(int(log(right))+1)%8), "(int(log(right))+1 +(8-(int(log(right))+1)%8)): ", (int(log(right))+1 +(8-(int(log(right))+1)%8)))
      #return left << (int(log(right))+1 +difference_bits_eight) | right
      return left << 8*ceil(len(content)/2) | right
      
    else:
      result = 0
      count = 0
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST 3 content: ", content, "cls.NUMBER_RECURSIVE_FUNCTIONS: ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      while count < total_length or count < len(content):
        character = content[count]
        result = result<<8 | ord(character)
        count+=1
        if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
          print("TEST 4 result: ", result, "cls.NUMBER_RECURSIVE_FUNCTIONS: ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST 5 result: ", result, "cls.NUMBER_RECURSIVE_FUNCTIONS (down): ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      return result
  
  ## Find the number resulted from the user file content.
  @classmethod
  def big_number (cls, filename, recursive = False):
    BASE = 2
    is_binary = False
    ## Open and read the user file.
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_EXTRACTING_BIG_NUMBER)
    try:
      with open(filename, 'tr') as check_file:  # try open file in text mode
          content = check_file.read()
    except:  # if fail then file is non-text (binary)
      is_binary = True
      with open(filename, 'br') as check_file:  # try open file in text mode
          content = check_file.read()
            
    content = '{0}{1}'.format(chr(255),content)
    ## Transform the file in a binary number and after in a decimal number. 
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print ("PASSED HERE")
    
    #count = 0
    #while count 
    #result = cls.recursive_str_to_num (content)
    #reduce (lambda x, y: (ord (x) if type (x) == type (str()) else x)<<8|ord (y), content)
    #result = reduce (lambda x, y: ((ord (x) if type (x) == type (str()) else x)<<(cls.filter_log (ord (y),BASE)+1))|ord (y), content)
    count = 0
    total_length = len(content)
    character = None
    result = 0
    if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
      timing = TimeLeft(cls.TIME_LEFT_BIG_NUMBER, len(content), True)
    
    if not recursive:
      while count < total_length:
        character = content[count]
        result = result<<8 | ord(character)
        count+=1
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print("result (incrementing): ", result)
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
          timing.count_time_and_print()
    else:
      cls.NUMBER_RECURSIVE_FUNCTIONS = 1 ## Coloca um para que o programa possa detectar que se trata de uma chamada a uma função recursiva na linha seguinte.
      result = cls.transform_content(content, total_length) ## Chamamos uma função recursiva para continuar o processamento coforme as opções disponíveis.
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print ("TEST cls.NUMBER_RECURSIVE_FUNCTIONS: ", cls.NUMBER_RECURSIVE_FUNCTIONS)
        
    
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print ("PASSED HERE TOO")
      print("result: ", result, "bin(result): ", bin(result), "type(result): ", type(result), "len(bin(result)) -2: ", len(bin(result))-2)
    #n = ord(content[0])
    #    first = True
    #    for i in content:
    #      if first:
    #        if DEBUG:
    #          if ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT:
    #            print ("TEST: ", i)
    #        n = i
    #        first = False
      #s += cls.ZERO*(cls.BYTE -len ('{:b}'.format (i)))+ '{:b}'.format (i) 
      
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_EXTRACTING_DATA_COMPLETED)
    return result, is_binary
  
  

  ## Transform the big number in a file content again.
  ## Tarefa: remover 255 como caractere e utilizar operações binárias como alternativa mais eficiente e menos custosa.
  '''
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
  '''
  
  @classmethod
  def transform_content_revert (cls, content, total_length):
    if total_length > 8 and (not cls.MAX_RECURSIVE or cls.NUMBER_RECURSIVE_FUNCTIONS < cls.MAX_RECURSIVE) and (not cls.MAX_FREE_MEMORY or virtual_memory()[1] > cls.MAX_FREE_MEMORY):
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      difference_bits = int(2**(3+round(cls.SE(int(log(int(log(content,2)),2))-2)))) -(int(log(content,2))+1)
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST content: ", content, "bin(content): ",bin(content), "int(log(content,2))+1:", int(log(content,2))+1, "(int(log(content,2))+1 % 2) == 0: ", (int(log(content,2))+1) % 2 == 0, "difference_bits: ", difference_bits, "cls.NUMBER_RECURSIVE_FUNCTIONS (up): ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      left = cls.transform_content_revert((content>>((int(log(content,2))+1)//2)) & ((1<<((int(log(content,2))+1)//2))-1) if difference_bits == 0 else (content>>(2**(int(log(((int(log(content,2))+1)//2),2))+1))) & ((1<<((int(log(content,2))+1)//2))-1), total_length//2)
      #left = cls.transform_content_revert((content>>((int(log(content,2))+1)//2)) & ((1<<((int(log(content,2))+1)//2))-1) if int(log(content,2))+1 % 2 == 0 else (content>>((int(log(content,2))+1)//2)) & ((1<<((int(log(content,2))+1)//2 +1))-1), total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST 2 content: ", content, "bin(content): ",bin(content), "int(log(content,2))+1:", int(log(content,2))+1, "(int(log(content,2))+1) % 2 == 0: ", (int(log(content,2))+1) % 2 == 0, "content & ((1<<((int(log(content,2))+1)//2))-1):", content & ((1<<((int(log(content,2))+1)//2))-1), "content & ((1<<(((int(log(content,2))+1)//2)+1))-1):", content & ((1<<(((int(log(content,2))+1)//2)+1))-1), "difference_bits: ", difference_bits, "cls.NUMBER_RECURSIVE_FUNCTIONS (up): ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      right = cls.transform_content_revert(content & ((1<<((int(log(content,2))+1)//2))-1) if difference_bits == 0 else content & ((1<<(2**(int(log(((int(log(content,2))+1)//2),2))+1)))-1), total_length//2)
      #right = cls.transform_content_revert(content & ((1<<((int(log(content,2))+1)//2))-1) if difference_bits == 0 else content & ((1<<(((int(log(content,2))+1)//2)+difference_bits))-1), total_length//2)
      #right = cls.transform_content_revert(content & ((1<<((int(log(content,2))+1)//2))-1) if (int(log(content,2))+1) % 2 == 0 else content & ((1<<((int(log(content,2))+1)//2 +1))-1), total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST cls.NUMBER_RECURSIVE_FUNCTIONS (down) 2: ", cls.NUMBER_RECURSIVE_FUNCTIONS, "left: ", left, "right: ", right)
      return left + right
    
    else:
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST 3 content: ", content, "bin(content): ",  bin(content), "cls.NUMBER_RECURSIVE_FUNCTIONS: ", cls.NUMBER_RECURSIVE_FUNCTIONS)
      big_number_str = str() ## We will create a new variable to store strings with our number reduction.
      number_reduce = content ## The large number is assigned to the number_reduce variable to be reduced.
      while number_reduce > 1:
        char = number_reduce & cls.MASK 
        big_number_str = chr(char) + big_number_str
        number_reduce >>= 8
        if DEBUG and ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT and CLI_MODE:
          print ("chr(char): ", chr(char), "number_reduce:", number_reduce, "bin: ", bin(number_reduce))
          print("mask: ", cls.MASK, "big_number_str: ", big_number_str, "char: ", char)
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      return big_number_str
  
  @classmethod  
  ## Let's convert the number into strings via this function:
  def revert_big_number (cls, big_number, filename, is_binary, recursive = False):
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_BIG_NUMBER_REVERT_FILE)
    
    if not recursive:
      big_number_str = str() ## We will create a new variable to store strings with our number reduction.
      number_reduce = big_number ## The large number is assigned to the number_reduce variable to be reduced.
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print ("number_reduce:", number_reduce, "bin: ", bin(number_reduce), 'length: ', len(bin(number_reduce))-2)
      while number_reduce > 1:
        char = number_reduce & cls.MASK 
        big_number_str = chr(char) + big_number_str
        number_reduce >>= 8
        if DEBUG and ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT and CLI_MODE:
          print ("number_reduce:", number_reduce, "bin: ", bin(number_reduce))
          print("mask: ", cls.MASK, "big_number_str: ", big_number_str, "char: ", char)
    else:
      big_number_str2 = str() ## We will create a new variable to store strings with our number reduction.
      number_reduce = big_number ## The large number is assigned to the number_reduce variable to be reduced.
      count = int(log(big_number,2))+1
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print ("number_reduce:", number_reduce, "bin: ", bin(number_reduce), 'length: ', len(bin(number_reduce))-2)
      while number_reduce > 1 and log(count,2) % 2 != 0:
        char = number_reduce & cls.MASK 
        big_number_str2 = chr(char) + big_number_str2
        number_reduce >>= 8
        count-= 8
        if DEBUG and ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT and CLI_MODE:
          print ("number_reduce:", number_reduce, "bin: ", bin(number_reduce))
          print("mask: ", cls.MASK, "big_number_str: ", big_number_str2, "char: ", char)
      cls.NUMBER_RECURSIVE_FUNCTIONS = 1
      if number_reduce > 1:
        big_number_str = cls.transform_content_revert (number_reduce, int(log(number_reduce, 2))+1)
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print ("big_number_str: ", big_number_str, "big_number_str2: ", big_number_str2)
        big_number_str += big_number_str2
      else:
        big_number_str = big_number_str2
      del big_number_str2
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print ("result: ", big_number_str)
    
    big_number_str = big_number_str[1:]
    ## Open and write the new file.
    if is_binary:
      with open (filename, "wb") as f:
          f.write (big_number_str)
    else:
      with open (filename, "w") as f:
          f.write (big_number_str)
        #n = int (big_number_str[i :i +cls.BYTE -1], 2)
        #f.write (n.to_bytes (2, 'big'))
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_FILE_CREATION_COMPL)
      
  @classmethod
  def boolean_algebra (cls,number):
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_COMPRESS_OPERATION)
    #With the Quine-McCluskey function we don't need to worry about the elaboration and understanding of the algorithm, rather we can just
     #define which Boolean algebra we want using a specific module for this.
    qm = QuineMcCluskey()
    #First, we must perform an operation to determine the positions in which the number 1, the digit of a binary number, appears within the large decimal number 
    #(and which we must turn into binary).
    #We have to determine the limits for the inclusion of lists in order to avoid overflows.
    result_ones = list()
    #result_dontcares = list()
    #number_str = '{:b}'.format(number) ## We store a determined sequence of bits for later analysis
    #count_ones = number_str.count ('1') ## We count the number of ones in the binary sequence
    count_ones = int(log(number, 2))
    number_reduced = int(number)
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print ("First number_reduced: ", number_reduced, "bin(number_reduced): ", bin(number_reduced), 'length: ', len(bin(number_reduced))-2)
    if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
      timing = TimeLeft(cls.TIME_LEFT_REDUCE_BITS, count_ones, True)
    
    while count_ones >= 0 and number_reduced > 0: ## Colocar aqui um timer remaining
      ones = list()
      while len(ones) < cls.MAX_SIZE -1 and count_ones >= 0 and number_reduced > 0:
        if number_reduced & 1 == 1: #if number_reduced % 2 == 1:
          ones.append(count_ones)
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print ("TESTE count_ones: ", count_ones, "number_reduced: ", number_reduced)
        count_ones-=1
        number_reduced >>= 1 
        #number_reduced //= 2 
        
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
          timing.count_time_and_print()
        #if DEBUG and ALLOW_PROMPT_MESSAGES:
        #print("bit (after number_reduced //= 2): number_reduced % 2: ", number_reduced % 2)
      result_ones.append(ones)
    #number_str_len = len (number_str) ## We determine the length of this sequence
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
    #number_substr = number_str ## As we are going to reduce the amount of bits that we put as a string, we need a variable to carry out this elimination process
    #for i in range(ceil (current_len  /cls.MAX_SIZE)):
    #while number_substr: ## Here we will carry out the process of counting ones respecting the limits of list formation of the operating system to use the Quine-McCluskey function.
    #ones = list (map (lambda a: a[0], list(filter (lambda x: x[1] == '1', list(enumerate(number_substr[:cls.MAX_SIZE]))))))
    #result_ones.append(ones) ## We will store all the results and also do all the Boolean formula transformation operations separately.
    #number_substr = number_substr[cls.MAX_SIZE:len(number_substr)] ## We will perform binary sequence reduction according to cls.MAX_SIZE
    #current_len = len (number_substr)
    #current_pos = current_len if current_len < cls.MAX_SIZE else cls.MAX_SIZE
    
    ## Now we need to know how many bits are dontcares. We will calculate the complement to determine what those bits would be.
    amount_bits_number = int(log(number,2)) +1
    complement = 2**(int(log (amount_bits_number, 2))+1) ## We will use the size of the bit stream to calculate the amount of doncares for this purpose. Thus, the difference between the largest exponential number in base 2 will be the limit, and the size of the bit stream will be put at the beginning of the dontcares bit stream.
    final_num = amount_bits_number % (cls.MAX_SIZE+1) ## Here we will filter all values above cls.MAX_SIZE, which would be the maximum limit for creating lists in Python according to the bit width of the hardware word or instruction.
     ## Since the bitlist is in packets, each intermediate packet is complete and need not count dontcares, but the last packet, as well as a single bitstream packet, can have dontcares bits.
    dontcares = list(range(final_num, complement if complement -1 <= cls.MAX_SIZE else cls.MAX_SIZE+1)) ## Here we will create a list with all the dontcares bits
    #result_dontcares.append(dontcares)
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print ("result_ones: ", result_ones,"dontcares: ", dontcares, "type(result_ones): ", type(result_ones), "type(dontcares): ", type(dontcares))
    result = [qm.simplify(i, [] if (result_ones.index(i) +1 != len(result_ones)) else dontcares) for i in result_ones[:-1 if len(result_ones) > 1 else 1]] ## We will return the result of simplifying the bitstream with all boolean functions in a list.
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_QUINE_MCCLUSKEY_COMPL)
      print(cls.MESSAGE_COMPRESS_OPERATION_COMPL)
      
    return result 
  
  ## Compact the file or the directory (main function).
  @classmethod
  def compact_file (cls, filename):
    
    if path.isfile (filename):
      if ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print(cls.MESSAGE_PREPARING_COMPRESS)
      filesize = Path(filename).stat().st_size * 8
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print("filename: ", filename, "filesize: ", filesize)
      filename_modified = cls.change_name (filename, cls.EXT)
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print(filename)
      number, is_binary = cls.big_number(filename) ## Transform the file in a big number.
      if DEBUG and PRINT_LONG_TEXT and CLI_MODE and ALLOW_PROMPT_MESSAGES:
          print(number)
      #cls.revert_big_number(number,filename[0], '.2txt', first_num)
      ## The binary sequence must be simplified with the Quine-McCluskey algorithm.
      boolean_functions = cls.boolean_algebra(number)
      if DEBUG and ALLOW_PROMPT_MESSAGES and PRINT_LONG_TEXT and CLI_MODE:
          print(boolean_functions[0])
      ## Register all the changes in a data bank.
      con = cls.create_data_bank(filename_modified) ## Starting the data bank.
      cls.register_data_bank([boolean_functions, filename, filesize +8, is_binary], con) ## Filesize variable must need have a sum operation with eight because the character with binary number 255 was inserted.
      if ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print(cls.MESSAGE_SUCCESSFULLY_CREATED)
      con.close()
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_COMPLETED_COMPRESS)
  
  @classmethod
  def read_data_bank (cls,con):
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_READING_DATABANK)
    cursor = con.cursor ()
    cursor.execute(cls.SQL_READ_DATABANK)
    boolean_functions = cursor.fetchall()
    cursor.execute(cls.SQL_READ_COMPLEMENT)
    datacompl = cursor.fetchall()
    filename = datacompl[0][0]
    filesize = datacompl[0][1]
    if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print("filesize (reading_data_bank): ", filesize)
    is_binary = datacompl[0][2]
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_READING_COMPLETED)
    return boolean_functions, filename, filesize, is_binary
  
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

  '''
  @classmethod
  def thuth_table_recursive_deeper2(cls, boolean_functions, count):
    mask = 3
    count2 = 0
    mini_lenght = int(log (boolean_functions[0][0],2))+1
    bit_count = filesize
    result = 1
    final_result = cls.thuth_table_recursive_deeper2(boolean_functions, count -1)
    #while count2 < mini_lenght//2:
    bits = miniterm_q & mask
    if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
      if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
        if bit_count & 1 == 1:
          result &= 1
        else:
          result &= 0
      elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
        if bit_count & 1 == 0:
          result &= 1 
        else: 
          result &= 0
    miniterm_q>>=2
    bit_count>>=1
    count2+=1
    return result
  '''
  '''
    mask = 3
    count2 = 0
    mini_lenght = int(log (boolean_functions[0][0],2))+1
    bit_count = filesize
    result = 1
      while count2 < mini_lenght//2:
        bits = miniterm_q & mask
      if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
        if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
          if bit_count & 1 == 1:
            result &= 1
          else:
            result &= 0
        elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
          if bit_count & 1 == 0:
            result &= 1 
          else: 
            result &= 0
      miniterm_q>>=2
      bit_count>>=1
      count2+=1
    #result_or |= result
    return result
  '''
  
  '''
  @classmethod
  def thuth_table_recursive_deeper(cls, boolean_functions, filesize, total_length):
    if total_length > 1 and (not cls.MAX_RECURSIVE or cls.NUMBER_RECURSIVE_FUNCTIONS < cls.MAX_RECURSIVE) and (not cls.MAX_FREE_MEMORY or virtual_memory()[1] > cls.MAX_FREE_MEMORY):
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print("1705 TEST 1 filesize: {0}, total_length: {1} (thuth_table_recursive_deeper)".format(filesize, total_length))
      left = cls.thuth_table_recursive_deeper(boolean_functions[:len(boolean_functions)//2], filesize, total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      right = cls.thuth_table_recursive_deeper(boolean_functions[len(boolean_functions)//2:], filesize, total_length//2)
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      #return left << ceil(len(boolean_functions)/2) | right
      return left | right
    else:
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print("1714 TEST 2 filesize: {0}, total_length: {1} (thuth_table_recursive_deeper)".format(filesize, total_length))
      mask = 3
      count2 = 0
      mini_lenght = int(log (boolean_functions[0][0],2))+1
      bit_count = filesize
      result = 1
      result_or = 0
      for i in boolean_functions:
        miniterm_q = i[0]
        while count2 < mini_lenght//2:
          bits = miniterm_q & mask
          if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
            if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
              if bit_count & 1 == 1:
                result &= 1
              else:
                result &= 0
            elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
              if bit_count & 1 == 0:
                result &= 1 
              else: 
                result &= 0
          miniterm_q>>=2
          bit_count>>=1
          count2+=1
          print("1745 TEST 3 miniterm: {0}, bin(miniterm_q): {4}, bit_count: {1}, bin(bit_count): {5}, count2: {2}, result: {3} (thuth_table_recursive_deeper).".format(miniterm_q, bit_count, count2, result, bin(miniterm_q), bin(bit_count)))
        result_or |= result
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print("1747 TEST 4 result_or: {0}, miniterm: {1} (thuth_table_recursive_deeper).".format(result_or, miniterm_q))
      return result_or
      
      
      
      mask = 3
      mini_lenght = int(log (boolean_functions[0][0],2))+1
      count = 0
      big_number_result = 0
      while count < filesize:
        result_or = 0
        for i in boolean_functions:
          ## Primeiro devemos recolher cada um dos minitermos e substituir cada caractere pela sua devida variável.
          miniterm_q = i[0]
          count2 = 0
          bit_count = count
          result = 1
          while count2 < mini_lenght//2:
            bits = miniterm_q & mask
            if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
              if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
                if bit_count & 1 == 1:
                  result &= 1
                else:
                  result &= 0
              elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
                if bit_count & 1 == 0:
                  result &= 1 
                else: 
                  result &= 0
            miniterm_q>>=2
            bit_count>>=1
            count2+=1
          result_or |= result
        count+=1
        big_number_result = big_number_result<<1 | result_or
      return big_number_result
      '''

  '''
  @classmethod
  def truth_table_recursive (cls,boolean_functions, filesize):
    if filesize > 1 and (not cls.MAX_RECURSIVE or cls.NUMBER_RECURSIVE_FUNCTIONS < cls.MAX_RECURSIVE) and (not cls.MAX_FREE_MEMORY or virtual_memory()[1] > cls.MAX_FREE_MEMORY):
      cls.NUMBER_RECURSIVE_FUNCTIONS+=1
      big_number_result = cls.truth_table_recursive(boolean_functions, filesize -1)
      partial_result = cls.thuth_table_recursive_deeper(boolean_functions, filesize -1,len(boolean_functions))
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print("1792 TEST 1 partial_result: {0}, big_number_result: {1}, bin(big_number_result): {2}, filesize: {3} (truth_table_recursive; exiting from thuth_table_recursive_deeper).".format(partial_result, big_number_result, bin(big_number_result), filesize))
      big_number_result = big_number_result<<(1) | partial_result
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print("1795 TEST 2 big_number_result: {0} (truth_table_recursive).".format(big_number_result))
      #big_number_result = big_number_result<<(int(log(partial_result))+1) |partial_result
      cls.NUMBER_RECURSIVE_FUNCTIONS-=1
      return big_number_result
    elif (not cls.MAX_RECURSIVE or cls.NUMBER_RECURSIVE_FUNCTIONS < cls.MAX_RECURSIVE) and (not cls.MAX_FREE_MEMORY or virtual_memory()[1] > cls.MAX_FREE_MEMORY):
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print ("1788 TEST 3 FIRST! Filesize: {0} (truth_table_recursive).".format(filesize))
      return cls.thuth_table_recursive_deeper(boolean_functions, filesize, len(boolean_functions))
    else:
      if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
        print ("TEST 4 ENTER HERE!!! (truth_table_recursive)")
      mask = 3
      mini_lenght = int(log (boolean_functions[0][0],2))+1
      count = 0
      big_number_result = 0
      while count < filesize:
        result_or = 0
        for i in boolean_functions:
          ## Primeiro devemos recolher cada um dos minitermos e substituir cada caractere pela sua devida variável.
          miniterm_q = i[0]
          count2 = 0
          bit_count = count
          result = 1
          while count2 < mini_lenght//2:
            bits = miniterm_q & mask
            if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
              if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
                if bit_count & 1 == 1:
                  result &= 1
                else:
                  result &= 0
              elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
                if bit_count & 1 == 0:
                  result &= 1 
                else: 
                  result &= 0
            miniterm_q>>=2
            bit_count>>=1
            count2+=1
          result_or |= result
        count+=1
        big_number_result = big_number_result<<1 | result_or
      return big_number_result
  '''
  
  @classmethod
  #@njit(parallel = True)
  def output_truth_table (cls,boolean_functions, filesize): #, recursive = False):
    #if ALLOW_PROMPT_MESSAGES and CLI_MODE:
    #print(cls.MESSAGE_DECOMPRESSION)
    ## O objetivo com esta função é conseguir a saída de uma tabela verdade.
    ## Dentro de cada variável do vetor ou da lista boolean_functions existem tuplas cujos valores são:
    ## LEVEL_ID, package_number, pos_miniterm_pack, miniterm
    ## Exemplo de entrada:
    ## [(1, 0, 0, '-1100--01-111'), (2, 0, 1, '-0-1-1-100111'), (3, 0, 2, '-110101010-0-'), (4, 0, 3, '-1010-000000-'), (5, 0, 4, '-0001111100-0')]

    if True: #if not recursive:
      if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
        timing = TimeLeft(cls.TIME_LEFT_ASSEMBLY_BOOL_ALG,filesize, True)

      mask = 3
      mini_lenght = int(log (boolean_functions[0][0],2))+1
      count = 0
      big_number_result = 0
      while count < filesize:
        result_or = 0
        for i in boolean_functions:
          ## Primeiro devemos recolher cada um dos minitermos e substituir cada caractere pela sua devida variável.
          miniterm_q = i[0]
          count2 = 0
          bit_count = count
          result = 1
          if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
            print("miniterm:", miniterm_q, "bin: ", bin(miniterm_q))
          while count2 < mini_lenght//2:
            bits = miniterm_q & mask
            if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
              print ("({0}/{1}) processed, ".format(count2, mini_lenght//2), "teste0, bits: ", bits, "count:", count)
            if bits != cls.BOOLEAN_VARIABLE_NOT_INCLUDED:
              if bits == cls.BOOLEAN_VARIABLE_REPRESENTION:
                if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
                  print("teste1: ", bits, "bit_count & 1 == 1", bit_count & 1 == 1)
                if bit_count & 1 == 1:
                  result &= 1
                else:
                  result &= 0
              elif bits == cls.NEGATE_BOOLEAN_VARIABLE_REPRESENTION:
                if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
                  print("teste2", bits,bit_count & 1 == 0)
                if bit_count & 1 == 0:
                  result &= 1 
                else: 
                  result &= 0
              if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
                print("result!!!", result)
            miniterm_q>>=2
            bit_count>>=1
            if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
              print ("result: ", result, "count2: ", count2, "count: ", count, "bit_count:", bit_count,"result_or: ", result_or) 
            count2+=1
          result_or |= result
        count+=1
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print("FINISH result_or: ", result_or)
          
        big_number_result = big_number_result<<1 | result_or
        
        if DEBUG and ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print("NEXT BIT big_number_result: ", big_number_result, ", count: ", count)
          
        if ALLOW_PROMPT_MESSAGES and ENABLE_TIME_LEFT_APPEAR and CLI_MODE:
          timing.count_time_and_print()
    '''
    else:
      cls.NUMBER_RECURSIVE_FUNCTIONS = 1
      big_number_result = cls.truth_table_recursive (boolean_functions, filesize)
      if ALLOW_PROMPT_MESSAGES and DEBUG and CLI_MODE:
        print("TEST: big_number_result: ", big_number_result, ", bin(big_number_result): ", bin(big_number_result), "len(bin(big_number_result)) -2: ", len(bin(big_number_result))-2)
      #exit(0)
    '''
        
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_SET_BOOLEAN_ALGEBRA_COMPL)
    
    return big_number_result
  
  ## descompact the file or the directory (main function).
  @classmethod
  def descompact_file (cls, data):
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_PREPARING_DESCOMPRESSION)
    if path.isfile (data): ## If the user input is a file and not a folder.
      con = connect (data) ## Starting the data bank.
      boolean_functions, filename, filesize, is_binary = cls.read_data_bank (con) ## Read all the components of the data bank.
      number = cls.output_truth_table (boolean_functions, filesize) ## Recover the big number from boolean functions.
      ## Register all the changes in a data bank.
      if DEBUG:
        if ALLOW_PROMPT_MESSAGES and CLI_MODE:
          print (boolean_functions[0])
          print("TEST: filename: ",filename)
          if PRINT_LONG_TEXT:
            print ("big number", number)
      cls.revert_big_number(number, filename, is_binary)
      con.close()
    if ALLOW_PROMPT_MESSAGES and CLI_MODE:
      print(cls.MESSAGE_SUCCESSFULLY_RECOVERED)
      print(cls.MESSAGE_DECOMPRESSION_FINISH)

## Main program

if CLI_MODE:
  data = True
  choice = 1
  while data and choice != '3':
    choice = input(EggCellCompactor.MESSAGE_USER_MENU)
    if choice == '1':
      data = EggCellCompactor.user_data (True)
      if data:
        EggCellCompactor.compact_file (data)
    elif choice == '2':
      data = EggCellCompactor.user_data (False)
      if data:
        EggCellCompactor.descompact_file (data)