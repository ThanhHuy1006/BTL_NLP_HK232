import nltk
from nltk import Tree

# Define the function to display a parse tree
def draw_parse_tree(tree):
    tree.draw()

# Define the function to create parse trees with semantic annotations
def create_trees():
    # Tree for "Who saw the dog?"
    t1 = Tree('S', [
        Tree('WH-NP', [Tree('Who', ['who'])]),
        Tree('VP', [
            Tree('VBD', [Tree('saw', ['λx.λy.see(x, y)'])]),
            Tree('NP', [
                Tree('DT', [Tree('the', ['λP.ιx[P(x)]'])]),
                Tree('NN', [Tree('dog', ['dog'])])
            ])
        ]),
    ])

    # Tree for "Who did John give the book to?"
    t2 = Tree('S', [
        Tree('WH-NP', [Tree('Who', ['who'])]),
        Tree('VP', [
            Tree('VBD', [Tree('did', ['λp.p'])]),
            Tree('NP', [Tree('NNP', [Tree('John', ['john'])])]),
            Tree('VP', [
                Tree('VB', [Tree('give', ['λx.λy.λz.give(x, y, z)'])]),
                Tree('NP', [
                    Tree('DT', [Tree('the', ['λP.ιx[P(x)]'])]),
                    Tree('NN', [Tree('book', ['book'])])
                ]),
                Tree('PP', [
                    Tree('TO', [Tree('to', ['to'])]),
                    Tree('NP', [Tree('PRP', [Tree('_', ['_'])])])
                ])
            ])
        ])
    ])

    # Draw the trees
    print("Parse Tree for 'Who did John give the book to?':")
    draw_parse_tree(t2)

# Call the function to create and draw the parse trees
create_trees()

