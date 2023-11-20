The program transforms files into Boolean functions and stores these Boolean functions in a local database. Once they are stored, the Boolean functions can be extracted to retrieve the file and compose it again by the same program.

One of the problems that the program currently has would be data corruption after recovering the Boolean functions file, which is a problem considered complex to resolve. Another issue is that the program previously had as its main reason for existence the recursive compression of files with the storage of Boolean functions that represented the file bits as logical outputs, and the idea was to compress the files in such a way that there would be a considerable reduction in the size of the files. The objective was to reduce file sizes in order to have more disk storage space. Unfortunately, this objective was not achieved because it was discovered that storing the Boolean functions of the files required more storage space than the file itself.

As the main objective of the program was frustrated during the algorithm studies, during implementation and after the discoveries, unfortunately the program was discontinued and will no longer be implemented. The program is also considered obsolete and is only useful for studying. Currently the program is in Command Line Interface (CLI) mode and not in graphical mode.