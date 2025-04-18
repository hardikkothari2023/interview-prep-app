def generate_qa(topic):
    sample_data = {
        "data structures": [
            {
                "question": "What is a stack?",
                "options": ["A LIFO data structure", "A FIFO data structure", "A tree data structure", "A graph data structure"],
                "correctAnswer": "A LIFO data structure"
            },
            {
                "question": "Explain binary trees.",
                "options": ["A tree with max 2 children per node", "A tree with max 3 children per node", "A cyclic graph", "A stack data structure"],
                "correctAnswer": "A tree with max 2 children per node"
            },
            {
                "question": "What is a queue?",
                "options": ["A LIFO data structure", "A FIFO data structure", "A cyclic data structure", "A tree data structure"],
                "correctAnswer": "A FIFO data structure"
            },
            {
                "question": "Explain linked lists.",
                "options": ["A linear collection of elements where each element points to the next", "A collection of nodes connected by edges", "A cyclic data structure", "A stack data structure"],
                "correctAnswer": "A linear collection of elements where each element points to the next"
            },
            {
                "question": "What is a graph?",
                "options": ["A linear collection of elements", "A collection of nodes connected by edges", "A cyclic data structure", "A tree data structure"],
                "correctAnswer": "A collection of nodes connected by edges"
            }
        ],
        "machine learning": [
            {
                "question": "What is overfitting?",
                "options": [
                    "Model performs well on train but poorly on test data",
                    "Model performs well on both train and test data",
                    "Model performs poorly on both train and test data",
                    "Model performs well on test but poorly on train data"
                ],
                "correctAnswer": "Model performs well on train but poorly on test data"
            },
            {
                "question": "Define precision and recall.",
                "options": [
                    "Precision = TP / (TP+FP), Recall = TP / (TP+FN)",
                    "Precision = FP / (FP+TN), Recall = TN / (TN+FP)",
                    "Precision = TP / (TP+TN), Recall = FP / (FP+TN)",
                    "Precision = TN / (TN+FP), Recall = FN / (FN+TP)"
                ],
                "correctAnswer": "Precision = TP / (TP+FP), Recall = TP / (TP+FN)"
            },
            {
                "question": "What is the difference between supervised and unsupervised learning?",
                "options": [
                    "Supervised learning uses labeled data, while unsupervised learning uses unlabeled data",
                    "Supervised learning uses unlabeled data, while unsupervised learning uses labeled data",
                    "Both use labeled data",
                    "Both use unlabeled data"
                ],
                "correctAnswer": "Supervised learning uses labeled data, while unsupervised learning uses unlabeled data"
            },
            {
                "question": "Explain the bias-variance tradeoff.",
                "options": [
                    "The bias-variance tradeoff is the balance between the model's ability to generalize and its complexity",
                    "The bias-variance tradeoff is the relationship between accuracy and error in training",
                    "The bias-variance tradeoff defines the optimal amount of training data required",
                    "The bias-variance tradeoff measures how well a model fits the data"
                ],
                "correctAnswer": "The bias-variance tradeoff is the balance between the model's ability to generalize and its complexity"
            },
            {
                "question": "What is cross-validation?",
                "options": [
                    "Cross-validation is a technique used to evaluate machine learning models by splitting data into multiple subsets",
                    "Cross-validation is a process of training a model on one set and testing it on another",
                    "Cross-validation is used to tune hyperparameters of the model",
                    "Cross-validation is the evaluation of model performance using a single test set"
                ],
                "correctAnswer": "Cross-validation is a technique used to evaluate machine learning models by splitting data into multiple subsets"
            }
        ],
        "python": [
            {
                "question": "What is a Python decorator?",
                "options": [
                    "A function that wraps another function to modify its behavior",
                    "A special class for Python objects",
                    "A way to define functions inside other functions",
                    "A function that handles exceptions"
                ],
                "correctAnswer": "A function that wraps another function to modify its behavior"
            },
            {
                "question": "Explain list comprehension in Python.",
                "options": [
                    "A concise way to create lists using a single line of code",
                    "A type of loop used to iterate through lists",
                    "A way to define classes inside lists",
                    "A method to filter list elements based on conditions"
                ],
                "correctAnswer": "A concise way to create lists using a single line of code"
            },
            {
                "question": "What are lambda functions in Python?",
                "options": [
                    "Lambda functions are small anonymous functions defined using the `lambda` keyword",
                    "Lambda functions are functions that take a lambda expression as input",
                    "Lambda functions are functions with no return values",
                    "Lambda functions are functions that can take multiple parameters"
                ],
                "correctAnswer": "Lambda functions are small anonymous functions defined using the `lambda` keyword"
            },
            {
                "question": "What is the difference between deep copy and shallow copy?",
                "options": [
                    "A shallow copy copies references to objects, while a deep copy copies the objects themselves",
                    "A deep copy copies references, while a shallow copy copies the objects themselves",
                    "A shallow copy is faster, while a deep copy is more memory-efficient",
                    "A deep copy is used for immutable objects, while a shallow copy is used for mutable objects"
                ],
                "correctAnswer": "A shallow copy copies references to objects, while a deep copy copies the objects themselves"
            },
            {
                "question": "What are Python generators?",
                "options": [
                    "Generators are functions that allow iteration over data without loading it all into memory at once",
                    "Generators are data structures used for storing large datasets",
                    "Generators are functions that return values immediately without using `yield`",
                    "Generators are used to define the flow of control in loops"
                ],
                "correctAnswer": "Generators are functions that allow iteration over data without loading it all into memory at once"
            }
        ],"web development": [
    {
        "question": "What is HTML?",
        "options": [
            "A programming language",
            "A markup language for creating web pages",
            "A database management system",
            "A CSS framework"
        ],
        "correctAnswer": "A markup language for creating web pages"
    },
    {
        "question": "What does CSS stand for?",
        "options": [
            "Cascading Style Sheets",
            "Common Style Sheets",
            "Creative Style Sheets",
            "Computer Style Sheets"
        ],
        "correctAnswer": "Cascading Style Sheets"
    },
    {
        "question": "Which tag is used to link an external CSS file?",
        "options": [
            "<style>",
            "<link>",
            "<css>",
            "<a>"
        ],
        "correctAnswer": "<link>"
    },
    {
        "question": "What is the purpose of JavaScript?",
        "options": [
            "To style a webpage",
            "To structure a webpage",
            "To add interactivity to a webpage",
            "To handle user inputs"
        ],
        "correctAnswer": "To add interactivity to a webpage"
    },
    {
        "question": "Which of the following is NOT a JavaScript framework?",
        "options": [
            "React",
            "Angular",
            "Vue",
            "HTML"
        ],
        "correctAnswer": "HTML"
    }
],"databases": [
    {
        "question": "What is a primary key?",
        "options": [
            "A unique identifier for a table's record",
            "A foreign key that references another table",
            "An index for a table",
            "A type of query in SQL"
        ],
        "correctAnswer": "A unique identifier for a table's record"
    },
    {
        "question": "Which SQL command is used to retrieve data from a database?",
        "options": [
            "INSERT",
            "SELECT",
            "DELETE",
            "UPDATE"
        ],
        "correctAnswer": "SELECT"
    },
    {
        "question": "What is normalization in databases?",
        "options": [
            "The process of minimizing redundancy",
            "The process of adding more tables",
            "The process of adding indexes",
            "The process of defining foreign keys"
        ],
        "correctAnswer": "The process of minimizing redundancy"
    },
    {
        "question": "What is the difference between INNER JOIN and LEFT JOIN?",
        "options": [
            "INNER JOIN returns records with matching values in both tables, LEFT JOIN returns all records from the left table",
            "INNER JOIN returns all records from both tables, LEFT JOIN returns only matching records",
            "There is no difference",
            "LEFT JOIN returns records with matching values in both tables"
        ],
        "correctAnswer": "INNER JOIN returns records with matching values in both tables, LEFT JOIN returns all records from the left table"
    },
    {
        "question": "What is a foreign key?",
        "options": [
            "A primary key in another table",
            "A key used to establish a relationship between two tables",
            "A unique identifier for a table's record",
            "A key used for indexing tables"
        ],
        "correctAnswer": "A key used to establish a relationship between two tables"
    }
]
,"cloud computing": [
    {
        "question": "What is cloud computing?",
        "options": [
            "Computing resources provided over the internet",
            "The use of local data storage",
            "A type of database management",
            "The practice of using computers offline"
        ],
        "correctAnswer": "Computing resources provided over the internet"
    },
    {
        "question": "Which of the following is NOT a type of cloud service?",
        "options": [
            "Infrastructure as a Service (IaaS)",
            "Platform as a Service (PaaS)",
            "Software as a Service (SaaS)",
            "Operating System as a Service (OaaS)"
        ],
        "correctAnswer": "Operating System as a Service (OaaS)"
    },
    {
        "question": "What is the main advantage of using cloud computing?",
        "options": [
            "Cost efficiency",
            "Local data storage",
            "Faster processing speeds",
            "Limited access to resources"
        ],
        "correctAnswer": "Cost efficiency"
    },
    {
        "question": "What is a public cloud?",
        "options": [
            "Cloud resources shared with multiple users",
            "Cloud resources available only to a single organization",
            "A cloud hosted locally",
            "A cloud with limited storage resources"
        ],
        "correctAnswer": "Cloud resources shared with multiple users"
    },
    {
        "question": "Which service model provides the most control to the user?",
        "options": [
            "IaaS",
            "PaaS",
            "SaaS",
            "DaaS"
        ],
        "correctAnswer": "IaaS"
    }
]
,"artificial intelligence": [
    {
        "question": "What is artificial intelligence?",
        "options": [
            "The simulation of human intelligence in machines",
            "A software program for data storage",
            "A way to store and manage large datasets",
            "A system for solving mathematical problems"
        ],
        "correctAnswer": "The simulation of human intelligence in machines"
    },
    {
        "question": "Which of the following is a subfield of AI?",
        "options": [
            "Machine Learning",
            "Databases",
            "Operating Systems",
            "Web Development"
        ],
        "correctAnswer": "Machine Learning"
    },
    {
        "question": "What is supervised learning?",
        "options": [
            "A type of machine learning where the model is trained with labeled data",
            "A type of AI that simulates human consciousness",
            "A method used to collect data from users",
            "A way of training models using unsupervised data"
        ],
        "correctAnswer": "A type of machine learning where the model is trained with labeled data"
    },
    {
        "question": "What is reinforcement learning?",
        "options": [
            "A learning method where the agent learns by interacting with an environment and receiving rewards",
            "A type of machine learning with unsupervised data",
            "A method used to store data in a cloud environment",
            "A supervised learning method for classification"
        ],
        "correctAnswer": "A learning method where the agent learns by interacting with an environment and receiving rewards"
    },
    {
        "question": "What is natural language processing (NLP)?",
        "options": [
            "A field of AI that focuses on the interaction between computers and human language",
            "A method of database management",
            "A system for managing large datasets",
            "A type of machine learning used for regression tasks"
        ],
        "correctAnswer": "A field of AI that focuses on the interaction between computers and human language"
    }
]
,"cybersecurity": [
    {
        "question": "What is a firewall?",
        "options": [
            "A network security system that monitors and controls incoming and outgoing network traffic",
            "A tool for storing data",
            "A method for optimizing internet speeds",
            "A type of encryption algorithm"
        ],
        "correctAnswer": "A network security system that monitors and controls incoming and outgoing network traffic"
    },
    {
        "question": "What is the primary function of encryption?",
        "options": [
            "To secure data by converting it into a readable format",
            "To compress files",
            "To reduce the size of data",
            "To protect data by converting it into an unreadable format"
        ],
        "correctAnswer": "To protect data by converting it into an unreadable format"
    },
    {
        "question": "What is phishing?",
        "options": [
            "A method of tricking people into revealing sensitive information",
            "A tool for optimizing data storage",
            "A system for managing network traffic",
            "A method for securing passwords"
        ],
        "correctAnswer": "A method of tricking people into revealing sensitive information"
    },
    {
        "question": "What does VPN stand for?",
        "options": [
            "Virtual Private Network",
            "Virtual Public Network",
            "Visible Private Network",
            "Visible Public Network"
        ],
        "correctAnswer": "Virtual Private Network"
    },
    {
        "question": "What is multi-factor authentication?",
        "options": [
            "A security system that requires more than one method of authentication",
            "A system used to encrypt data",
            "A tool for managing network traffic",
            "A method for accessing data using a single password"
        ],
        "correctAnswer": "A security system that requires more than one method of authentication"
    }
]
,"operating systems": [
    {
        "question": "What is the role of the operating system?",
        "options": [
            "Manages hardware resources and provides services for computer programs",
            "Stores files and data",
            "Provides network connectivity",
            "Handles application installations"
        ],
        "correctAnswer": "Manages hardware resources and provides services for computer programs"
    },
    {
        "question": "What is the difference between a process and a thread?",
        "options": [
            "A process is a program in execution, and a thread is a smaller unit of a process",
            "A process is a collection of threads, and a thread is a program in execution",
            "A thread is a collection of programs, and a process is an execution unit",
            "There is no difference"
        ],
        "correctAnswer": "A process is a program in execution, and a thread is a smaller unit of a process"
    },
    {
        "question": "What is virtual memory?",
        "options": [
            "A memory management technique that gives an application the illusion of having a large, contiguous block of memory",
            "Memory used by graphics-intensive applications",
            "A technique for optimizing file storage on hard drives",
            "A hardware-based memory optimization method"
        ],
        "correctAnswer": "A memory management technique that gives an application the illusion of having a large, contiguous block of memory"
    },
    {
        "question": "What is a file system?",
        "options": [
            "A method for storing and organizing files on storage devices",
            "A hardware component that manages file access",
            "A type of encryption used for file protection",
            "A program used to manage application installation"
        ],
        "correctAnswer": "A method for storing and organizing files on storage devices"
    },
    {
        "question": "What is the difference between a deadlock and a race condition?",
        "options": [
            "A deadlock is when two processes are waiting for each other to release resources, while a race condition occurs when two processes access shared resources simultaneously",
            "A deadlock is caused by the operating system, while a race condition is caused by hardware",
            "A deadlock is when processes cannot execute at all, while a race condition prevents processes from completing correctly",
            "There is no difference"
        ],
        "correctAnswer": "A deadlock is when two processes are waiting for each other to release resources, while a race condition occurs when two processes access shared resources simultaneously"
    }
],"sql": [
            {
                "question": "What is a primary key?",
                "options": [
                    "A unique identifier for a table's record",
                    "A foreign key that references another table",
                    "An index for a table",
                    "A type of query in SQL"
                ],
                "correctAnswer": "A unique identifier for a table's record"
            },
            {
                "question": "Which SQL command is used to retrieve data from a database?",
                "options": [
                    "INSERT",
                    "SELECT",
                    "DELETE",
                    "UPDATE"
                ],
                "correctAnswer": "SELECT"
            },
            {
                "question": "What is normalization in databases?",
                "options": [
                    "The process of minimizing redundancy",
                    "The process of adding more tables",
                    "The process of adding indexes",
                    "The process of defining foreign keys"
                ],
                "correctAnswer": "The process of minimizing redundancy"
            },
            {
                "question": "What is the difference between INNER JOIN and LEFT JOIN?",
                "options": [
                    "INNER JOIN returns records with matching values in both tables, LEFT JOIN returns all records from the left table",
                    "INNER JOIN returns all records from both tables, LEFT JOIN returns only matching records",
                    "There is no difference",
                    "LEFT JOIN returns records with matching values in both tables"
                ],
                "correctAnswer": "INNER JOIN returns records with matching values in both tables, LEFT JOIN returns all records from the left table"
            },
            {
                "question": "What is a foreign key?",
                "options": [
                    "A primary key in another table",
                    "A key used to establish a relationship between two tables",
                    "A unique identifier for a table's record",
                    "A key used for indexing tables"
                ],
                "correctAnswer": "A key used to establish a relationship between two tables"
            }

        ],"algorithms": [
            {
                "question": "What is the time complexity of binary search?",
                "options": [
                    "O(n)",
                    "O(log n)",
                    "O(n^2)",
                    "O(1)"
                ],
                "correctAnswer": "O(log n)"
            },
            {
                "question": "Which sorting algorithm has the best average time complexity?",
                "options": [
                    "Bubble Sort",
                    "Quick Sort",
                    "Merge Sort",
                    "Insertion Sort"
                ],
                "correctAnswer": "Quick Sort"
            },
            {
                "question": "What is a greedy algorithm?",
                "options": [
                    "An algorithm that always makes the locally optimal choice",
                    "An algorithm that solves problems by dividing them into smaller sub-problems",
                    "An algorithm that checks all possibilities to find the best solution",
                    "An algorithm that uses dynamic programming to solve problems"
                ],
                "correctAnswer": "An algorithm that always makes the locally optimal choice"
            },
            {
                "question": "What is the time complexity of quicksort in the worst case?",
                "options": [
                    "O(n log n)",
                    "O(n^2)",
                    "O(log n)",
                    "O(n)"
                ],
                "correctAnswer": "O(n^2)"
            },
            {
                "question": "What is dynamic programming?",
                "options": [
                    "An algorithmic technique for solving problems by breaking them into smaller overlapping subproblems",
                    "A technique to improve search algorithms",
                    "A method of sorting large data sets",
                    "An approach to improve greedy algorithms"
                ],
                "correctAnswer": "An algorithmic technique for solving problems by breaking them into smaller overlapping subproblems"
            }
        ],"javascript": [
            {
                "question": "What is the difference between `null` and `undefined` in JavaScript?",
                "options": [
                    "`null` is a primitive value, `undefined` is an object",
                    "`null` is an object, `undefined` is a primitive value",
                    "`null` is used for variables without a value, `undefined` is for objects",
                    "There is no difference, they are the same"
                ],
                "correctAnswer": "`null` is an object, `undefined` is a primitive value"
            },
            {
                "question": "What does the `this` keyword refer to in JavaScript?",
                "options": [
                    "It refers to the global object",
                    "It refers to the current function",
                    "It refers to the object from which the function was called",
                    "It refers to the window object"
                ],
                "correctAnswer": "It refers to the object from which the function was called"
            },
            {
                "question": "What is a closure in JavaScript?",
                "options": [
                    "A function that is called after an event",
                    "A function that is defined inside another function and can access the outer function's variables",
                    "A block of code that is executed once",
                    "A technique used to debug JavaScript code"
                ],
                "correctAnswer": "A function that is defined inside another function and can access the outer function's variables"
            },
            {
                "question": "Which of the following methods can be used to convert a string into an integer in JavaScript?",
                "options": [
                    "parseInt()",
                    "toString()",
                    "Integer()",
                    "stringify()"
                ],
                "correctAnswer": "parseInt()"
            },
            {
                "question": "What is the purpose of the `setTimeout()` function in JavaScript?",
                "options": [
                    "It sets a delay before executing a function",
                    "It sets a timeout for a network request",
                    "It pauses the execution of a function for a given time",
                    "It sets the timeout for an event listener"
                ],
                "correctAnswer": "It sets a delay before executing a function"
            }
        ],"object-oriented programming": [
            {
                "question": "What is the concept of inheritance in Object-Oriented Programming?",
                "options": [
                    "A way to define multiple classes in a program",
                    "A technique where a new class can inherit properties and methods from an existing class",
                    "A way to declare global variables",
                    "A way to reuse a function"
                ],
                "correctAnswer": "A technique where a new class can inherit properties and methods from an existing class"
            },
            {
                "question": "What is polymorphism in Object-Oriented Programming?",
                "options": [
                    "The ability to call a method with different arguments",
                    "The ability of a class to have more than one method with the same name but different signatures",
                    "The ability to use a method from another class",
                    "The ability to override a method from a parent class"
                ],
                "correctAnswer": "The ability of a class to have more than one method with the same name but different signatures"
            },
            {
                "question": "What is encapsulation in Object-Oriented Programming?",
                "options": [
                    "The process of hiding the internal implementation details of an object and only exposing the necessary parts",
                    "The ability of an object to hold multiple values",
                    "The concept of creating a new class from an existing one",
                    "The use of dynamic typing in a class"
                ],
                "correctAnswer": "The process of hiding the internal implementation details of an object and only exposing the necessary parts"
            },
            {
                "question": "Which of the following is true about an abstract class in OOP?",
                "options": [
                    "An abstract class cannot have any methods",
                    "An abstract class can be instantiated directly",
                    "An abstract class can contain both fully implemented methods and abstract methods",
                    "An abstract class can only be used as a base for other abstract classes"
                ],
                "correctAnswer": "An abstract class can contain both fully implemented methods and abstract methods"
            },
            {
                "question": "What does the term 'overloading' refer to in Object-Oriented Programming?",
                "options": [
                    "Overriding a method in a subclass",
                    "Defining a method with the same name but different parameters in the same class",
                    "Creating multiple constructors in a class",
                    "Creating a class that performs multiple functions"
                ],
                "correctAnswer": "Defining a method with the same name but different parameters in the same class"
            }
        ], "computer networks": [
            {
                "question": "What is the OSI Model in computer networking?",
                "options": [
                    "A network security protocol",
                    "A conceptual framework used to understand network interactions in seven layers",
                    "A type of physical network cable",
                    "A type of routing algorithm"
                ],
                "correctAnswer": "A conceptual framework used to understand network interactions in seven layers"
            },
            {
                "question": "What is the main difference between TCP and UDP?",
                "options": [
                    "TCP is connectionless, while UDP is connection-oriented",
                    "TCP is connection-oriented, while UDP is connectionless",
                    "TCP is faster than UDP",
                    "UDP uses less bandwidth than TCP"
                ],
                "correctAnswer": "TCP is connection-oriented, while UDP is connectionless"
            },
            {
                "question": "Which of the following is a function of the Network Layer in the OSI model?",
                "options": [
                    "Establishing, managing, and terminating connections",
                    "Error detection and correction",
                    "Routing and forwarding of data packets",
                    "Data encryption"
                ],
                "correctAnswer": "Routing and forwarding of data packets"
            },
            {
                "question": "What is the purpose of the ARP protocol in a computer network?",
                "options": [
                    "To resolve domain names to IP addresses",
                    "To map an IP address to a MAC address",
                    "To control the flow of data packets",
                    "To establish a connection between two devices"
                ],
                "correctAnswer": "To map an IP address to a MAC address"
            },
            {
                "question": "Which protocol is used to securely send data over the internet?",
                "options": [
                    "HTTP",
                    "FTP",
                    "SSH",
                    "HTTPS"
                ],
                "correctAnswer": "HTTPS"
            }
        ],"software engineering": [
            {
                "question": "What is the purpose of software requirements gathering?",
                "options": [
                    "To write the code for the software",
                    "To identify the needs and expectations of the stakeholders",
                    "To test the software",
                    "To deploy the software"
                ],
                "correctAnswer": "To identify the needs and expectations of the stakeholders"
            },
            {
                "question": "What is the difference between functional and non-functional requirements?",
                "options": [
                    "Functional requirements define what the system should do, while non-functional requirements define how the system should perform",
                    "Functional requirements are related to the system architecture, while non-functional requirements are related to the user interface",
                    "Functional requirements are optional, while non-functional requirements are mandatory",
                    "There is no difference; both are the same"
                ],
                "correctAnswer": "Functional requirements define what the system should do, while non-functional requirements define how the system should perform"
            },
            {
                "question": "What is the purpose of software testing?",
                "options": [
                    "To check if the code runs correctly",
                    "To identify bugs and errors in the software",
                    "To ensure that the system performs efficiently",
                    "To improve the software’s security"
                ],
                "correctAnswer": "To identify bugs and errors in the software"
            },
            {
                "question": "Which software development model focuses on repetitive cycles of software development?",
                "options": [
                    "Waterfall Model",
                    "V-Model",
                    "Agile Model",
                    "Spiral Model"
                ],
                "correctAnswer": "Agile Model"
            },
            {
                "question": "What is version control in software engineering?",
                "options": [
                    "A way to ensure that the software runs faster",
                    "A technique to track changes to the codebase and collaborate with others",
                    "A process for monitoring software usage",
                    "A method to compress the code for deployment"
                ],
                "correctAnswer": "A technique to track changes to the codebase and collaborate with others"
            }
        ],"deep learning": [
            {
                "question": "What is deep learning?",
                "options": [
                    "A type of machine learning that uses neural networks with many layers",
                    "A machine learning algorithm for supervised learning only",
                    "A technique to extract features from structured data",
                    "A method for traditional linear regression"
                ],
                "correctAnswer": "A type of machine learning that uses neural networks with many layers"
            },
            {
                "question": "What is a neural network?",
                "options": [
                    "A data structure used in deep learning algorithms",
                    "A collection of algorithms designed to recognize patterns",
                    "A framework for organizing databases",
                    "A method to compress large datasets"
                ],
                "correctAnswer": "A collection of algorithms designed to recognize patterns"
            },
            {
                "question": "What is the purpose of the activation function in a neural network?",
                "options": [
                    "To control the flow of data through the network",
                    "To normalize the input data before feeding it into the network",
                    "To introduce non-linearity into the network",
                    "To initialize the weights in the network"
                ],
                "correctAnswer": "To introduce non-linearity into the network"
            },
            {
                "question": "Which of the following is a common activation function used in deep learning?",
                "options": [
                    "Linear",
                    "Sigmoid",
                    "Euclidean",
                    "Exponential"
                ],
                "correctAnswer": "Sigmoid"
            },
            {
                "question": "What is overfitting in deep learning?",
                "options": [
                    "When the model learns too much from the training data, resulting in poor generalization to new data",
                    "When the model does not learn enough from the training data",
                    "When the model runs faster due to too many parameters",
                    "When the neural network is too shallow"
                ],
                "correctAnswer": "When the model learns too much from the training data, resulting in poor generalization to new data"
            }
        ], "natural language processing": [
            {
                "question": "What is Natural Language Processing (NLP)?",
                "options": [
                    "A field of artificial intelligence that deals with the interaction between computers and human languages",
                    "A machine learning algorithm for image recognition",
                    "A type of neural network for time series forecasting",
                    "A method of analyzing large datasets for pattern detection"
                ],
                "correctAnswer": "A field of artificial intelligence that deals with the interaction between computers and human languages"
            },
            {
                "question": "What is tokenization in NLP?",
                "options": [
                    "The process of dividing a text into smaller units like words or phrases",
                    "The process of removing stop words from a text",
                    "The technique of translating text into a different language",
                    "The method of assigning labels to words in a sentence"
                ],
                "correctAnswer": "The process of dividing a text into smaller units like words or phrases"
            },
            {
                "question": "Which of the following is a common technique used for text classification in NLP?",
                "options": [
                    "K-means clustering",
                    "Logistic Regression",
                    "Principal Component Analysis",
                    "Kalman Filtering"
                ],
                "correctAnswer": "Logistic Regression"
            },
            {
                "question": "What is Named Entity Recognition (NER) in NLP?",
                "options": [
                    "A technique used to recognize and classify named entities like persons, organizations, and locations in text",
                    "A method for encoding text data into numerical vectors",
                    "A method for removing punctuation from text",
                    "A technique for translating text from one language to another"
                ],
                "correctAnswer": "A technique used to recognize and classify named entities like persons, organizations, and locations in text"
            },
            {
                "question": "What is word embedding in NLP?",
                "options": [
                    "The process of converting words into fixed-length vector representations",
                    "A method of counting word frequency in a document",
                    "The technique of replacing words with synonyms",
                    "A way to remove stop words from a sentence"
                ],
                "correctAnswer": "The process of converting words into fixed-length vector representations"
            }
        ],"data analysis": [
            {
                "question": "What is the first step in a typical data analysis process?",
                "options": [
                    "Cleaning the data",
                    "Collecting the data",
                    "Analyzing the data",
                    "Visualizing the data"
                ],
                "correctAnswer": "Collecting the data"
            },
            {
                "question": "What is the purpose of data cleaning in data analysis?",
                "options": [
                    "To make the data more consistent by removing or correcting errors",
                    "To visualize the data in graphs and charts",
                    "To run statistical tests on the data",
                    "To generate reports from the data"
                ],
                "correctAnswer": "To make the data more consistent by removing or correcting errors"
            },
            {
                "question": "Which of the following is a type of data visualization technique?",
                "options": [
                    "Data cleaning",
                    "Histograms",
                    "Data modeling",
                    "Data transformation"
                ],
                "correctAnswer": "Histograms"
            },
            {
                "question": "What is a correlation in data analysis?",
                "options": [
                    "A relationship between two or more variables where changes in one are associated with changes in another",
                    "The process of collecting large datasets",
                    "A method of cleaning data by removing outliers",
                    "The process of visualizing data on a map"
                ],
                "correctAnswer": "A relationship between two or more variables where changes in one are associated with changes in another"
            },
            {
                "question": "Which of the following libraries is commonly used for data analysis in Python?",
                "options": [
                    "TensorFlow",
                    "NumPy",
                    "React",
                    "Django"
                ],
                "correctAnswer": "NumPy"
            }
        ],

    }

    return sample_data.get(topic.lower(), [{"question": "No data", "options": [], "correctAnswer": "Sorry, no Q&A for this topic yet."}])
