"""
Module containing Author class. Part of the author_reputation package.
Eric Vin, 2019
"""

class Author:
    """
    Class representing an author article. Currently assumes that reputation is
    calculated in order, though methods are abstracted to allow for out of order
    pulling in the future (As is described in paper).
    """

    def __init__(self, author_id, starting_reputation):
        """
        Author Constructor:
            -author_id: A unique identifier representing the author
            -starting_reputation: The reputation where the author should start
        """
        #Sets the author_id to the passed author_id
        self.author_id = author_id

        #Initializes the author's reputation to the starting reputation passed
        self.reputation = starting_reputation

    def __str__(self):
        """
        Returns a string interpretation of this Author
        """
        return "Author ID: " + str(self.author_id) + "    Reputation:" + str(self.reputation)

    def get_author_rep(self):
        """
        Returns the author's reputation
        """
        return self.reputation

    def set_author_rep(self, new_author_rep):
        """
        Sets the author's reputation
        """
        self.reputation = new_author_rep

    @classmethod
    def check_same_author(cls, author_1, author_2):
        """
        Checks if the two passed authors are the same author.
        Currently does this by comparing the ids of the authors.
        """
        if author_1.author_id == author_2.author_id:
            return True

        return False
